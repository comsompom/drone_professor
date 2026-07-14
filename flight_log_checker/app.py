from __future__ import annotations

import os
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from flight_tools import (
    APP_ROOT,
    GENERATED_DIR,
    PROJECT_ROOT,
    UPLOAD_DIR,
    LogSelectionError,
    detect_window,
    generate_2d_chart,
    generate_3d_replay,
    list_available_logs,
    metric_catalog,
)


def _safe_int(value: str | None, default: int) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024
app.config["UPLOAD_FOLDER"] = str(UPLOAD_DIR)

STATE = {
    "log_path": None,
    "window": None,
    "outputs": {},
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/state")
def state():
    return jsonify(_state_payload())


@app.route("/api/logs")
def logs():
    return jsonify({"logs": list_available_logs()})


@app.route("/api/metrics")
def metrics():
    return jsonify({"metrics": metric_catalog()})


@app.post("/api/select-log")
def select_log():
    try:
        log_path = _resolve_log_request()
        window = detect_window(log_path)
        STATE["log_path"] = str(log_path)
        STATE["window"] = window
        STATE["outputs"] = {}
        return jsonify(_state_payload())
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/api/detect-window")
def detect_selected_window():
    try:
        log_path = _selected_log_path()
        STATE["window"] = detect_window(log_path)
        return jsonify(_state_payload())
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/api/generate/3d")
def generate_3d():
    try:
        log_path = _selected_log_path()
        window = _window_or_detect(log_path)
        output = generate_3d_replay(log_path, window)
        STATE["outputs"]["3d"] = output.name
        return jsonify(_state_payload())
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/api/generate/2d")
def generate_2d():
    try:
        log_path = _selected_log_path()
        window = _window_or_detect(log_path)
        payload = request.get_json(silent=True) or {}
        metrics = payload.get("metrics") or []
        output = generate_2d_chart(log_path, window, metrics)
        STATE["outputs"]["2d"] = output.name
        return jsonify(_state_payload())
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.route("/generated/<path:filename>")
def generated_file(filename: str):
    return send_from_directory(GENERATED_DIR, filename)


def _resolve_log_request() -> Path:
    uploaded = request.files.get("log_file")
    if uploaded and uploaded.filename:
        name = secure_filename(uploaded.filename)
        if not name.lower().endswith(".bin"):
            raise LogSelectionError("Uploaded file must be a .BIN log.")
        output = UPLOAD_DIR / name
        uploaded.save(output)
        return output.resolve()

    raw_path = request.form.get("log_path") or (request.get_json(silent=True) or {}).get("log_path")
    if not raw_path:
        raise LogSelectionError("Select or upload a .BIN log first.")

    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    path = path.resolve()
    if not path.exists() or not path.is_file():
        raise LogSelectionError(f"Log file not found: {path}")
    if path.suffix.lower() != ".bin":
        raise LogSelectionError("Selected file must be a .BIN log.")
    return path


def _selected_log_path() -> Path:
    if not STATE["log_path"]:
        raise LogSelectionError("Select a log before generating charts.")
    path = Path(str(STATE["log_path"]))
    if not path.exists():
        raise LogSelectionError(f"Selected log no longer exists: {path}")
    return path


def _window_or_detect(log_path: Path) -> dict:
    if STATE["window"] is None:
        STATE["window"] = detect_window(log_path)
    return dict(STATE["window"])


def _state_payload() -> dict:
    log_path = STATE["log_path"]
    outputs = dict(STATE["outputs"])
    return {
        "log": {
            "path": log_path,
            "name": Path(log_path).name if log_path else None,
        },
        "window": STATE["window"],
        "outputs": {
            "2d": f"/generated/{outputs['2d']}" if outputs.get("2d") else None,
            "3d": f"/generated/{outputs['3d']}" if outputs.get("3d") else None,
        },
        "logs": list_available_logs(),
        "metrics": metric_catalog(),
        "app_root": str(APP_ROOT),
    }


if __name__ == "__main__":
    port = _safe_int(os.environ.get("FLIGHT_LOG_CHECKER_PORT"), 5080)
    app.run(host="127.0.0.1", port=port, debug=False)
