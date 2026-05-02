"""
ArduPilot Flight Log Analyzer — LLM-powered parameter tuning advisor.

Workflow:
    1. Parses an ArduPilot DataFlash .BIN log and extracts full telemetry
       (position, attitude, speed, RC inputs) into a CSV file.
    2. Optionally loads the user's current .param file and an ArduPilot
       parameter knowledge-base JSON.
    3. Sends everything to an OpenAI LLM with a structured analysis prompt.
    4. Prints the analysis, saves a Markdown report, and writes a CSV of
       all recommended parameter changes.

Usage:
    Edit the constants in the USER CONFIGURATION section, then run:
        python ardupilot_analyzer.py
"""

from __future__ import annotations

import csv
import json
import sys
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
from openai import OpenAI
from pymavlink import mavutil


# =============================================================================
# USER CONFIGURATION
# =============================================================================

OPENAI_API_KEY = "sk-..."
OPENAI_MODEL = "gpt-5.4-mini"  # gpt-5.5,  gpt-5.4,  gpt-5.4-mini

LOG_FILE_PATH = "00000006.BIN"
PARAM_FILE_PATH = "ad5_20260423.param"  # set to None to skip
KB_FILE_PATH = "ardupilot_kb.json"      # set to None to skip

CSV_OUTPUT_PATH = "flight_telemetry.csv"
REPORT_OUTPUT_PATH = "suggestion_report.md"

# Time window in seconds from log start. Set either to None for no boundary.
START_TIME_SECONDS: Optional[float] = None
END_TIME_SECONDS: Optional[float] = None

# Keep every Nth row in the CSV. 1 = no downsampling.
DOWNSAMPLE_STEP = 4

# Optional drone context — helps the LLM give more specific advice.
DRONE_MODEL = ""        # e.g. "Volantex Ranger EX 757-3"
DRONE_DESCRIPTION = ""  # e.g. "Fixed-wing, 1800 mm wingspan, ~2.1 kg AUW, ArduPlane 4.5"


# =============================================================================
# TELEMETRY EXTRACTION
# =============================================================================

def msg_to_record(msg, fields: list[str]) -> dict:
    return {f: getattr(msg, f) for f in fields if hasattr(msg, f)}


