from __future__ import annotations

import json
import re
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

APP_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = APP_ROOT.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
LOGS_DIR = PROJECT_ROOT / "logs"
GENERATED_DIR = APP_ROOT / "generated"
UPLOAD_DIR = APP_ROOT / "uploads"

for directory in (GENERATED_DIR, UPLOAD_DIR):
    directory.mkdir(parents=True, exist_ok=True)

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import detect_flight_window as window_detector  # noqa: E402
import flight_2d_chart as chart2d  # noqa: E402
import flight_3d_replay as replay3d  # noqa: E402


class LogSelectionError(RuntimeError):
    pass


Metric = dict[str, str]

METRICS: list[Metric] = [
    {"id": "speed_mps", "label": "Speed", "unit": "m/s", "color": "#00e5ff"},
    {"id": "z_alt", "label": "Altitude", "unit": "m", "color": "#a259ff"},
    {"id": "vspeed_mps", "label": "Vertical Speed", "unit": "m/s", "color": "#00ff9d"},
    {"id": "accel_mps2", "label": "Acceleration", "unit": "m/s2", "color": "#ff3d71"},
    {"id": "throttle_pct", "label": "Throttle", "unit": "%", "color": "#ffb830"},
    {"id": "Roll", "label": "Roll", "unit": "deg", "color": "#36f1cd"},
    {"id": "Pitch", "label": "Pitch", "unit": "deg", "color": "#ff8a3d"},
    {"id": "Yaw", "label": "Yaw", "unit": "deg", "color": "#6f8cff"},
    {"id": "VN", "label": "North Velocity", "unit": "m/s", "color": "#92ff4f"},
    {"id": "VE", "label": "East Velocity", "unit": "m/s", "color": "#44a4ff"},
    {"id": "VD", "label": "Down Velocity", "unit": "m/s", "color": "#ff5fd7"},
    {"id": "Lat", "label": "Latitude", "unit": "deg", "color": "#99a6ff"},
    {"id": "Lng", "label": "Longitude", "unit": "deg", "color": "#f0d35f"},
]

DEFAULT_METRICS = ["speed_mps", "z_alt", "vspeed_mps", "accel_mps2", "throttle_pct"]


def list_available_logs() -> list[dict[str, Any]]:
    logs: list[Path] = []
    if LOGS_DIR.exists():
        logs.extend(LOGS_DIR.glob("*.BIN"))
        logs.extend(LOGS_DIR.glob("*.bin"))
    if UPLOAD_DIR.exists():
        logs.extend(UPLOAD_DIR.glob("*.BIN"))
        logs.extend(UPLOAD_DIR.glob("*.bin"))

    seen = set()
    items = []
    for path in sorted(logs, key=lambda item: item.stat().st_mtime, reverse=True):
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        items.append({
            "name": path.name,
            "path": str(resolved),
            "size_mb": round(path.stat().st_size / (1024 * 1024), 2),
            "modified": path.stat().st_mtime,
            "location": "uploads" if UPLOAD_DIR in resolved.parents else "logs",
        })
    return items


def metric_catalog() -> list[Metric]:
    return [dict(metric, default=metric["id"] in DEFAULT_METRICS) for metric in METRICS]


def detect_window(log_path: Path) -> dict[str, float]:
    records = window_detector.extract_records(log_path)
    window = window_detector.detect_flight_window(records)
    payload = asdict(window)
    payload["duration_s"] = payload["end_time_s"] - payload["start_time_s"]
    return {key: round(float(value), 3) for key, value in payload.items()}


def generate_3d_replay(log_path: Path, window: dict[str, float]) -> Path:
    output = _output_path(log_path, "3d")
    data = replay3d.extract_flight_data(log_path)
    local = replay3d.lla_to_local_ned(data)
    filtered = replay3d.filter_by_time_window(local, window["start_time_s"], window["end_time_s"])
    if not filtered:
        raise RuntimeError("No 3D samples in the detected flight window.")
    local_kin = replay3d.add_kinematics(filtered)
    local_ds = replay3d.downsample_for_animation(local_kin, max(1, int(replay3d.ANIMATION_DOWNSAMPLE_STEP)))
    replay3d.build_3d_replay(local_ds, output, title=f"3D Flight Replay: {log_path.name}")
    return output


