"""
ArduPilot Flight Log Analyzer — LLM-powered parameter tuning advisor.

Workflow:
  1. Reads an ArduPilot DataFlash .BIN log and extracts full telemetry
     (position, attitude, speed, RC inputs) into a CSV file.
  2. Optionally loads the user's current .param file and an ArduPilot
     parameter knowledge-base JSON.
  3. Sends everything to an OpenAI-compatible LLM with a structured prompt.
  4. Prints the LLM's analysis and renders a table of recommended parameter
     changes (old value → suggested value + reason).

Usage example:
    python ardupilot_analyzer.py

Edit the constants in the USER CONFIGURATION section below to match your setup.
"""

from __future__ import annotations

import csv
import json
import math
import os
import sys
import textwrap
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
from pymavlink import mavutil
from openai import OpenAI

# =============================================================================
# USER CONFIGURATION  ← edit these before running
# =============================================================================

# --- OpenAI credentials & model ---
OPENAI_API_KEY  = "sk-..."                      # your OpenAI API key
OPENAI_MODEL    = "gpt-5.5"                      # model to use

# --- Input files ---
LOG_FILE_PATH   = "00000006.BIN"               # ArduPilot .BIN log
PARAM_FILE_PATH = "ad5_20260423.param"         # current .param file  (or None)
KB_FILE_PATH    = "ardupilot_kb.json"          # parameter knowledge base (or None)

# --- Output ---
CSV_OUTPUT_PATH = "flight_telemetry.csv"       # extracted telemetry CSV

# --- Optional time window (seconds from log start; set None for full log) ---
START_TIME_SECONDS: Optional[float] = None     # e.g. 200
END_TIME_SECONDS:   Optional[float] = None     # e.g. 615

# --- Downsampling for the CSV (1 = no downsampling, 4 = keep every 4th row) ---
DOWNSAMPLE_STEP = 4

# --- Optional: describe your drone for better context ---
DRONE_MODEL       = ""          # e.g. "Volantex Ranger EX 757-3"
DRONE_DESCRIPTION = ""          # e.g. "Fixed-wing, 1800mm wingspan, ~2.1 kg AUW, ArduPlane 4.5"

# =============================================================================
# TELEMETRY EXTRACTION
# =============================================================================


def _msg_to_record(msg, fields: List[str]) -> Dict[str, float]:
    return {f: getattr(msg, f) for f in fields if hasattr(msg, f)}


