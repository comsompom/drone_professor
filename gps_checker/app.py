from __future__ import annotations

import atexit
import os

from flask import Flask, jsonify, render_template

from gps_reader import GpsMonitor


def _safe_int(value: str | None, default: int) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


app = Flask(__name__)
monitor = GpsMonitor(
    forced_port=os.environ.get("GPS_PORT"),
    forced_baud=_safe_int(os.environ.get("GPS_BAUD"), 0) or None
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/state")
def state():
    return jsonify(monitor.snapshot())


@app.route("/api/ports")
def ports():
    return jsonify({"ports": monitor.list_ports()})


@app.post("/api/rescan")
def rescan():
    monitor.rescan()
    return jsonify({"ok": True})


if __name__ == "__main__":
    monitor.start()
    atexit.register(monitor.stop)
    app.run(host="127.0.0.1", port=_safe_int(os.environ.get("GPS_CHECKER_PORT"), 5050), debug=False)
