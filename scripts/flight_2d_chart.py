"""
ArduPilot BIN log to interactive 2D telemetry chart.

Extracts position, attitude, and speed telemetry from an ArduPilot
DataFlash log (.BIN) and generates a self-contained interactive HTML
chart where the user selects the Y-axis metric and hovering over any
point shows a full telemetry table.
"""

from __future__ import annotations

import json
import math
from bisect import bisect_left
from pathlib import Path
from typing import Any

from pymavlink import mavutil

# =============================================================================
# USER CONSTANTS
# =============================================================================
LOG_FILE_PATH = "00000001.BIN"
OUTPUT_HTML_PATH = "flight_2d_chart.html"
DOWNSAMPLE_STEP = 3          # reduce for more resolution, increase for speed

# Optional time window in seconds from log start.
START_TIME_SECONDS = 448    # set to None for full file
END_TIME_SECONDS = 1530    # set to None for full file


# =============================================================================
# DATA EXTRACTION  (identical pipeline to the 3-D script)
# =============================================================================

Record = dict[str, Any]


def _msg_to_record(msg, fields: list[str]) -> Record:
    return {f: getattr(msg, f) for f in fields if hasattr(msg, f)}


def _nearest_record(records: list[Record], t: float, tolerance_s: float) -> Record | None:
    if not records:
        return None

    times = [float(record["t"]) for record in records]
    index = bisect_left(times, t)
    best: tuple[float, Record] | None = None

    for candidate_index in (index - 1, index):
        if 0 <= candidate_index < len(records):
            record = records[candidate_index]
            delta = abs(float(record["t"]) - t)
            if delta <= tolerance_s and (best is None or delta < best[0]):
                best = (delta, record)

    return best[1] if best else None


def _has_value(record: Record | None, field: str) -> bool:
    return record is not None and field in record and record[field] is not None


def extract_flight_data(log_path: Path) -> list[Record]:
    mavlog = mavutil.mavlink_connection(str(log_path))
    pos_records, att_records, gps_records, xkf1_records, rcin_records = [], [], [], [], []

    while True:
        msg = mavlog.recv_match()
        if msg is None:
            break
        msg_type = msg.get_type()
        if not hasattr(msg, "TimeUS"):
            continue
        t = msg.TimeUS / 1e6

        if msg_type == "POS":
            rec = _msg_to_record(msg, ["Lat", "Lng", "Alt", "RelHomeAlt"])
            rec["t"] = t
            pos_records.append(rec)
        elif msg_type == "ATT":
            rec = _msg_to_record(msg, ["Roll", "Pitch", "Yaw"])
            rec["t"] = t
            att_records.append(rec)
        elif msg_type == "GPS":
            rec = _msg_to_record(msg, ["Spd", "Status", "NSats"])
            rec["t"] = t
            gps_records.append(rec)
        elif msg_type == "XKF1":
            rec = _msg_to_record(msg, ["VN", "VE", "VD"])
            rec["t"] = t
            xkf1_records.append(rec)
        elif msg_type == "RCIN":
            # C3 = throttle stick PWM (typically 1000–2000 µs)
            rec = _msg_to_record(msg, ["C3"])
            rec["t"] = t
            rcin_records.append(rec)

    if not pos_records or not att_records:
        raise RuntimeError("Required POS/ATT data not found in log.")

    pos_records.sort(key=lambda record: record["t"])
    att_records.sort(key=lambda record: record["t"])
    gps_records.sort(key=lambda record: record["t"])
    xkf1_records.sort(key=lambda record: record["t"])
    rcin_records.sort(key=lambda record: record["t"])

    merged: list[Record] = []
    for pos in pos_records:
        t = float(pos["t"])
        att = _nearest_record(att_records, t, 0.2)
        if att is None:
            continue

        gps = _nearest_record(gps_records, t, 0.5)
        xkf1 = _nearest_record(xkf1_records, t, 0.5)
        rcin = _nearest_record(rcin_records, t, 0.5)

        vn = float(xkf1["VN"]) if _has_value(xkf1, "VN") else None
        ve = float(xkf1["VE"]) if _has_value(xkf1, "VE") else None
        vd = float(xkf1["VD"]) if _has_value(xkf1, "VD") else None
        ekf_speed_mps = math.hypot(vn, ve) if vn is not None and ve is not None else None
        speed_mps = float(gps["Spd"]) if _has_value(gps, "Spd") else (ekf_speed_mps or 0.0)

        merged.append(
            {
                "t": t,
                "Lat": float(pos["Lat"]),
                "Lng": float(pos["Lng"]),
                "Alt": float(pos["Alt"]),
                "RelHomeAlt": float(pos.get("RelHomeAlt", 0.0)),
                "Roll": float(att["Roll"]),
                "Pitch": float(att["Pitch"]),
                "Yaw": float(att["Yaw"]),
                "VN": vn,
                "VE": ve,
                "VD": vd,
                "C3": float(rcin["C3"]) if _has_value(rcin, "C3") else None,
                "speed_mps": speed_mps,
                "vspeed_mps": -vd if vd is not None else None,
                "horiz_speed_mps": ekf_speed_mps if ekf_speed_mps is not None else speed_mps,
            }
        )

    # Normalise RCIN C3 PWM (1000-2000 us) to 0-100%.
    c3_values = [float(record["C3"]) for record in merged if record["C3"] is not None]
    pwm_min = min(c3_values) if c3_values else None
    pwm_max = max(c3_values) if c3_values else None
    for record in merged:
        if record["C3"] is not None and pwm_min is not None and pwm_max is not None and pwm_max > pwm_min:
            record["throttle_pct"] = max(0.0, min(100.0, (float(record["C3"]) - pwm_min) / (pwm_max - pwm_min) * 100.0))
        elif record["C3"] is not None:
            record["throttle_pct"] = 0.0
        else:
            record["throttle_pct"] = None

    previous: Record | None = None
    for record in merged:
        if record["vspeed_mps"] is None:
            if previous is not None:
                dt = float(record["t"]) - float(previous["t"])
                record["vspeed_mps"] = (float(record["Alt"]) - float(previous["Alt"])) / dt if dt > 0 else 0.0
            else:
                record["vspeed_mps"] = 0.0

        if previous is not None:
            dt = float(record["t"]) - float(previous["t"])
            dv = float(record["horiz_speed_mps"]) - float(previous["horiz_speed_mps"])
            record["accel_mps2"] = dv / dt if dt > 0 else 0.0
        else:
            record["accel_mps2"] = 0.0
        previous = record

    return merged