def generate_2d_chart(log_path: Path, window: dict[str, float], selected_metrics: list[str]) -> Path:
    output = _output_path(log_path, "2d")
    selected = _normalize_metrics(selected_metrics)
    data = chart2d.extract_flight_data(log_path)
    data = chart2d.add_relative_time(data)
    filtered = chart2d.filter_by_time_window(data, window["start_time_s"], window["end_time_s"])
    if not filtered:
        raise RuntimeError("No 2D samples in the detected flight window.")
    ds = chart2d.downsample(filtered, max(1, int(chart2d.DOWNSAMPLE_STEP)))
    _build_custom_2d_chart(ds, output, title=f"2D Flight Telemetry: {log_path.name}", selected_metrics=selected)
    return output


def _normalize_metrics(selected_metrics: list[str]) -> list[str]:
    allowed = {metric["id"] for metric in METRICS}
    selected = [metric for metric in selected_metrics if metric in allowed]
    return selected or DEFAULT_METRICS


def _output_path(log_path: Path, kind: str) -> Path:
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", log_path.stem)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    return GENERATED_DIR / f"{safe_name}_{kind}_{stamp}.html"


def _round_or_none(value: Any, digits: int) -> float | None:
    if value is None:
        return None
    return round(float(value), digits)


def _series_value(record: dict[str, Any], metric_id: str, alt0: float) -> float | None:
    if metric_id == "z_alt":
        return float(record["Alt"]) - alt0
    return record.get(metric_id)


def _build_custom_2d_chart(records: list[dict[str, Any]], html_out: Path, title: str, selected_metrics: list[str]) -> None:
    alt0 = float(records[0]["Alt"])
    metrics = [metric for metric in METRICS if metric["id"] in selected_metrics]
    telem = {
        "t": [_round_or_none(record["t_rel"], 3) for record in records],
        "lat": [_round_or_none(record["Lat"], 7) for record in records],
        "lng": [_round_or_none(record["Lng"], 7) for record in records],
        "roll": [_round_or_none(record["Roll"], 2) for record in records],
        "pitch": [_round_or_none(record["Pitch"], 2) for record in records],
        "yaw": [_round_or_none(record["Yaw"], 2) for record in records],
        "series": {
            metric["id"]: [_round_or_none(_series_value(record, metric["id"], alt0), 4) for record in records]
            for metric in metrics
        },
        "metrics": metrics,
    }
    html = CHART_TEMPLATE.replace("__TITLE__", _json_string(title)).replace("__TELEM__", json.dumps(telem))
    html_out.write_text(html, encoding="utf-8")


def _json_string(value: str) -> str:
    return json.dumps(value)[1:-1]