def extract_flight_data(log_path: Path) -> pd.DataFrame:
    """Parse a .BIN log and merge POS / ATT / GPS / XKF1 / RCIN into one DataFrame."""
    print(f"[1/4] Parsing log: {log_path}")
    mavlog = mavutil.mavlink_connection(str(log_path))

    pos_records = []
    att_records = []
    gps_records = []
    xkf1_records = []
    rcin_records = []

    while True:
        msg = mavlog.recv_match()
        if msg is None:
            break
        mtype = msg.get_type()
        if not hasattr(msg, "TimeUS"):
            continue
        t = msg.TimeUS / 1e6

        if mtype == "POS":
            rec = msg_to_record(msg, ["Lat", "Lng", "Alt", "RelHomeAlt"])
            rec["t"] = t
            pos_records.append(rec)
        elif mtype == "ATT":
            rec = msg_to_record(msg, ["Roll", "Pitch", "Yaw", "RollRate", "PitchRate", "YawRate"])
            rec["t"] = t
            att_records.append(rec)
        elif mtype == "GPS":
            rec = msg_to_record(msg, ["Spd", "Status", "NSats", "HDop"])
            rec["t"] = t
            gps_records.append(rec)
        elif mtype == "XKF1":
            rec = msg_to_record(msg, ["VN", "VE", "VD", "PN", "PE", "PD"])
            rec["t"] = t
            xkf1_records.append(rec)
        elif mtype == "RCIN":
            # Standard mapping: C1=Roll, C2=Pitch, C3=Throttle, C4=Yaw
            rec = msg_to_record(msg, ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"])
            rec["t"] = t
            rcin_records.append(rec)

    if not pos_records or not att_records:
        raise RuntimeError("Required POS / ATT data not found in log.")

    def to_df(records):
        return pd.DataFrame(records).sort_values("t").reset_index(drop=True)

    pos_df = to_df(pos_records)
    att_df = to_df(att_records)
    gps_df = to_df(gps_records) if gps_records else pd.DataFrame(columns=["t"])
    xkf1_df = to_df(xkf1_records) if xkf1_records else pd.DataFrame(columns=["t"])
    rcin_df = to_df(rcin_records) if rcin_records else pd.DataFrame(columns=["t"])

    merged = pd.merge_asof(
        pos_df[["t", "Lat", "Lng", "Alt", "RelHomeAlt"]].sort_values("t"),
        att_df,
        on="t",
        direction="nearest",
        tolerance=0.2,
    )

    for extra_df, tol in [(gps_df, 0.5), (xkf1_df, 0.5), (rcin_df, 0.5)]:
        if not extra_df.empty:
            merged = pd.merge_asof(
                merged.sort_values("t"),
                extra_df,
                on="t",
                direction="nearest",
                tolerance=tol,
            )

    merged = merged.dropna(subset=["Roll", "Pitch", "Yaw"]).reset_index(drop=True)
    merged["t_rel"] = merged["t"] - merged["t"].iloc[0]

    # Ground speed — prefer GPS Spd, fall back to EKF horizontal velocity.
    if "Spd" not in merged.columns:
        merged["Spd"] = np.nan
    if {"VN", "VE"}.issubset(merged.columns):
        ekf_spd = np.sqrt(np.square(merged["VN"]) + np.square(merged["VE"]))
        merged["speed_mps"] = merged["Spd"].fillna(ekf_spd)
    else:
        merged["speed_mps"] = merged["Spd"].fillna(0.0)

    # Vertical speed — EKF VD is down-positive so we negate it.
    if "VD" in merged.columns:
        merged["vspeed_mps"] = -merged["VD"]
    else:
        merged["vspeed_mps"] = merged["Alt"].diff() / merged["t"].diff()

    # Throttle percentage derived from RC channel 3 PWM range.
    if "C3" in merged.columns and merged["C3"].notna().any():
        c3 = merged["C3"]
        pwm_min, pwm_max = c3.min(), c3.max()
        if pwm_max > pwm_min:
            merged["throttle_pct"] = ((c3 - pwm_min) / (pwm_max - pwm_min) * 100.0).clip(0, 100)
        else:
            merged["throttle_pct"] = 0.0
    else:
        merged["throttle_pct"] = np.nan

    # Stick deflection as +/-100% for roll, pitch, and yaw channels.
    for ch, label in [("C1", "rc_roll_pct"), ("C2", "rc_pitch_pct"), ("C4", "rc_yaw_pct")]:
        if ch in merged.columns and merged[ch].notna().any():
            raw = merged[ch]
            centre = (raw.min() + raw.max()) / 2
            half = (raw.max() - raw.min()) / 2 or 1
            merged[label] = ((raw - centre) / half * 100.0).clip(-100, 100)
        else:
            merged[label] = np.nan

    return merged


def filter_by_time_window(
    df: pd.DataFrame,
    start_s: Optional[float],
    end_s: Optional[float],
) -> pd.DataFrame:
    out = df
    if start_s is not None:
        out = out[out["t_rel"] >= float(start_s)]
    if end_s is not None:
        out = out[out["t_rel"] <= float(end_s)]
    return out.reset_index(drop=True)


def downsample(df: pd.DataFrame, step: int) -> pd.DataFrame:
    return df.iloc[::max(1, step)].reset_index(drop=True)


# =============================================================================
# CSV EXPORT
# =============================================================================

CSV_COLUMNS = [
    "t_rel", "Lat", "Lng", "Alt", "RelHomeAlt",
    "Roll", "Pitch", "Yaw",
    "RollRate", "PitchRate", "YawRate",
    "speed_mps", "vspeed_mps", "throttle_pct",
    "rc_roll_pct", "rc_pitch_pct", "rc_yaw_pct",
    "VN", "VE", "VD",
    "Spd", "NSats", "HDop",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
]


def save_csv(df: pd.DataFrame, csv_path: Path) -> None:
    cols = [c for c in CSV_COLUMNS if c in df.columns]
    df[cols].round(4).to_csv(csv_path, index=False)
    print(f"[2/4] Telemetry CSV saved: {csv_path} ({len(df)} rows, {len(cols)} columns)")


# =============================================================================
# PARAMETER AND KNOWLEDGE-BASE LOADING
# =============================================================================

def load_param_file(path: Path) -> dict[str, str]:
    """Parse a Mission Planner / ArduPilot .param file (name,value pairs)."""
    params = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(",", 1)
            if len(parts) == 2:
                params[parts[0].strip()] = parts[1].strip()
    return params


def load_knowledge_base(path: Path) -> list[dict]:
    """Load the parameter knowledge-base JSON, tolerating BOM and encoding variants."""
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            raw = path.read_text(encoding=encoding).strip()
            if not raw:
                print(f"WARNING: KB file is empty: {path} — skipping.")
                return []
            data = json.loads(raw)
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                for value in data.values():
                    if isinstance(value, list):
                        return value
            print("WARNING: KB file has unexpected structure — skipping.")
            return []
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    print(f"WARNING: Could not parse KB file {path} — skipping.")
    return []


# =============================================================================
# TELEMETRY STATISTICS
# =============================================================================

def compute_stats(df: pd.DataFrame) -> dict:
    """Compute per-channel descriptive statistics to include in the LLM prompt."""
    duration = float(df["t_rel"].iloc[-1] - df["t_rel"].iloc[0])
    stats = {"duration_s": round(duration, 1)}

    channels = [
        "Alt", "RelHomeAlt", "speed_mps", "vspeed_mps", "throttle_pct",
        "Roll", "Pitch", "Yaw", "RollRate", "PitchRate", "YawRate",
        "rc_roll_pct", "rc_pitch_pct", "rc_yaw_pct",
    ]
    for col in channels:
        if col in df.columns and df[col].notna().any():
            s = df[col].dropna()
            stats[col] = {
                "min": round(float(s.min()), 3),
                "max": round(float(s.max()), 3),
                "mean": round(float(s.mean()), 3),
                "std": round(float(s.std()), 3),
                "p5": round(float(s.quantile(0.05)), 3),
                "p95": round(float(s.quantile(0.95)), 3),
            }
    return stats


# =============================================================================
# LLM PROMPT
# =============================================================================

def csv_excerpt(df: pd.DataFrame, n: int = 40) -> str:
    """Return the first and last n rows of the telemetry as CSV text."""
    cols = [c for c in CSV_COLUMNS if c in df.columns]
    combined = pd.concat([df[cols].head(n), df[cols].tail(n)])
    combined = combined.drop_duplicates(subset=["t_rel"])
    return combined.round(3).to_csv(index=False)


def build_prompt(
    stats: dict,
    excerpt: str,
    current_params: Optional[dict[str, str]],
    kb: Optional[list[dict]],
    drone_model: str,
    drone_description: str,
) -> str:
    sections = []

    if drone_model or drone_description:
        sections.append("## Drone Information")
        if drone_model:
            sections.append(f"Model: {drone_model}")
        if drone_description:
            sections.append(f"Description: {drone_description}")

    sections.append("## Flight Statistics")
    sections.append(json.dumps(stats, indent=2))

    sections.append("## Telemetry Sample (CSV excerpt — first and last 40 rows)")
    sections.append(excerpt)

    if current_params:
        sections.append("## Current ArduPilot Parameters")
        sections.append("\n".join(f"{k} = {v}" for k, v in sorted(current_params.items())))

    if kb:
        sections.append("## ArduPilot Parameter Knowledge Base")
        kb_lines = []
        for entry in kb:
            name = entry.get("parameter_name", "")
            desc = entry.get("description", "")
            attrs = entry.get("attributes", {})
            line = f"{name}: {desc}"
            if attrs:
                line += " [" + "; ".join(f"{k}={v}" for k, v in attrs.items()) + "]"
            kb_lines.append(line)
        sections.append("\n".join(kb_lines))

    sections.append(textwrap.dedent("""
        ## Your Task

        You are an expert ArduPilot flight controller tuner. Analyse the flight
        telemetry statistics and sample data above. Consider the drone's current
        parameter values and the parameter knowledge base provided.

        1. **Summarise the flight behaviour** — identify issues such as oscillations,
           unusual attitude angles, excessive throttle variation, poor speed regulation,
           GPS quality problems, or erratic RC inputs.

        2. **Analyse current parameters** — note parameters that appear suboptimal
           given the observed flight behaviour.

        3. **Suggest parameter changes** — for each parameter you recommend changing,
           output a line in exactly this pipe-delimited format:

               PARAM_CHANGE | <PARAMETER_NAME> | <CURRENT_VALUE> | <SUGGESTED_VALUE> | <REASON>

           Use "N/A" for current value if the parameter is absent from the param file.
           Each PARAM_CHANGE line must be on its own line.

        4. After all PARAM_CHANGE lines, add an **Additional Notes** section with any
           safety observations or tuning recommendations that do not map to a single
           parameter.

        Be specific and conservative — only recommend changes you are confident about
        based on the data provided.
    """).strip())

    return "\n\n".join(sections)


# =============================================================================
# LLM CALL
# =============================================================================

def call_llm(prompt: str) -> str:
    print("[3/4] Sending data to LLM...")
    try:
        import httpx
        client = OpenAI(api_key=OPENAI_API_KEY, http_client=httpx.Client())
    except TypeError:
        client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert ArduPilot flight controller engineer "
                    "specialising in fixed-wing and VTOL drone tuning. "
                    "Your analysis is data-driven, safety-focused, and conservative."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content or ""


# =============================================================================
# RESPONSE PARSING AND OUTPUT
# =============================================================================

def parse_response(response: str) -> tuple[list[tuple[str, str, str, str]], str]:
    """Split the LLM response into structured parameter changes and narrative text."""
    changes = []
    narrative_lines = []

    for line in response.splitlines():
        if line.strip().startswith("PARAM_CHANGE"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                changes.append((parts[1], parts[2], parts[3], parts[4]))
        else:
            narrative_lines.append(line)

    return changes, "\n".join(narrative_lines).strip()


def print_report(changes: list[tuple[str, str, str, str]], narrative: str) -> None:
    print("\n" + "=" * 80)
    print("  ARDUPILOT FLIGHT ANALYSIS REPORT")
    print("=" * 80)
    print()
    print(narrative)

    if not changes:
        print("\n[No structured PARAM_CHANGE lines found — see narrative above.]")
        return

    print("\n" + "=" * 80)
    print("  SUGGESTED PARAMETER CHANGES")
    print("=" * 80)

    col_widths = (32, 15, 18, 55)
    sep = "-" * sum(col_widths)
    header = (
        f"{'Parameter':<{col_widths[0]}}"
        f"{'Current':<{col_widths[1]}}"
        f"{'Suggested':<{col_widths[2]}}"
        f"{'Reason'}"
    )
    print(header)
    print(sep)

    for name, current, suggested, reason in changes:
        wrapped = textwrap.wrap(reason, width=col_widths[3])
        first_line = wrapped[0] if wrapped else ""
        print(f"{name:<{col_widths[0]}}{current:<{col_widths[1]}}{suggested:<{col_widths[2]}}{first_line}")
        indent = " " * sum(col_widths[:3])
        for continuation in wrapped[1:]:
            print(f"{indent}{continuation}")

    print(sep)
    print(f"\nTotal suggested changes: {len(changes)}")


def save_changes_csv(changes: list[tuple[str, str, str, str]], output_path: Path) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["Parameter", "Current Value", "Suggested Value", "Reason"])
        writer.writerows(changes)
    print(f"Parameter changes CSV saved: {output_path}")


def save_markdown_report(
    changes: list[tuple[str, str, str, str]],
    narrative: str,
    report_path: Path,
    log_name: str,
    drone_model: str,
) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# ArduPilot Flight Analysis Report",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Log file | `{log_name}` |",
    ]
    if drone_model:
        lines.append(f"| Drone model | {drone_model} |")
    lines += [
        f"| Generated | {now} |",
        "",
        "## Flight Analysis",
        "",
        narrative,
        "",
        "## Suggested Parameter Changes",
        "",
    ]

    if changes:
        lines += [
            "| Parameter | Current Value | Suggested Value | Reason |",
            "|-----------|---------------|-----------------|--------|",
        ]
        for name, current, suggested, reason in changes:
            safe_reason = reason.replace("|", "&#124;")
            lines.append(f"| `{name}` | {current} | **{suggested}** | {safe_reason} |")
        lines += ["", f"*Total suggested changes: {len(changes)}*", ""]
    else:
        lines += ["_No structured parameter changes were identified._", ""]

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Markdown report saved: {report_path}")


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    log_path = Path(LOG_FILE_PATH)
    if not log_path.exists():
        sys.exit(f"ERROR: Log file not found: {log_path}")

    if START_TIME_SECONDS is not None and END_TIME_SECONDS is not None:
        if float(START_TIME_SECONDS) > float(END_TIME_SECONDS):
            sys.exit("ERROR: START_TIME_SECONDS must be less than or equal to END_TIME_SECONDS.")

    raw = extract_flight_data(log_path)
    filtered = filter_by_time_window(raw, START_TIME_SECONDS, END_TIME_SECONDS)

    if filtered.empty:
        sys.exit("ERROR: No samples in the selected time range. Adjust START/END time constants.")

    ds = downsample(filtered, DOWNSAMPLE_STEP)
    print(f"       Samples: total={len(raw)} | selected={len(filtered)} | saved to CSV={len(ds)}")

    save_csv(ds, Path(CSV_OUTPUT_PATH))

    current_params = None
    if PARAM_FILE_PATH:
        param_path = Path(PARAM_FILE_PATH)
        if param_path.exists():
            current_params = load_param_file(param_path)
            print(f"       Loaded {len(current_params)} parameters from {param_path}")
        else:
            print(f"WARNING: Param file not found: {param_path} — skipping.")

    kb = None
    if KB_FILE_PATH:
        kb_path = Path(KB_FILE_PATH)
        if kb_path.exists():
            kb = load_knowledge_base(kb_path)
            print(f"       Loaded {len(kb)} KB entries from {kb_path}")
        else:
            print(f"WARNING: KB file not found: {kb_path} — skipping.")

    prompt = build_prompt(
        stats=compute_stats(ds),
        excerpt=csv_excerpt(ds),
        current_params=current_params,
        kb=kb,
        drone_model=DRONE_MODEL,
        drone_description=DRONE_DESCRIPTION,
    )

    raw_response = call_llm(prompt)
    print("[4/4] Response received. Parsing...\n")

    changes, narrative = parse_response(raw_response)

    print_report(changes, narrative)

    if changes:
        save_changes_csv(changes, Path(CSV_OUTPUT_PATH).with_name("suggested_params.csv"))

    save_markdown_report(
        changes=changes,
        narrative=narrative,
        report_path=Path(REPORT_OUTPUT_PATH),
        log_name=log_path.name,
        drone_model=DRONE_MODEL,
    )


if __name__ == "__main__":
    main()