def add_relative_time(records: list[Record]) -> list[Record]:
    t0 = float(records[0]["t"])
    out = []
    for record in records:
        next_record = record.copy()
        next_record["t_rel"] = float(record["t"]) - t0
        out.append(next_record)
    return out


def filter_by_time_window(records: list[Record], start_s: float | None, end_s: float | None) -> list[Record]:
    out = records
    if start_s is not None:
        out = [record for record in out if float(record["t_rel"]) >= float(start_s)]
    if end_s is not None:
        out = [record for record in out if float(record["t_rel"]) <= float(end_s)]
    return out


def downsample(records: list[Record], step: int) -> list[Record]:
    return records[::max(1, step)]


# =============================================================================
# HTML GENERATION
# =============================================================================

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flight Telemetry — {title}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Barlow:wght@300;400;600;700&display=swap');

  :root {{
    --bg:        #0a0c10;
    --surface:   #111520;
    --border:    #1e2535;
    --accent:    #00e5ff;
    --accent2:   #ff3d71;
    --accent3:   #a259ff;
    --text:      #c8d6e5;
    --dim:       #4a5568;
    --chart-h:   520px;
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    background: var(--bg);
    color: var(--text);
    font-family: 'Barlow', sans-serif;
    font-weight: 300;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }}

  /* ── header ── */
  header {{
    padding: 28px 36px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 18px;
  }}
  .logo-mark {{
    width: 38px; height: 38px;
    background: var(--accent);
    clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
    flex-shrink: 0;
  }}
  header h1 {{
    font-size: 1.15rem;
    font-weight: 600;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #fff;
  }}
  header span {{
    font-family: 'Share Tech Mono', monospace;
    font-size: .78rem;
    color: var(--dim);
    margin-left: auto;
  }}

  /* ── controls ── */
  .controls {{
    padding: 18px 36px;
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
    border-bottom: 1px solid var(--border);
    background: var(--surface);
  }}
  .controls label {{
    font-size: .8rem;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--dim);
  }}
  .metric-btn {{
    padding: 7px 18px;
    border: 1px solid var(--border);
    border-radius: 3px;
    background: transparent;
    color: var(--text);
    font-family: 'Barlow', sans-serif;
    font-size: .85rem;
    cursor: pointer;
    transition: all .18s;
  }}
  .metric-btn:hover {{ border-color: var(--accent); color: var(--accent); }}
  .metric-btn.active {{
    background: var(--accent);
    border-color: var(--accent);
    color: #000;
    font-weight: 600;
  }}

  /* ── chart wrapper ── */
  .chart-area {{
    flex: 1;
    padding: 24px 36px;
    position: relative;
  }}
  canvas {{
    width: 100% !important;
    height: var(--chart-h) !important;
    display: block;
  }}

  /* ── tooltip ── */
  #tooltip {{
    position: fixed;
    pointer-events: none;
    background: rgba(10,12,16,.96);
    border: 1px solid var(--accent);
    border-radius: 4px;
    padding: 12px 16px;
    font-family: 'Share Tech Mono', monospace;
    font-size: .75rem;
    color: var(--text);
    z-index: 9999;
    opacity: 0;
    transition: opacity .12s;
    min-width: 220px;
    line-height: 1.8;
    box-shadow: 0 0 24px rgba(0,229,255,.12);
  }}
  #tooltip.visible {{ opacity: 1; }}
  #tooltip .tt-title {{
    font-family: 'Barlow', sans-serif;
    font-weight: 700;
    font-size: .82rem;
    color: var(--accent);
    border-bottom: 1px solid var(--border);
    padding-bottom: 6px;
    margin-bottom: 6px;
    letter-spacing: .06em;
    text-transform: uppercase;
  }}
  #tooltip table {{ width: 100%; border-collapse: collapse; }}
  #tooltip td {{ padding: 1px 0; }}
  #tooltip td:first-child {{ color: var(--dim); padding-right: 12px; }}
  #tooltip td:last-child {{ color: #fff; text-align: right; font-weight: bold; }}

  /* ── stat strip ── */
  .stats {{
    display: flex;
    gap: 0;
    border-top: 1px solid var(--border);
  }}
  .stat {{
    flex: 1;
    padding: 14px 24px;
    border-right: 1px solid var(--border);
    text-align: center;
  }}
  .stat:last-child {{ border-right: none; }}
  .stat-val {{
    font-family: 'Share Tech Mono', monospace;
    font-size: 1.35rem;
    color: var(--accent);
    display: block;
  }}
  .stat-lbl {{
    font-size: .7rem;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--dim);
    margin-top: 2px;
    display: block;
  }}