CHART_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root {
  --bg: #070a0f;
  --panel: #0d1320;
  --panel2: #101827;
  --line: #223149;
  --text: #d9e6f2;
  --muted: #7d8da3;
  --accent: #00e5ff;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  min-height: 100vh;
  color: var(--text);
  background: var(--bg);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 18px 22px;
  border-bottom: 1px solid var(--line);
  background: #080c13;
}
h1 { margin: 0; font-size: 18px; letter-spacing: .08em; text-transform: uppercase; }
.mono { color: var(--muted); font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; }
.toolbar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  padding: 14px 22px;
  border-bottom: 1px solid var(--line);
  background: var(--panel);
}
button {
  min-height: 34px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 6px;
  color: var(--text);
  background: #0a101b;
  font-weight: 700;
  cursor: pointer;
}
button.active { color: #001014; background: var(--accent); border-color: var(--accent); }
.chart-shell { padding: 18px 22px; }
canvas {
  display: block;
  width: 100%;
  height: 560px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: linear-gradient(180deg, #09101a 0%, #070a0f 100%);
}
.stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  border-top: 1px solid var(--line);
  background: var(--panel);
}
.stat { padding: 13px 18px; border-right: 1px solid var(--line); }
.stat:last-child { border-right: 0; }
.stat strong { display: block; color: var(--accent); font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 20px; }
.stat span { color: var(--muted); font-size: 11px; font-weight: 800; text-transform: uppercase; }
#tooltip {
  position: fixed;
  min-width: 240px;
  pointer-events: none;
  opacity: 0;
  padding: 12px;
  border: 1px solid var(--accent);
  border-radius: 6px;
  color: var(--text);
  background: rgba(7,10,15,.96);
  box-shadow: 0 0 24px rgba(0,229,255,.14);
  font-size: 12px;
  z-index: 10;
}
#tooltip.visible { opacity: 1; }
#tooltip .title { color: var(--accent); font-weight: 800; margin-bottom: 6px; }
#tooltip div { display: flex; justify-content: space-between; gap: 18px; line-height: 1.7; }
#tooltip span:first-child { color: var(--muted); }
@media (max-width: 760px) {
  header { align-items: flex-start; flex-direction: column; }
  .stats { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  canvas { height: 420px; }
}
</style>
</head>
<body>
<header>
  <h1>__TITLE__</h1>
  <span class="mono" id="activeLabel"></span>
</header>
<div class="toolbar" id="toolbar"></div>
<div class="chart-shell"><canvas id="chart"></canvas></div>
<div class="stats">
  <div class="stat"><strong id="duration">--</strong><span>Duration</span></div>
  <div class="stat"><strong id="samples">--</strong><span>Samples</span></div>
  <div class="stat"><strong id="minVal">--</strong><span>Min</span></div>
  <div class="stat"><strong id="maxVal">--</strong><span>Max</span></div>
</div>
<div id="tooltip"></div>
<script>
const TELEM = __TELEM__;
const canvas = document.getElementById("chart");
const ctx = canvas.getContext("2d");
const toolbar = document.getElementById("toolbar");
const tooltip = document.getElementById("tooltip");
let activeMetric = TELEM.metrics[0]?.id;
let nearest = -1;
const PAD = {top: 32, right: 28, bottom: 54, left: 74};

function clean(values) { return values.filter((value) => value !== null && value !== undefined && !Number.isNaN(Number(value))); }
function fmt(value, digits = 2) { return value === null || value === undefined || Number.isNaN(Number(value)) ? "--" : Number(value).toFixed(digits); }
function dpr() { return window.devicePixelRatio || 1; }
function plotW() { return canvas.width / dpr() - PAD.left - PAD.right; }
function plotH() { return canvas.height / dpr() - PAD.top - PAD.bottom; }
function px(value, min, max) { return PAD.left + ((value - min) / (max - min || 1)) * plotW(); }
function py(value, min, max) { return PAD.top + (1 - (value - min) / (max - min || 1)) * plotH(); }

function initToolbar() {
  toolbar.replaceChildren();
  TELEM.metrics.forEach((metric, index) => {
    const button = document.createElement("button");
    button.textContent = metric.label;
    button.className = index === 0 ? "active" : "";
    button.addEventListener("click", () => {
      activeMetric = metric.id;
      nearest = -1;
      document.querySelectorAll("button").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
      draw();
    });
    toolbar.appendChild(button);
  });
}

function resize() {
  const rect = canvas.getBoundingClientRect();
  const scale = dpr();
  canvas.width = Math.floor(rect.width * scale);
  canvas.height = Math.floor(rect.height * scale);
  ctx.setTransform(scale, 0, 0, scale, 0, 0);
  draw();
}

function draw() {
  const metric = TELEM.metrics.find((item) => item.id === activeMetric);
  if (!metric) return;
  const xs = TELEM.t;
  const ys = TELEM.series[metric.id];
  const valid = clean(ys);
  const width = canvas.width / dpr();
  const height = canvas.height / dpr();
  const xMin = xs[0];
  const xMax = xs[xs.length - 1];
  let yMin = Math.min(...valid);
  let yMax = Math.max(...valid);
  const pad = (yMax - yMin) * 0.12 || 1;
  yMin -= pad;
  yMax += pad;
  ctx.clearRect(0, 0, width, height);

  ctx.strokeStyle = "#223149";
  ctx.lineWidth = 1;
  for (let i = 0; i <= 8; i++) {
    const x = PAD.left + (i / 8) * plotW();
    ctx.beginPath(); ctx.moveTo(x, PAD.top); ctx.lineTo(x, PAD.top + plotH()); ctx.stroke();
  }
  for (let i = 0; i <= 6; i++) {
    const y = PAD.top + (i / 6) * plotH();
    ctx.beginPath(); ctx.moveTo(PAD.left, y); ctx.lineTo(PAD.left + plotW(), y); ctx.stroke();
  }

  ctx.beginPath();
  let started = false;
  ys.forEach((value, i) => {
    if (value === null || value === undefined) return;
    const x = px(xs[i], xMin, xMax);
    const y = py(value, yMin, yMax);
    if (!started) { ctx.moveTo(x, y); started = true; } else { ctx.lineTo(x, y); }
  });
  ctx.strokeStyle = metric.color;
  ctx.lineWidth = 2.4;
  ctx.stroke();

  ctx.fillStyle = "#7d8da3";
  ctx.font = "12px ui-monospace, monospace";
  ctx.textAlign = "center";
  for (let i = 0; i <= 8; i++) {
    const value = xMin + (i / 8) * (xMax - xMin);
    ctx.fillText(`${value.toFixed(0)}s`, PAD.left + (i / 8) * plotW(), PAD.top + plotH() + 20);
  }
  ctx.textAlign = "right";
  for (let i = 0; i <= 6; i++) {
    const value = yMax - (i / 6) * (yMax - yMin);
    ctx.fillText(value.toFixed(1), PAD.left - 10, PAD.top + (i / 6) * plotH() + 4);
  }

  if (nearest >= 0 && ys[nearest] !== null && ys[nearest] !== undefined) {
    const x = px(xs[nearest], xMin, xMax);
    const y = py(ys[nearest], yMin, yMax);
    ctx.strokeStyle = "rgba(255,255,255,.2)";
    ctx.setLineDash([4, 5]);
    ctx.beginPath(); ctx.moveTo(x, PAD.top); ctx.lineTo(x, PAD.top + plotH()); ctx.stroke();
    ctx.setLineDash([]);
    ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI * 2); ctx.fillStyle = metric.color; ctx.fill();
  }

  document.getElementById("activeLabel").textContent = `${metric.label} (${metric.unit})`;
  document.getElementById("duration").textContent = `${(xMax - xMin).toFixed(1)}s`;
  document.getElementById("samples").textContent = xs.length;
  document.getElementById("minVal").textContent = `${Math.min(...valid).toFixed(2)} ${metric.unit}`;
  document.getElementById("maxVal").textContent = `${Math.max(...valid).toFixed(2)} ${metric.unit}`;
}