def extract_flight_data(log_path: Path) -> pd.DataFrame:
    """Parse .BIN log and merge POS / ATT / GPS / XKF1 / RCIN into one DataFrame."""
    print(f"[1/4] Parsing log: {log_path} …")
    mavlog = mavutil.mavlink_connection(str(log_path))

    pos_records:  list[dict] = []
    att_records:  list[dict] = []
    gps_records:  list[dict] = []
    xkf1_records: list[dict] = []
    rcin_records: list[dict] = []

    while True:
        msg = mavlog.recv_match()
        if msg is None:
            break
        mtype = msg.get_type()
        if not hasattr(msg, "TimeUS"):
            continue
        t = msg.TimeUS / 1e6

        if mtype == "POS":
            rec = _msg_to_record(msg, ["Lat", "Lng", "Alt", "RelHomeAlt"])
            rec["t"] = t
            pos_records.append(rec)
        elif mtype == "ATT":
            rec = _msg_to_record(msg, ["Roll", "Pitch", "Yaw", "RollRate", "PitchRate", "YawRate"])
            rec["t"] = t
            att_records.append(rec)
        elif mtype == "GPS":
            rec = _msg_to_record(msg, ["Spd", "Status", "NSats", "HDop"])
            rec["t"] = t
            gps_records.append(rec)
        elif mtype == "XKF1":
            rec = _msg_to_record(msg, ["VN", "VE", "VD", "PN", "PE", "PD"])
            rec["t"] = t
            xkf1_records.append(rec)
        elif mtype == "RCIN":
            # Channels: C1=Roll, C2=Pitch, C3=Throttle, C4=Yaw (standard)
            rec = _msg_to_record(msg, ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"])
            rec["t"] = t
            rcin_records.append(rec)

    if not pos_records or not att_records:
        raise RuntimeError("Required POS / ATT data not found in log.")

    def to_df(records, cols=None):
        df = pd.DataFrame(records).sort_values("t").reset_index(drop=True)
        return df if cols is None else df[[c for c in cols if c in df.columns]]

    pos_df  = to_df(pos_records)
    att_df  = to_df(att_records)
    gps_df  = to_df(gps_records)  if gps_records  else pd.DataFrame(columns=["t"])
    xkf1_df = to_df(xkf1_records) if xkf1_records else pd.DataFrame(columns=["t"])
    rcin_df = to_df(rcin_records)  if rcin_records else pd.DataFrame(columns=["t"])

    base   = pos_df[["t", "Lat", "Lng", "Alt", "RelHomeAlt"]].copy()
    merged = pd.merge_asof(base.sort_values("t"), att_df,  on="t", direction="nearest", tolerance=0.2)

    if not gps_df.empty:
        merged = pd.merge_asof(merged.sort_values("t"), gps_df,  on="t", direction="nearest", tolerance=0.5)
    if not xkf1_df.empty:
        merged = pd.merge_asof(merged.sort_values("t"), xkf1_df, on="t", direction="nearest", tolerance=0.5)
    if not rcin_df.empty:
        merged = pd.merge_asof(merged.sort_values("t"), rcin_df, on="t", direction="nearest", tolerance=0.5)

    merged = merged.dropna(subset=["Roll", "Pitch", "Yaw"]).reset_index(drop=True)
    merged["t_rel"] = merged["t"] - merged["t"].iloc[0]

    # --- Derived channels ---
    # Ground speed
    if "Spd" not in merged.columns:
        merged["Spd"] = np.nan
    if {"VN", "VE"}.issubset(merged.columns):
        ekf_spd = np.sqrt(np.square(merged["VN"]) + np.square(merged["VE"]))
        merged["speed_mps"] = merged["Spd"].fillna(ekf_spd)
    else:
        merged["speed_mps"] = merged["Spd"].fillna(0.0)

    # Vertical speed (EKF VD is down-positive → negate)
    if "VD" in merged.columns:
        merged["vspeed_mps"] = -merged["VD"]
    else:
        merged["vspeed_mps"] = merged["Alt"].diff() / merged["t"].diff()

    # Throttle % from RC C3 PWM
    if "C3" in merged.columns and merged["C3"].notna().any():
        c3 = merged["C3"]
        pwm_min, pwm_max = c3.min(), c3.max()
        if pwm_max > pwm_min:
            merged["throttle_pct"] = ((c3 - pwm_min) / (pwm_max - pwm_min) * 100.0).clip(0, 100)
        else:
            merged["throttle_pct"] = 0.0
    else:
        merged["throttle_pct"] = np.nan

    # RC inputs as % deviation from centre (±100 %)
    for ch, label in [("C1", "rc_roll_pct"), ("C2", "rc_pitch_pct"), ("C4", "rc_yaw_pct")]:
        if ch in merged.columns and merged[ch].notna().any():
            raw = merged[ch]
            centre = (raw.min() + raw.max()) / 2
            half   = (raw.max() - raw.min()) / 2 or 1
            merged[label] = ((raw - centre) / half * 100.0).clip(-100, 100)
        else:
            merged[label] = np.nan

    return merged


def filter_by_time_window(df: pd.DataFrame,
                           start_s: Optional[float],
                           end_s:   Optional[float]) -> pd.DataFrame:
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
    print(f"[2/4] Telemetry CSV saved: {csv_path}  ({len(df)} rows, {len(cols)} columns)")


# =============================================================================
# PARAMETER & KNOWLEDGE-BASE LOADING
# =============================================================================

def load_param_file(path: Path) -> Dict[str, str]:
    """Parse a Mission Planner / ArduPilot .param file (name,value CSV)."""
    params: Dict[str, str] = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(",", 1)
            if len(parts) == 2:
                params[parts[0].strip()] = parts[1].strip()
    return params


def load_knowledge_base(path: Path) -> List[dict]:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# =============================================================================
# TELEMETRY STATISTICS SUMMARY  (to keep prompt concise)
# =============================================================================

def compute_stats(df: pd.DataFrame) -> dict:
    duration = df["t_rel"].iloc[-1] - df["t_rel"].iloc[0]
    stats: dict = {"duration_s": round(float(duration), 1)}

    numeric_cols = [
        "Alt", "RelHomeAlt", "speed_mps", "vspeed_mps", "throttle_pct",
        "Roll", "Pitch", "Yaw", "RollRate", "PitchRate", "YawRate",
        "rc_roll_pct", "rc_pitch_pct", "rc_yaw_pct",
    ]
    for col in numeric_cols:
        if col in df.columns and df[col].notna().any():
            s = df[col].dropna()
            stats[col] = {
                "min":    round(float(s.min()),  3),
                "max":    round(float(s.max()),  3),
                "mean":   round(float(s.mean()), 3),
                "std":    round(float(s.std()),  3),
                "p5":     round(float(s.quantile(0.05)), 3),
                "p95":    round(float(s.quantile(0.95)), 3),
            }
    return stats


# =============================================================================
# LLM PROMPT BUILDER
# =============================================================================

def build_prompt(
    stats:       dict,
    csv_excerpt: str,
    current_params: Optional[Dict[str, str]],
    kb:             Optional[List[dict]],
    drone_model:    str,
    drone_desc:     str,
) -> str:
    sections: list[str] = []

    # 1. Context
    if drone_model or drone_desc:
        sections.append("## Drone Information")
        if drone_model:
            sections.append(f"Model: {drone_model}")
        if drone_desc:
            sections.append(f"Description: {drone_desc}")

    # 2. Stats
    sections.append("## Flight Statistics (from log)")
    sections.append(json.dumps(stats, indent=2))

    # 3. CSV excerpt (first + last 40 rows to keep within context)
    sections.append("## Telemetry Sample (CSV excerpt)")
    sections.append(csv_excerpt)

    # 4. Current parameters
    if current_params:
        sections.append("## Current ArduPilot Parameters")
        param_lines = "\n".join(f"{k} = {v}" for k, v in sorted(current_params.items()))
        sections.append(param_lines)

    # 5. Knowledge base (compact: name + description + range)
    if kb:
        sections.append("## ArduPilot Parameter Knowledge Base (reference)")
        kb_lines = []
        for entry in kb:
            name = entry.get("parameter_name", "")
            disp = entry.get("display_name", "").replace("\u00c2", "").strip()
            desc = entry.get("description", "")
            attrs = entry.get("attributes", {})
            parts = [f"{name}: {desc}"]
            if attrs:
                attr_str = "; ".join(f"{k}={v}" for k, v in attrs.items())
                parts.append(f"[{attr_str}]")
            kb_lines.append(" ".join(parts))
        sections.append("\n".join(kb_lines))

    # 6. Task instructions
    task = textwrap.dedent("""
        ## Your Task

        You are an expert ArduPilot flight controller tuner. Analyze the flight
        telemetry statistics and sample data above. Consider the drone's current
        parameter values and the parameter knowledge base provided.

        Please:

        1. **Summarize the flight behavior**: identify any issues such as
           oscillations, unusual attitude angles, excessive throttle variation,
           poor speed regulation, GPS quality, or erratic RC inputs.

        2. **Analyse current parameters**: note parameters that appear suboptimal
           given the observed flight behavior.

        3. **Suggest parameter changes**: for each parameter you recommend
           changing, output a line in EXACTLY this pipe-delimited format:

           PARAM_CHANGE | <PARAMETER_NAME> | <CURRENT_VALUE> | <SUGGESTED_VALUE> | <REASON>

           Use "N/A" for current value if the parameter is not present in the
           current param file. Keep each PARAM_CHANGE line on its own line so
           it can be parsed automatically.

        4. After all PARAM_CHANGE lines, provide **Additional Notes** with any
           flight safety observations or tuning recommendations that don't map
           to a single parameter change.

        Be specific and conservative — only recommend changes you are confident
        about based on the data provided.
    """).strip()

    sections.append(task)
    return "\n\n".join(sections)


# =============================================================================
# LLM CALL
# =============================================================================

def call_llm(prompt: str) -> str:
    print("[3/4] Sending data to LLM …")
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert ArduPilot flight controller engineer "
                    "specializing in fixed-wing and VTOL drone tuning. "
                    "Your analysis is data-driven, safety-focused, and conservative."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content or ""


# =============================================================================
# RESPONSE PARSING & DISPLAY
# =============================================================================

def parse_and_display(response: str) -> None:
    print("\n" + "=" * 80)
    print("  ARDUPILOT FLIGHT ANALYSIS REPORT")
    print("=" * 80)

    changes: list[tuple[str, str, str, str]] = []
    narrative_lines: list[str] = []

    for line in response.splitlines():
        if line.strip().startswith("PARAM_CHANGE"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                # PARAM_CHANGE | name | current | suggested | reason
                changes.append((parts[1], parts[2], parts[3], parts[4]))
        else:
            narrative_lines.append(line)

    # Print narrative (analysis text)
    print("\n".join(narrative_lines).strip())

    # Print parameter change table
    if changes:
        print("\n" + "=" * 80)
        print("  SUGGESTED PARAMETER CHANGES")
        print("=" * 80)

        col_w = [32, 15, 18, 55]
        header = (
            f"{'Parameter':<{col_w[0]}}"
            f"{'Current':<{col_w[1]}}"
            f"{'Suggested':<{col_w[2]}}"
            f"{'Reason'}"
        )
        sep = "-" * (sum(col_w) + 5)
        print(header)
        print(sep)

        for name, current, suggested, reason in changes:
            # Wrap reason to fit
            reason_words = reason.split()
            reason_lines: list[str] = []
            current_line = ""
            for word in reason_words:
                if len(current_line) + len(word) + 1 <= col_w[3]:
                    current_line = (current_line + " " + word).strip()
                else:
                    if current_line:
                        reason_lines.append(current_line)
                    current_line = word
            if current_line:
                reason_lines.append(current_line)

            # First row
            print(
                f"{name:<{col_w[0]}}"
                f"{current:<{col_w[1]}}"
                f"{suggested:<{col_w[2]}}"
                f"{reason_lines[0] if reason_lines else ''}"
            )
            # Continuation rows for long reasons
            indent = " " * (col_w[0] + col_w[1] + col_w[2])
            for rline in reason_lines[1:]:
                print(f"{indent}{rline}")

        print(sep)
        print(f"\nTotal suggested changes: {len(changes)}")

        # Also save table to CSV
        changes_csv = Path(CSV_OUTPUT_PATH).with_name("suggested_params.csv")
        with open(changes_csv, "w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["Parameter", "Current Value", "Suggested Value", "Reason"])
            writer.writerows(changes)
        print(f"Parameter suggestions also saved to: {changes_csv}")
    else:
        print("\n[No structured PARAM_CHANGE lines found in LLM response — see narrative above.]")


# =============================================================================
# CSV EXCERPT HELPER
# =============================================================================

def csv_excerpt(df: pd.DataFrame, n: int = 40) -> str:
    """Return first n and last n rows as CSV text."""
    cols = [c for c in CSV_COLUMNS if c in df.columns]
    head = df[cols].head(n)
    tail = df[cols].tail(n)
    combined = pd.concat([head, tail]).drop_duplicates(subset=["t_rel"])
    return combined.round(3).to_csv(index=False)


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    log_path = Path(LOG_FILE_PATH)
    csv_path = Path(CSV_OUTPUT_PATH)

    if not log_path.exists():
        sys.exit(f"ERROR: Log file not found: {log_path}")

    # --- Step 1: Extract telemetry ---
    raw = extract_flight_data(log_path)

    if START_TIME_SECONDS is not None and END_TIME_SECONDS is not None:
        if float(START_TIME_SECONDS) > float(END_TIME_SECONDS):
            sys.exit("ERROR: START_TIME_SECONDS must be <= END_TIME_SECONDS")

    filtered = filter_by_time_window(raw, START_TIME_SECONDS, END_TIME_SECONDS)
    if filtered.empty:
        sys.exit("ERROR: No samples in selected time range. Adjust START/END time constants.")

    ds = downsample(filtered, DOWNSAMPLE_STEP)
    print(f"       Samples: total={len(raw)} | selected={len(filtered)} | saved={len(ds)}")

    save_csv(ds, csv_path)

    # --- Step 2: Load optional inputs ---
    current_params: Optional[Dict[str, str]] = None
    if PARAM_FILE_PATH:
        p = Path(PARAM_FILE_PATH)
        if p.exists():
            current_params = load_param_file(p)
            print(f"       Loaded {len(current_params)} parameters from {p}")
        else:
            print(f"WARNING: Param file not found: {p} — skipping.")

    kb: Optional[List[dict]] = None
    if KB_FILE_PATH:
        k = Path(KB_FILE_PATH)
        if k.exists():
            kb = load_knowledge_base(k)
            print(f"       Loaded {len(kb)} KB entries from {k}")
        else:
            print(f"WARNING: KB file not found: {k} — skipping.")

    # --- Step 3: Build prompt ---
    stats   = compute_stats(ds)
    excerpt = csv_excerpt(ds, n=40)
    prompt  = build_prompt(
        stats=stats,
        csv_excerpt=excerpt,
        current_params=current_params,
        kb=kb,
        drone_model=DRONE_MODEL,
        drone_desc=DRONE_DESCRIPTION,
    )

    # Uncomment to inspect prompt before sending:
    # Path("debug_prompt.txt").write_text(prompt, encoding="utf-8")

    # --- Step 4: Call LLM and display results ---
    raw_response = call_llm(prompt)
    print("[4/4] Response received. Parsing …\n")
    parse_and_display(raw_response)


if __name__ == "__main__":
    main()