</style>
</head>
<body>

<header>
  <div class="logo-mark"></div>
  <h1>Flight Telemetry Viewer</h1>
  <span id="file-label">{title}</span>
</header>

<div class="controls">
  <label>Y-Axis&nbsp;&nbsp;</label>
  <button class="metric-btn active" data-metric="airspeed">Air Speed</button>
  <button class="metric-btn" data-metric="altitude">Altitude</button>
  <button class="metric-btn" data-metric="vspeed">Vertical Speed</button>
  <button class="metric-btn" data-metric="accel">Acceleration</button>
  <button class="metric-btn" data-metric="throttle">Throttle</button>
</div>

<div class="chart-area">
  <canvas id="chart"></canvas>
</div>

<div class="stats">
  <div class="stat"><span class="stat-val" id="sv-duration">—</span><span class="stat-lbl">Duration (s)</span></div>
  <div class="stat"><span class="stat-val" id="sv-maxspd">—</span><span class="stat-lbl">Max Speed (m/s)</span></div>
  <div class="stat"><span class="stat-val" id="sv-maxalt">—</span><span class="stat-lbl">Max Altitude (m rel)</span></div>
  <div class="stat"><span class="stat-val" id="sv-samples">—</span><span class="stat-lbl">Data Points</span></div>
</div>

<div id="tooltip"></div>

<script>
// ── Embedded telemetry ──────────────────────────────────────────────────────
const TELEM = {telemetry_json};

// ── Metric definitions ──────────────────────────────────────────────────────
const METRICS = {{
  airspeed: {{ key: "speed_mps", label: "Air Speed",       unit: "m/s",  color: "#00e5ff",  fill: "rgba(0,229,255,.08)"  }},
  altitude: {{ key: "z_alt",     label: "Altitude",        unit: "m",    color: "#a259ff",  fill: "rgba(162,89,255,.08)" }},
  vspeed:   {{ key: "vspeed",    label: "Vertical Speed",  unit: "m/s",  color: "#00ff9d",  fill: "rgba(0,255,157,.08)"  }},
  accel:    {{ key: "accel",     label: "Acceleration",    unit: "m/s²", color: "#ff3d71",  fill: "rgba(255,61,113,.08)" }},
  throttle: {{ key: "throttle",  label: "Throttle",        unit: "%",    color: "#ffb830",  fill: "rgba(255,184,48,.08)" }},
}};