canvas.addEventListener("mousemove", (event) => {
  const rect = canvas.getBoundingClientRect();
  const mx = event.clientX - rect.left;
  const my = event.clientY - rect.top;
  if (mx < PAD.left || mx > PAD.left + plotW() || my < PAD.top || my > PAD.top + plotH()) {
    tooltip.classList.remove("visible");
    nearest = -1;
    draw();
    return;
  }
  const xs = TELEM.t;
  const t = ((mx - PAD.left) / plotW()) * (xs[xs.length - 1] - xs[0]) + xs[0];
  nearest = xs.reduce((best, value, index) => Math.abs(value - t) < Math.abs(xs[best] - t) ? index : best, 0);
  draw();
  const metric = TELEM.metrics.find((item) => item.id === activeMetric);
  const value = TELEM.series[metric.id][nearest];
  tooltip.innerHTML = `
    <div class="title">Sample ${nearest}</div>
    <div><span>Time</span><strong>${fmt(TELEM.t[nearest], 2)} s</strong></div>
    <div><span>${metric.label}</span><strong>${fmt(value, 3)} ${metric.unit}</strong></div>
    <div><span>Roll</span><strong>${fmt(TELEM.roll[nearest], 2)} deg</strong></div>
    <div><span>Pitch</span><strong>${fmt(TELEM.pitch[nearest], 2)} deg</strong></div>
    <div><span>Yaw</span><strong>${fmt(TELEM.yaw[nearest], 2)} deg</strong></div>
    <div><span>Lat/Lng</span><strong>${fmt(TELEM.lat[nearest], 6)}, ${fmt(TELEM.lng[nearest], 6)}</strong></div>
  `;
  tooltip.classList.add("visible");
  let left = event.clientX + 18;
  let top = event.clientY - 10;
  if (left + 280 > window.innerWidth) left = event.clientX - 280;
  if (top + 210 > window.innerHeight) top = event.clientY - 210;
  tooltip.style.left = `${left}px`;
  tooltip.style.top = `${top}px`;
});
canvas.addEventListener("mouseleave", () => { tooltip.classList.remove("visible"); nearest = -1; draw(); });
window.addEventListener("resize", resize);
initToolbar();
resize();
</script>
</body>
</html>
"""
