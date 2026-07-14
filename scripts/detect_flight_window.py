"""
Detect flight start/end times from an ArduPilot DataFlash BIN log.

The printed times are seconds from the beginning of the log, matching the
START_TIME_SECONDS and END_TIME_SECONDS constants used by flight_3d_replay.py.
"""

from __future__ import annotations

import argparse
import math
from bisect import bisect_left
from dataclasses import dataclass
from pathlib import Path
from statistics import median
from typing import Any

from pymavlink import mavutil


LOG_FILE_PATH = Path(__file__).with_name("00000001.BIN")

# Tuned for this fixed-wing style log: parked/handled speed is near zero, real
# flight quickly reaches sustained speed and climbs well above ground noise.
FLIGHT_SPEED_MPS = 8.0
FLIGHT_ALTITUDE_M = 8.0
SUSTAINED_FLIGHT_SECONDS = 8.0

GROUND_SPEED_MPS = 2.0
GROUND_ALTITUDE_M = 1.5
START_PADDING_SECONDS = 1.5

LANDING_SPEED_MPS = 2.0
LANDING_ALTITUDE_M = 1.5
SUSTAINED_LANDED_SECONDS = 6.0


Record = dict[str, Any]


@dataclass(frozen=True)
class FlightWindow:
    start_time_s: float
    end_time_s: float
    launch_time_s: float
    landing_time_s: float


def _nearest_record(records: list[Record], times: list[float], t: float, tolerance_s: float) -> Record | None:
    if not records:
        return None

    index = bisect_left(times, t)
    best: tuple[float, Record] | None = None
    for candidate_index in (index - 1, index):
        if 0 <= candidate_index < len(records):
            record = records[candidate_index]
            delta = abs(float(record["t"]) - t)
            if delta <= tolerance_s and (best is None or delta < best[0]):
                best = (delta, record)

    return best[1] if best else None


def _window_end_index(records: list[Record], start_index: int, seconds: float) -> int:
    start_time = float(records[start_index]["t_rel"])
    end_time = start_time + seconds
    index = start_index
    while index < len(records) and float(records[index]["t_rel"]) <= end_time:
        index += 1
    return index


def _has_sustained_flight(records: list[Record], start_index: int) -> bool:
    end_index = _window_end_index(records, start_index, SUSTAINED_FLIGHT_SECONDS)
    window = records[start_index:end_index]
    if len(window) < 5:
        return False

    speeds = [float(record["speed_mps"]) for record in window]
    altitudes = [float(record["alt_m"]) for record in window]
    return median(speeds) >= FLIGHT_SPEED_MPS and max(altitudes) >= FLIGHT_ALTITUDE_M


def _has_sustained_landing(records: list[Record], start_index: int) -> bool:
    end_index = _window_end_index(records, start_index, SUSTAINED_LANDED_SECONDS)
    window = records[start_index:end_index]
    if len(window) < 5:
        return False

    speeds = [float(record["speed_mps"]) for record in window]
    altitudes = [float(record["alt_m"]) for record in window]
    return max(speeds) <= LANDING_SPEED_MPS and min(abs(altitude) for altitude in altitudes) <= LANDING_ALTITUDE_M


def extract_records(log_path: Path) -> list[Record]:
    mavlog = mavutil.mavlink_connection(str(log_path))
    pos_records: list[Record] = []
    gps_records: list[Record] = []
    xkf1_records: list[Record] = []

    while True:
        msg = mavlog.recv_match()
        if msg is None:
            break
        if not hasattr(msg, "TimeUS"):
            continue

        msg_type = msg.get_type()
        t = float(msg.TimeUS) / 1e6
        if msg_type == "POS":
            pos_records.append({"t": t, "alt_m": float(getattr(msg, "RelHomeAlt", 0.0))})
        elif msg_type == "GPS":
            gps_records.append({"t": t, "speed_mps": float(msg.Spd)})
        elif msg_type == "XKF1":
            xkf1_records.append({"t": t, "speed_mps": math.hypot(float(msg.VN), float(msg.VE))})

    if not pos_records:
        raise RuntimeError("No POS records found in log.")

    pos_records.sort(key=lambda record: record["t"])
    gps_records.sort(key=lambda record: record["t"])
    xkf1_records.sort(key=lambda record: record["t"])
    gps_times = [float(record["t"]) for record in gps_records]
    xkf1_times = [float(record["t"]) for record in xkf1_records]

    t0 = float(pos_records[0]["t"])
    records: list[Record] = []
    for pos in pos_records:
        t = float(pos["t"])
        gps = _nearest_record(gps_records, gps_times, t, 0.5)
        xkf1 = _nearest_record(xkf1_records, xkf1_times, t, 0.5)

        if gps is not None:
            speed_mps = float(gps["speed_mps"])
        elif xkf1 is not None:
            speed_mps = float(xkf1["speed_mps"])
        else:
            speed_mps = 0.0

        records.append(
            {
                "t_rel": t - t0,
                "alt_m": float(pos["alt_m"]),
                "speed_mps": speed_mps,
            }
        )

    return records