// ── Stat strip ──────────────────────────────────────────────────────────────
const duration = (TELEM.t[TELEM.t.length-1] - TELEM.t[0]).toFixed(1);
const maxSpd   = Math.max(...TELEM.speed_mps).toFixed(1);
const maxAlt   = Math.max(...TELEM.z_alt).toFixed(1);
document.getElementById("sv-duration").textContent = duration;
document.getElementById("sv-maxspd").textContent   = maxSpd;
document.getElementById("sv-maxalt").textContent   = maxAlt;
document.getElementById("sv-samples").textContent  = TELEM.t.length;

// ── Canvas chart ────────────────────────────────────────────────────────────
const canvas  = document.getElementById("chart");
const ctx     = canvas.getContext("2d");
let activeMetric = "airspeed";
let mouseX = -1, mouseY = -1, nearestIdx = -1;

function dpr() {{ return window.devicePixelRatio || 1; }}

function resize() {{
  const r = dpr();
  const w = canvas.parentElement.clientWidth - 72;   // account for padding
  const h = parseInt(getComputedStyle(document.documentElement).getPropertyValue("--chart-h"));
  canvas.width  = w * r;
  canvas.height = h * r;
  ctx.scale(r, r);
  draw();
}}

// Padding
const PAD = {{ top: 28, right: 30, bottom: 54, left: 72 }};

function plotW() {{ return (canvas.width  / dpr()) - PAD.left - PAD.right; }}
function plotH() {{ return (canvas.height / dpr()) - PAD.top  - PAD.bottom; }}

function valToPixel(val, min, max, axis) {{
  const t = (val - min) / (max - min || 1);
  return axis === "x"
    ? PAD.left + t * plotW()
    : PAD.top  + (1 - t) * plotH();
}}

