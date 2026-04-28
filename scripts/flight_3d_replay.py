"""
ArduPilot BIN log to interactive 3D flight replay.

This script extracts position, attitude, and speed telemetry from an ArduPilot
DataFlash log (.BIN) and generates an animated 3D HTML replay.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from pymavlink import mavutil

# =============================================================================
# USER CONSTANTS
# =============================================================================
LOG_FILE_PATH = "00000007.BIN"
OUTPUT_HTML_PATH = "flight_3d_replay.html"
ANIMATION_DOWNSAMPLE_STEP = 8

# Optional time window in seconds from log start.
# Set to None to disable the boundary.
START_TIME_SECONDS = 1265       # set None for the full file parse
END_TIME_SECONDS = 1485         # set None for the full time parse


def _msg_to_record(msg, fields: List[str]) -> Dict[str, float]:
    rec = {}
    for field in fields:
        if hasattr(msg, field):
            rec[field] = getattr(msg, field)
    return rec


def extract_flight_data(log_path: Path) -> pd.DataFrame:
    """Extract and align POS, ATT, GPS, and XKF1 data into one timeline."""
    mavlog = mavutil.mavlink_connection(str(log_path))

    pos_records, att_records, gps_records, xkf1_records = [], [], [], []

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

    if not pos_records or not att_records:
        raise RuntimeError("Required POS/ATT data not found in log.")

    pos_df = pd.DataFrame(pos_records).sort_values("t")
    att_df = pd.DataFrame(att_records).sort_values("t")
    gps_df = pd.DataFrame(gps_records).sort_values("t") if gps_records else pd.DataFrame(columns=["t"])
    xkf1_df = pd.DataFrame(xkf1_records).sort_values("t") if xkf1_records else pd.DataFrame(columns=["t"])

    # POS is our base timeline because it has continuous global coordinates.
    base = pos_df[["t", "Lat", "Lng", "Alt", "RelHomeAlt"]].copy()

    # Attach nearest attitude/speed samples by time.
    merged = pd.merge_asof(base.sort_values("t"), att_df, on="t", direction="nearest", tolerance=0.2)
    if not gps_df.empty:
        merged = pd.merge_asof(merged.sort_values("t"), gps_df[["t", "Spd"]], on="t", direction="nearest", tolerance=0.5)
    if not xkf1_df.empty:
        merged = pd.merge_asof(
            merged.sort_values("t"),
            xkf1_df[["t", "VN", "VE", "VD"]],
            on="t",
            direction="nearest",
            tolerance=0.5,
        )

    merged = merged.dropna(subset=["Roll", "Pitch", "Yaw"]).reset_index(drop=True)

    # Derive speed from XKF1 if GPS speed missing.
    if "Spd" not in merged.columns:
        merged["Spd"] = np.nan
    if {"VN", "VE"}.issubset(merged.columns):
        ekf_speed = np.sqrt(np.square(merged["VN"]) + np.square(merged["VE"]))
        merged["speed_mps"] = merged["Spd"].fillna(ekf_speed)
    else:
        merged["speed_mps"] = merged["Spd"]
    merged["speed_mps"] = merged["speed_mps"].fillna(0.0)

    return merged


def lla_to_local_ned(df: pd.DataFrame) -> pd.DataFrame:
    """Convert lat/lng/alt to local metric frame around first position."""
    lat0 = float(df["Lat"].iloc[0])
    lng0 = float(df["Lng"].iloc[0])
    alt0 = float(df["Alt"].iloc[0])

    meters_per_deg_lat = 111_320.0
    meters_per_deg_lng = 111_320.0 * math.cos(math.radians(lat0))

    out = df.copy()
    out["x_east_m"] = (out["Lng"] - lng0) * meters_per_deg_lng
    out["y_north_m"] = (out["Lat"] - lat0) * meters_per_deg_lat
    out["z_up_m"] = out["Alt"] - alt0
    out["t_rel"] = out["t"] - out["t"].iloc[0]
    return out


def downsample_for_animation(df: pd.DataFrame, step: int) -> pd.DataFrame:
    if step <= 1:
        return df
    return df.iloc[::step].reset_index(drop=True)


def filter_by_time_window(
    df: pd.DataFrame,
    start_time_s: float | None,
    end_time_s: float | None,
) -> pd.DataFrame:
    """Filter rows using optional relative time bounds (seconds from log start)."""
    out = df
    if start_time_s is not None:
        out = out[out["t_rel"] >= float(start_time_s)]
    if end_time_s is not None:
        out = out[out["t_rel"] <= float(end_time_s)]
    return out.reset_index(drop=True)


def build_3d_replay(df: pd.DataFrame, html_out: Path, title: str) -> None:
    x = df["x_east_m"].to_numpy()
    y = df["y_north_m"].to_numpy()
    z = df["z_up_m"].to_numpy()
    t = df["t_rel"].to_numpy()
    spd = df["speed_mps"].to_numpy()
    roll = df["Roll"].to_numpy()
    pitch = df["Pitch"].to_numpy()
    yaw = df["Yaw"].to_numpy()

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
    for i in range(len(df)):
        info = (
            f"t={t[i]:.1f}s<br>"
            f"speed={spd[i]:.1f} m/s ({spd[i]*3.6:.1f} km/h)<br>"
            f"alt={z[i]:.1f} m rel<br>"
            f"roll={roll[i]:.1f} deg<br>"
            f"pitch={pitch[i]:.1f} deg<br>"
            f"yaw={yaw[i]:.1f} deg"
        )
        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=x[: i + 1],
                        y=y[: i + 1],
                        z=z[: i + 1],
                        mode="lines",
                        line=dict(width=5, color=np.linspace(0, 1, i + 1), colorscale="Viridis"),
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
                        args=[None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
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
                    dict(method="animate", args=[[str(i)], {"mode": "immediate", "frame": {"duration": 0, "redraw": True}}], label=str(i))
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
    if filtered.empty:
        raise RuntimeError("No samples in selected time range. Adjust START_TIME_SECONDS/END_TIME_SECONDS.")

    local_ds = downsample_for_animation(filtered, max(1, int(ANIMATION_DOWNSAMPLE_STEP)))

    print(f"Samples total: {len(local)} | selected: {len(filtered)} | animated frames: {len(local_ds)}")
    build_3d_replay(local_ds, out_path, title=f"3D Flight Replay: {log_path.name}")
    print(f"Replay saved to: {out_path}")


if __name__ == "__main__":
    main()