def detect_flight_window(records: list[Record]) -> FlightWindow:
    flight_index = next((i for i in range(len(records)) if _has_sustained_flight(records, i)), None)
    if flight_index is None:
        raise RuntimeError("Could not find a sustained flight segment.")

    airborne_index = next(
        (
            i
            for i in range(flight_index, len(records))
            if float(records[i]["speed_mps"]) >= FLIGHT_SPEED_MPS
            and abs(float(records[i]["alt_m"])) >= GROUND_ALTITUDE_M
        ),
        None,
    )
    if airborne_index is None:
        raise RuntimeError("Could not find the first high-speed airborne sample.")

    launch_index = airborne_index
    airborne_time_s = float(records[airborne_index]["t_rel"])
    for i in range(airborne_index, -1, -1):
        record = records[i]
        if airborne_time_s - float(record["t_rel"]) > 30.0:
            break
        if float(record["speed_mps"]) <= GROUND_SPEED_MPS and abs(float(record["alt_m"])) <= GROUND_ALTITUDE_M:
            launch_index = i
            break

    launch_time_s = float(records[launch_index]["t_rel"])
    start_time_s = max(0.0, launch_time_s - START_PADDING_SECONDS)

    landing_search_start = next(
        i for i in range(airborne_index, len(records)) if float(records[i]["t_rel"]) >= airborne_time_s + 30.0
    )
    landing_index = None
    for i in range(landing_search_start, len(records)):
        record = records[i]
        if (
            float(record["speed_mps"]) <= LANDING_SPEED_MPS
            and abs(float(record["alt_m"])) <= LANDING_ALTITUDE_M
            and _has_sustained_landing(records, i)
        ):
            landing_index = i
            break

    if landing_index is None:
        raise RuntimeError("Could not find a sustained landing segment.")

    return FlightWindow(
        start_time_s=start_time_s,
        end_time_s=float(records[landing_index]["t_rel"]),
        launch_time_s=launch_time_s,
        landing_time_s=float(records[landing_index]["t_rel"]),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect START_TIME_SECONDS and END_TIME_SECONDS for a BIN log.")
    parser.add_argument("log", nargs="?", type=Path, default=LOG_FILE_PATH, help="Path to ArduPilot .BIN log")
    parser.add_argument("--quiet", action="store_true", help="Print only: <start_seconds> <end_seconds>")
    parser.add_argument("--decimals", type=int, default=0, help="Number of decimal places to print")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    log_path = args.log.expanduser().resolve()
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    records = extract_records(log_path)
    window = detect_flight_window(records)
    start = round(window.start_time_s, args.decimals)
    end = round(window.end_time_s, args.decimals)

    if args.quiet:
        print(f"{start:.{args.decimals}f} {end:.{args.decimals}f}")
        return

    print(f"Log: {log_path}")
    print("Use these values in flight_3d_replay.py:")
    print(f"START_TIME_SECONDS = {start:.{args.decimals}f}")
    print(f"END_TIME_SECONDS = {end:.{args.decimals}f}")
    print()
    print(f"Detected low-speed launch sample: {window.launch_time_s:.2f}s")
    print(f"Detected low-speed landing sample: {window.landing_time_s:.2f}s")


if __name__ == "__main__":
    main()