function draw() {{
  const W = canvas.width  / dpr();
  const H = canvas.height / dpr();
  ctx.clearRect(0, 0, W, H);

  const m     = METRICS[activeMetric];
  const xs    = TELEM.t;
  const ys    = TELEM[m.key];
  const xMin  = xs[0], xMax = xs[xs.length-1];
  let yMin    = Math.min(...ys), yMax = Math.max(...ys);
  const yPad  = (yMax - yMin) * .1 || 1;
  yMin -= yPad; yMax += yPad;

  // Grid lines
  ctx.strokeStyle = "#1e2535";
  ctx.lineWidth   = 1;
  const gridX = 8, gridY = 6;
  for (let i = 0; i <= gridX; i++) {{
    const px = PAD.left + (i / gridX) * plotW();
    ctx.beginPath(); ctx.moveTo(px, PAD.top); ctx.lineTo(px, PAD.top + plotH()); ctx.stroke();
  }}
  for (let i = 0; i <= gridY; i++) {{
    const py = PAD.top + (i / gridY) * plotH();
    ctx.beginPath(); ctx.moveTo(PAD.left, py); ctx.lineTo(PAD.left + plotW(), py); ctx.stroke();
  }}

  // Zero line
  if (yMin < 0 && yMax > 0) {{
    const py = valToPixel(0, yMin, yMax, "y");
    ctx.strokeStyle = "#2a3040";
    ctx.lineWidth   = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(PAD.left, py); ctx.lineTo(PAD.left + plotW(), py); ctx.stroke();
    ctx.setLineDash([]);
  }}

  // Filled area
  ctx.beginPath();
  ctx.moveTo(valToPixel(xs[0], xMin, xMax, "x"), valToPixel(0 > yMin ? 0 : yMin, yMin, yMax, "y"));
  for (let i = 0; i < xs.length; i++) {{
    ctx.lineTo(valToPixel(xs[i], xMin, xMax, "x"), valToPixel(ys[i], yMin, yMax, "y"));
  }}
  const baseY = valToPixel(Math.max(0, yMin), yMin, yMax, "y");
  ctx.lineTo(valToPixel(xs[xs.length-1], xMin, xMax, "x"), baseY);
  ctx.lineTo(valToPixel(xs[0], xMin, xMax, "x"), baseY);
  ctx.closePath();
  ctx.fillStyle = m.fill;
  ctx.fill();

  // Line
  ctx.beginPath();
  ctx.moveTo(valToPixel(xs[0], xMin, xMax, "x"), valToPixel(ys[0], yMin, yMax, "y"));
  for (let i = 1; i < xs.length; i++) {{
    ctx.lineTo(valToPixel(xs[i], xMin, xMax, "x"), valToPixel(ys[i], yMin, yMax, "y"));
  }}
  ctx.strokeStyle = m.color;
  ctx.lineWidth   = 2.2;
  ctx.lineJoin    = "round";
  ctx.stroke();

  // Axis labels — X
  ctx.fillStyle  = "#4a5568";
  ctx.font       = "11px 'Share Tech Mono', monospace";
  ctx.textAlign  = "center";
  ctx.textBaseline = "top";
  for (let i = 0; i <= gridX; i++) {{
    const v  = xMin + (i / gridX) * (xMax - xMin);
    const px = PAD.left + (i / gridX) * plotW();
    ctx.fillText(v.toFixed(0) + "s", px, PAD.top + plotH() + 10);
  }}

  // Axis labels — Y
  ctx.textAlign   = "right";
  ctx.textBaseline = "middle";
  for (let i = 0; i <= gridY; i++) {{
    const v  = yMax - (i / gridY) * (yMax - yMin);
    const py = PAD.top + (i / gridY) * plotH();
    ctx.fillText(v.toFixed(1), PAD.left - 8, py);
  }}

  // Axis titles
  ctx.fillStyle = "#6b7a99";
  ctx.font = "12px 'Barlow', sans-serif";
  ctx.textAlign = "center"; ctx.textBaseline = "bottom";
  ctx.fillText("Time (s)", PAD.left + plotW() / 2, H - 4);

  ctx.save();
  ctx.translate(16, PAD.top + plotH() / 2);
  ctx.rotate(-Math.PI / 2);
  ctx.textAlign = "center"; ctx.textBaseline = "middle";
  ctx.fillText(m.label + " (" + m.unit + ")", 0, 0);
  ctx.restore();

  // Hover crosshair + dot
  if (nearestIdx >= 0) {{
    const px = valToPixel(xs[nearestIdx], xMin, xMax, "x");
    const py = valToPixel(ys[nearestIdx], yMin, yMax, "y");

    // Vertical line
    ctx.strokeStyle = "rgba(255,255,255,.15)";
    ctx.lineWidth   = 1;
    ctx.setLineDash([3, 4]);
    ctx.beginPath(); ctx.moveTo(px, PAD.top); ctx.lineTo(px, PAD.top + plotH()); ctx.stroke();
    ctx.setLineDash([]);

    // Dot
    ctx.beginPath();
    ctx.arc(px, py, 6, 0, Math.PI * 2);
    ctx.fillStyle   = m.color;
    ctx.fill();
    ctx.strokeStyle = "#fff";
    ctx.lineWidth   = 1.5;
    ctx.stroke();
  }}
}}

// ── Tooltip ─────────────────────────────────────────────────────────────────
const tooltip = document.getElementById("tooltip");

function fmt(v, dec) {{
  if (v === null || v === undefined || isNaN(v)) return "—";
  return (+v).toFixed(dec);
}}

function showTooltip(i, px, py) {{
  const rows = [
    ["Time",         fmt(TELEM.t[i], 2)  + " s"],
    ["Air speed",    fmt(TELEM.speed_mps[i], 2) + " m/s  (" + fmt(TELEM.speed_mps[i]*3.6, 1) + " km/h)"],
    ["Altitude",     fmt(TELEM.z_alt[i], 1) + " m"],
    ["Vert. speed",  fmt(TELEM.vspeed[i],  2) + " m/s"],
    ["Accel.",       fmt(TELEM.accel[i],   2) + " m/s²"],
    ["Throttle",     fmt(TELEM.throttle[i], 1) + " %"],
    ["Roll",         fmt(TELEM.roll[i],    1) + " °"],
    ["Pitch",        fmt(TELEM.pitch[i],   1) + " °"],
    ["Yaw",          fmt(TELEM.yaw[i],     1) + " °"],
    ["Lat",          fmt(TELEM.lat[i],     6)],
    ["Lng",          fmt(TELEM.lng[i],     6)],
  ];
  const tableRows = rows.map(r => `<tr><td>${{r[0]}}</td><td>${{r[1]}}</td></tr>`).join("");
  tooltip.innerHTML = `<div class="tt-title">Frame ${{i}}</div><table>${{tableRows}}</table>`;
  tooltip.classList.add("visible");

  let left = px + 18, top = py - 10;
  if (left + 260 > window.innerWidth)  left = px - 260;
  if (top  + 260 > window.innerHeight) top  = py - 260;
  tooltip.style.left = left + "px";
  tooltip.style.top  = top  + "px";
}}

