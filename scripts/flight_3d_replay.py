"""
ArduPilot BIN log to interactive 3D flight replay.

This script extracts position, attitude, and speed telemetry from an ArduPilot
DataFlash log (.BIN) and generates an animated 3D HTML replay.
"""

from __future__ import annotations

import math
from bisect import bisect_left
from pathlib import Path
from statistics import median
from typing import Any

import plotly.graph_objects as go
from pymavlink import mavutil

# =============================================================================
# USER CONSTANTS
# =============================================================================
LOG_FILE_PATH = "00000001.BIN"
OUTPUT_HTML_PATH = "flight_3d_replay.html"
ANIMATION_DOWNSAMPLE_STEP = 5

# Optional time window in seconds from log start.
# Set to None to disable the boundary.
START_TIME_SECONDS = 448  # set None for the full file parse
END_TIME_SECONDS = 1530  # set None for the full time parse


Record = dict[str, Any]


def _msg_to_record(msg, fields: list[str]) -> Record:
    rec: Record = {}
    for field in fields:
        if hasattr(msg, field):
            rec[field] = getattr(msg, field)
    return rec


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
    """Extract and align POS, ATT, GPS, and XKF1 data into one timeline."""
    mavlog = mavutil.mavlink_connection(str(log_path))

    pos_records, att_records, gps_records, xkf1_records, arsp_records = [], [], [], [], []

    while True:
        msg = mavlog.recv_match()
        if msg is None:
            break
        msg_type = msg.get_type()

        if not hasattr(msg, "TimeUS"):
            continue

        t = msg.TimeUS / 1e6

        if msg_type == "POS":
            record = _msg_to_record(msg, ["Lat", "Lng", "Alt", "RelHomeAlt", "RelOriginAlt"])
            record["t"] = t
            pos_records.append(record)
        elif msg_type == "ATT":
            record = _msg_to_record(msg, ["Roll", "Pitch", "Yaw"])
            record["t"] = t
            att_records.append(record)
        elif msg_type == "GPS":
            record = _msg_to_record(msg, ["Spd", "Status", "NSats"])
            record["t"] = t
            gps_records.append(record)
        elif msg_type == "XKF1":
            record = _msg_to_record(msg, ["VN", "VE", "VD"])
            record["t"] = t
            xkf1_records.append(record)
        elif msg_type == "ARSP":
            record = _msg_to_record(msg, ["Airspeed", "H"])
            record["t"] = t
            arsp_records.append(record)

    if not pos_records or not att_records:
        raise RuntimeError("Required POS/ATT data not found in log.")

    pos_records.sort(key=lambda record: record["t"])
    att_records.sort(key=lambda record: record["t"])
    gps_records.sort(key=lambda record: record["t"])
    xkf1_records.sort(key=lambda record: record["t"])
    arsp_records.sort(key=lambda record: record["t"])

    merged: list[Record] = []
    for pos in pos_records:
        t = float(pos["t"])
        att = _nearest_record(att_records, t, 0.2)
        if att is None:
            continue

        gps = _nearest_record(gps_records, t, 0.5)
        xkf1 = _nearest_record(xkf1_records, t, 0.5)
        arsp = _nearest_record(arsp_records, t, 0.5)

        ground_speed_mps = 0.0
        if _has_value(gps, "Spd"):
            ground_speed_mps = float(gps["Spd"])
        elif _has_value(xkf1, "VN") and _has_value(xkf1, "VE"):
            ground_speed_mps = math.hypot(float(xkf1["VN"]), float(xkf1["VE"]))

        healthy_airspeed_mps = None
        if _has_value(arsp, "Airspeed") and _has_value(arsp, "H") and int(arsp["H"]) == 1:
            healthy_airspeed_mps = float(arsp["Airspeed"])

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
                "ground_speed_mps": ground_speed_mps,
                "healthy_airspeed_mps": healthy_airspeed_mps,
                "speed_mps": healthy_airspeed_mps if healthy_airspeed_mps is not None else ground_speed_mps,
            }
        )

    return merged


def lla_to_local_ned(records: list[Record]) -> list[Record]:
    """Convert lat/lng/alt to local metric frame around first position."""
    lat0 = float(records[0]["Lat"])
    lng0 = float(records[0]["Lng"])
    alt0 = float(records[0]["Alt"])
    t0 = float(records[0]["t"])

    meters_per_deg_lat = 111_320.0
    meters_per_deg_lng = 111_320.0 * math.cos(math.radians(lat0))

    out = []
    for record in records:
        next_record = record.copy()
        next_record["x_east_m"] = (float(record["Lng"]) - lng0) * meters_per_deg_lng
        next_record["y_north_m"] = (float(record["Lat"]) - lat0) * meters_per_deg_lat
        next_record["z_up_m"] = float(record["Alt"]) - alt0
        next_record["t_rel"] = float(record["t"]) - t0
        out.append(next_record)
    return out


def downsample_for_animation(records: list[Record], step: int) -> list[Record]:
    if step <= 1:
        return records
    return records[::step]


def add_kinematics(records: list[Record]) -> list[Record]:
    """Add per-sample timing and acceleration derived from speed."""
    out: list[Record] = []
    previous: Record | None = None
    for record in records:
        next_record = record.copy()
        if previous is None:
            next_record["dt_s"] = 0.0
            next_record["accel_mps2"] = 0.0
        else:
            dt = float(record["t_rel"]) - float(previous["t_rel"])
            dv = float(record["speed_mps"]) - float(previous["speed_mps"])
            next_record["dt_s"] = max(0.0, dt)
            next_record["accel_mps2"] = dv / dt if dt > 0 else 0.0
        out.append(next_record)
        previous = record
    return out


