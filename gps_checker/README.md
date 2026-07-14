# GPS Checker

Browser dashboard for u-blox GPS receivers such as the Here/Here+ RTK M8P. It auto-detects a connected serial GNSS receiver and displays live fix, RTK, satellite, and signal information.

## Setup

From the project root:

```bash
python3 -m venv gps_checker/.venv
source gps_checker/.venv/bin/activate
pip install -r gps_checker/requirements.txt
```

## Run

```bash
python gps_checker/app.py
```

Open:

```text
http://127.0.0.1:5050
```

The app scans serial ports automatically. You can force a known receiver if needed:

```bash
GPS_PORT=/dev/tty.usbmodem1101 GPS_BAUD=115200 python gps_checker/app.py
```

On Windows the port will usually look like `COM3` or `COM7`:

```powershell
$env:GPS_PORT="COM7"; $env:GPS_BAUD="115200"; python gps_checker/app.py
```

## Notes

- The receiver must expose a serial port over USB/UART.
- The app reads both NMEA and UBX streams. UBX `NAV-SAT` and `NAV-PVT` give the richest satellite and RTK status.
- If no satellites are listed, enable NMEA `GSV` or UBX `NAV-SAT` output in the receiver configuration.