function hideTooltip() {{
  tooltip.classList.remove("visible");
  nearestIdx = -1;
  draw();
}}

// ── Mouse interaction ────────────────────────────────────────────────────────
canvas.addEventListener("mousemove", e => {{
  const rect  = canvas.getBoundingClientRect();
  mouseX = e.clientX - rect.left;
  mouseY = e.clientY - rect.top;

  const xs   = TELEM.t;
  const xMin = xs[0], xMax = xs[xs.length - 1];

  // Map mouse X → data index
  const t = (mouseX - PAD.left) / plotW() * (xMax - xMin) + xMin;
  let best = 0, bestDist = Infinity;
  for (let i = 0; i < xs.length; i++) {{
    const d = Math.abs(xs[i] - t);
    if (d < bestDist) {{ bestDist = d; best = i; }}
  }}

  if (mouseX >= PAD.left && mouseX <= PAD.left + plotW() &&
      mouseY >= PAD.top  && mouseY <= PAD.top  + plotH()) {{
    nearestIdx = best;
    draw();
    showTooltip(best, e.clientX, e.clientY);
  }} else {{
    hideTooltip();
  }}
}});
canvas.addEventListener("mouseleave", hideTooltip);

// ── Metric buttons ───────────────────────────────────────────────────────────
document.querySelectorAll(".metric-btn").forEach(btn => {{
  btn.addEventListener("click", () => {{
    document.querySelectorAll(".metric-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    activeMetric = btn.dataset.metric;
    nearestIdx = -1;
    draw();
  }});
}});

// ── Init ─────────────────────────────────────────────────────────────────────
window.addEventListener("resize", resize);
resize();
</script>
</body>
</html>
"""


def _round_or_none(value: Any, digits: int) -> float | None:
    if value is None:
        return None
    return round(float(value), digits)


def build_2d_chart(records: list[Record], html_out: Path, title: str) -> None:
    # Align altitude to relative (subtract first value for local frame)
    alt0 = float(records[0]["Alt"])

    telem = {
        "t":         [_round_or_none(record["t_rel"], 3) for record in records],
        "speed_mps": [_round_or_none(record["speed_mps"], 3) for record in records],
        "z_alt":     [_round_or_none(float(record["Alt"]) - alt0, 2) for record in records],
        "vspeed":    [_round_or_none(record["vspeed_mps"], 3) for record in records],
        "accel":     [_round_or_none(record["accel_mps2"], 3) for record in records],
        "throttle":  [_round_or_none(record["throttle_pct"], 1) for record in records],
        "roll":      [_round_or_none(record["Roll"], 2) for record in records],
        "pitch":     [_round_or_none(record["Pitch"], 2) for record in records],
        "yaw":       [_round_or_none(record["Yaw"], 2) for record in records],
        "lat":       [_round_or_none(record["Lat"], 6) for record in records],
        "lng":       [_round_or_none(record["Lng"], 6) for record in records],
    }

    html = HTML_TEMPLATE.format(
        title=title,
        telemetry_json=json.dumps(telem),
    )
    html_out.write_text(html, encoding="utf-8")


def main() -> None:
    log_path = Path(LOG_FILE_PATH)
    out_path = Path(OUTPUT_HTML_PATH)

    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    print(f"Reading log: {log_path}")
    data = extract_flight_data(log_path)
    data = add_relative_time(data)

    if START_TIME_SECONDS is not None and END_TIME_SECONDS is not None:
        if float(START_TIME_SECONDS) > float(END_TIME_SECONDS):
            raise ValueError("START_TIME_SECONDS must be <= END_TIME_SECONDS")

    filtered = filter_by_time_window(data, START_TIME_SECONDS, END_TIME_SECONDS)
    if not filtered:
        raise RuntimeError("No samples in selected time range. Adjust START_TIME_SECONDS / END_TIME_SECONDS.")

    ds = downsample(filtered, DOWNSAMPLE_STEP)
    print(f"Samples: total={len(data)} | selected={len(filtered)} | chart points={len(ds)}")

    build_2d_chart(ds, out_path, title=log_path.name)
    print(f"Chart saved to: {out_path}")


if __name__ == "__main__":
    main()
