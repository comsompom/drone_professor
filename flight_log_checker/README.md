# Flight Log Checker

Flask dashboard for ArduPilot DataFlash `.BIN` logs. It selects a log, detects the flight window, generates 3D replay HTML and configurable 2D telemetry chart HTML, then displays those generated files inside application tabs.

## Run

From the project root:

```bash
pip install -r flight_log_checker/requirements.txt
python flight_log_checker/app.py
```

Open:

```text
http://127.0.0.1:5080
```

If the port is busy:

```bash
FLIGHT_LOG_CHECKER_PORT=5081 python flight_log_checker/app.py
```

## Notes

- Existing logs from `logs/*.BIN` are listed automatically.
- You can also upload a `.BIN` log through the dashboard.
- Flight start/end times are detected with `scripts/detect_flight_window.py` before generating any chart.
- 3D generation uses `scripts/flight_3d_replay.py`.
- 2D telemetry extraction uses `scripts/flight_2d_chart.py`; the dashboard controls which metrics are included in the generated chart.