def filter_by_time_window(
    records: list[Record],
    start_time_s: float | None,
    end_time_s: float | None,
) -> list[Record]:
    """Filter rows using optional relative time bounds (seconds from log start)."""
    out = records
    if start_time_s is not None:
        out = [record for record in out if float(record["t_rel"]) >= float(start_time_s)]
    if end_time_s is not None:
        out = [record for record in out if float(record["t_rel"]) <= float(end_time_s)]
    return out


def build_3d_replay(records: list[Record], html_out: Path, title: str) -> None:
    x = [float(record["x_east_m"]) for record in records]
    y = [float(record["y_north_m"]) for record in records]
    z = [float(record["z_up_m"]) for record in records]
    t = [float(record["t_rel"]) for record in records]
    spd = [float(record["speed_mps"]) for record in records]
    gspd = [float(record["ground_speed_mps"]) for record in records]
    aspd = [record["healthy_airspeed_mps"] for record in records]
    accel = [float(record["accel_mps2"]) for record in records]
    roll = [float(record["Roll"]) for record in records]
    pitch = [float(record["Pitch"]) for record in records]
    yaw = [float(record["Yaw"]) for record in records]
    dt = [float(record["dt_s"]) for record in records]
    positive_dt = [value for value in dt if value > 0]
    frame_duration_ms = max(20, int(median(positive_dt) * 1000)) if positive_dt else 50

    path_trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode="lines",
        line=dict(width=4, color="lightgray"),
        name="Flight path",
    )

    marker_trace = go.Scatter3d(
        x=[x[0]],
        y=[y[0]],
        z=[z[0]],
        mode="markers+text",
        marker=dict(size=7, color="red"),
        text=["Aircraft"],
        textposition="top center",
        name="Aircraft",
    )

    frames = []
    for i in range(len(records)):
        airspeed_text = f"{aspd[i]:.3f} m/s" if aspd[i] is not None else "n/a"
        info = (
            f"t={t[i]:.3f}s<br>"
            f"dt={dt[i]:.3f}s<br>"
            f"display speed={spd[i]:.3f} m/s ({spd[i]*3.6:.3f} km/h)<br>"
            f"ground speed={gspd[i]:.3f} m/s<br>"
            f"healthy airspeed={airspeed_text}<br>"
            f"accel={accel[i]:.3f} m/s^2<br>"
            f"alt={z[i]:.3f} m rel<br>"
            f"roll={roll[i]:.3f} deg<br>"
            f"pitch={pitch[i]:.3f} deg<br>"
            f"yaw={yaw[i]:.3f} deg"
        )
        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=x[: i + 1],
                        y=y[: i + 1],
                        z=z[: i + 1],
                        mode="lines",
                        line=dict(
                            width=5,
                            color=[j / max(1, i) for j in range(i + 1)],
                            colorscale="Viridis",
                        ),
                        name="Trail",
                    ),
                    go.Scatter3d(
                        x=[x[i]],
                        y=[y[i]],
                        z=[z[i]],
                        mode="markers+text",
                        marker=dict(size=8, color="red"),
                        text=[info],
                        textposition="top center",
                        name="Aircraft",
                    ),
                ],
                name=str(i),
            )
        )

    fig = go.Figure(data=[path_trace, marker_trace], frames=frames)
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title="East (m)",
            yaxis_title="North (m)",
            zaxis_title="Up (m)",
            aspectmode="data",
        ),
        legend=dict(x=0.01, y=0.99),
        updatemenus=[
            dict(
                type="buttons",
                showactive=True,
                x=0.02,
                y=0.02,
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[None, {"frame": {"duration": frame_duration_ms, "redraw": True}, "fromcurrent": True}],
                    ),
                    dict(
                        label="Pause",
                        method="animate",
                        args=[[None], {"mode": "immediate", "frame": {"duration": 0, "redraw": False}}],
                    ),
                ],
            )
        ],
        sliders=[
            dict(
                currentvalue={"prefix": "Frame: "},
                steps=[
                    dict(
                        method="animate",
                        args=[[str(i)], {"mode": "immediate", "frame": {"duration": 0, "redraw": True}}],
                        label=f"{t[i]:.2f}s",
                    )
                    for i in range(len(frames))
                ],
            )
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )

    fig.write_html(str(html_out), auto_open=False)


def main() -> None:
    log_path = Path(LOG_FILE_PATH)
    out_path = Path(OUTPUT_HTML_PATH)

    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    print(f"Reading log: {log_path}")
    data = extract_flight_data(log_path)
    local = lla_to_local_ned(data)

    if START_TIME_SECONDS is not None and END_TIME_SECONDS is not None:
        if float(START_TIME_SECONDS) > float(END_TIME_SECONDS):
            raise ValueError("START_TIME_SECONDS must be <= END_TIME_SECONDS")

    filtered = filter_by_time_window(local, START_TIME_SECONDS, END_TIME_SECONDS)
    if not filtered:
        raise RuntimeError("No samples in selected time range. Adjust START_TIME_SECONDS/END_TIME_SECONDS.")

    local_kin = add_kinematics(filtered)
    local_ds = downsample_for_animation(local_kin, max(1, int(ANIMATION_DOWNSAMPLE_STEP)))

    print(f"Samples total: {len(local)} | selected: {len(filtered)} | animated frames: {len(local_ds)}")
    build_3d_replay(local_ds, out_path, title=f"3D Flight Replay: {log_path.name}")
    print(f"Replay saved to: {out_path}")


if __name__ == "__main__":
    main()
