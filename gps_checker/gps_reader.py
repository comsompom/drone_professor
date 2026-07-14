from __future__ import annotations

import math
import struct
import threading
import time
from dataclasses import dataclass, field
from typing import Any

try:
    import serial
    from serial.tools import list_ports
except ImportError:  # pragma: no cover - handled at runtime in the UI
    serial = None
    list_ports = None


BAUD_RATES = (115200, 57600, 38400, 9600, 230400, 4800)
DETECT_SECONDS = 2.0
READ_TIMEOUT = 0.25

GNSS_NAMES = {
    0: "GPS",
    1: "SBAS",
    2: "Galileo",
    3: "BeiDou",
    4: "IMES",
    5: "QZSS",
    6: "GLONASS",
    7: "NavIC",
}

NMEA_TALKERS = {
    "GP": "GPS",
    "GL": "GLONASS",
    "GA": "Galileo",
    "GB": "BeiDou",
    "BD": "BeiDou",
    "GQ": "QZSS",
    "GN": "GNSS",
}

FIX_TYPE = {
    0: "No fix",
    1: "Dead reckoning",
    2: "2D fix",
    3: "3D fix",
    4: "GNSS + DR",
    5: "Time only",
}

GGA_QUALITY = {
    0: "No fix",
    1: "GNSS fix",
    2: "DGPS",
    4: "RTK fixed",
    5: "RTK float",
    6: "Dead reckoning",
}


@dataclass
class ReceiverState:
    connected: bool = False
    scanning: bool = True
    port: str | None = None
    baud: int | None = None
    source: str = "Waiting"
    receiver: dict[str, Any] = field(default_factory=dict)
    fix: dict[str, Any] = field(default_factory=dict)
    satellites: dict[str, dict[str, Any]] = field(default_factory=dict)
    streams: dict[str, int] = field(default_factory=lambda: {"nmea": 0, "ubx": 0, "bytes": 0})
    rtcm: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    detected_at: float | None = None
    last_message_at: float | None = None
    updated_at: float = field(default_factory=time.time)


class GpsMonitor:
    def __init__(self, forced_port: str | None = None, forced_baud: int | None = None) -> None:
        self.forced_port = forced_port
        self.forced_baud = forced_baud
        self._state = ReceiverState()
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._rescan = threading.Event()
        self._thread: threading.Thread | None = None
        self._parser = StreamParser(self._apply_message)
        self._serial = None

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._thread = threading.Thread(target=self._run, name="gps-reader", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        self._rescan.set()
        self._close_serial()
        if self._thread:
            self._thread.join(timeout=2.0)

    def rescan(self) -> None:
        self._rescan.set()

    def list_ports(self) -> list[dict[str, Any]]:
        if list_ports is None:
            return []
        ports = []
        for port in list_ports.comports():
            ports.append({
                "device": port.device,
                "description": port.description,
                "manufacturer": port.manufacturer,
                "hwid": port.hwid,
                "vid": port.vid,
                "pid": port.pid,
                "score": _port_score(port),
            })
        return sorted(ports, key=lambda item: item["score"], reverse=True)

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            data = _copy_state(self._state)
        data["ports"] = self.list_ports()
        data["now"] = time.time()
        return data

    def _run(self) -> None:
        if serial is None:
            self._set_error("pyserial is not installed. Run: pip install -r gps_checker/requirements.txt")
            return

        while not self._stop.is_set():
            self._set_scanning(True)
            target = self._detect_receiver()
            if target is None:
                self._set_disconnected("No GNSS receiver detected")
                self._wait_or_rescan(2.0)
                continue

            port, baud, protocol = target
            try:
                self._serial = serial.Serial(port, baudrate=baud, timeout=READ_TIMEOUT)
                self._set_connected(port, baud, protocol)
                while not self._stop.is_set() and not self._rescan.is_set():
                    chunk = self._serial.read(4096)
                    if chunk:
                        with self._lock:
                            self._state.streams["bytes"] += len(chunk)
                        self._parser.feed(chunk)
                    else:
                        self._mark_stale_if_needed()
            except Exception as exc:  # serial devices disappear often during testing
                self._set_error(f"Serial read failed: {exc}")
            finally:
                self._close_serial()
                self._set_disconnected("Receiver disconnected")
                self._rescan.clear()

    def _detect_receiver(self) -> tuple[str, int, str] | None:
        if self.forced_port:
            baud_rates = (self.forced_baud,) if self.forced_baud else BAUD_RATES
            candidates = [self.forced_port]
        else:
            candidates = [item["device"] for item in self.list_ports()]

        for port in candidates:
            baud_rates = (self.forced_baud,) if self.forced_baud else BAUD_RATES
            for baud in baud_rates:
                if self._stop.is_set() or self._rescan.is_set():
                    self._rescan.clear()
                    return None
                protocol = self._probe_port(port, baud)
                if protocol:
                    return port, baud, protocol
        return None

    def _probe_port(self, port: str, baud: int) -> str | None:
        try:
            with serial.Serial(port, baudrate=baud, timeout=0.2) as ser:
                deadline = time.time() + DETECT_SECONDS
                seen = bytearray()
                while time.time() < deadline and not self._stop.is_set():
                    data = ser.read(512)
                    if data:
                        seen.extend(data)
                        if b"\xb5\x62" in seen:
                            return "UBX"
                        if b"$GP" in seen or b"$GN" in seen or b"$GL" in seen or b"$GA" in seen:
                            return "NMEA"
        except Exception:
            return None
        return None

    def _apply_message(self, kind: str, name: str, payload: Any) -> None:
        with self._lock:
            now = time.time()
            self._state.last_message_at = now
            self._state.updated_at = now
            self._state.streams[kind] += 1
            if kind == "nmea":
                _apply_nmea(self._state, name, payload)
            else:
                _apply_ubx(self._state, name, payload)

    def _set_connected(self, port: str, baud: int, protocol: str) -> None:
        with self._lock:
            self._state.connected = True
            self._state.scanning = False
            self._state.port = port
            self._state.baud = baud
            self._state.source = protocol
            self._state.detected_at = time.time()
            self._state.updated_at = time.time()
            self._state.errors = []

    def _set_disconnected(self, reason: str) -> None:
        with self._lock:
            self._state.connected = False
            self._state.scanning = False
            self._state.port = None
            self._state.baud = None
            self._state.source = reason
            self._state.updated_at = time.time()

    def _set_scanning(self, scanning: bool) -> None:
        with self._lock:
            self._state.scanning = scanning
            self._state.source = "Scanning serial ports" if scanning else self._state.source
            self._state.updated_at = time.time()

    def _set_error(self, message: str) -> None:
        with self._lock:
            self._state.errors = ([message] + self._state.errors)[:5]
            self._state.scanning = False
            self._state.updated_at = time.time()

    def _mark_stale_if_needed(self) -> None:
        with self._lock:
            last = self._state.last_message_at
            if last and time.time() - last > 5:
                self._state.source = "Connected, waiting for data"

    def _wait_or_rescan(self, seconds: float) -> None:
        self._rescan.wait(seconds)
        self._rescan.clear()

    def _close_serial(self) -> None:
        ser = self._serial
        self._serial = None
        if ser:
            try:
                ser.close()
            except Exception:
                pass


class StreamParser:
    def __init__(self, callback) -> None:
        self.callback = callback
        self.buffer = bytearray()

    def feed(self, data: bytes) -> None:
        self.buffer.extend(data)
        while self.buffer:
            ubx_pos = self.buffer.find(b"\xb5\x62")
            nmea_pos = self.buffer.find(b"$")
            positions = [pos for pos in (ubx_pos, nmea_pos) if pos >= 0]
            if not positions:
                self.buffer.clear()
                return

            pos = min(positions)
            if pos:
                del self.buffer[:pos]

            if self.buffer.startswith(b"\xb5\x62"):
                if not self._consume_ubx():
                    return
            elif self.buffer.startswith(b"$"):
                if not self._consume_nmea():
                    return
            else:
                del self.buffer[0]

    def _consume_ubx(self) -> bool:
        if len(self.buffer) < 6:
            return False
        length = self.buffer[4] | (self.buffer[5] << 8)
        total = 6 + length + 2
        if len(self.buffer) < total:
            return False
        packet = bytes(self.buffer[:total])
        del self.buffer[:total]
        if not _valid_ubx_checksum(packet):
            return True
        msg_class = packet[2]
        msg_id = packet[3]
        payload = packet[6:-2]
        name = f"{msg_class:02X}-{msg_id:02X}"
        self.callback("ubx", name, payload)
        return True

    def _consume_nmea(self) -> bool:
        newline = self.buffer.find(b"\n")
        if newline < 0:
            if len(self.buffer) > 512:
                del self.buffer[0]
            return False
        line = bytes(self.buffer[:newline + 1])
        del self.buffer[:newline + 1]
        try:
            sentence = line.decode("ascii", errors="ignore").strip()
        except UnicodeDecodeError:
            return True
        parsed = _parse_nmea(sentence)
        if parsed:
            self.callback("nmea", parsed[0], parsed[1])
        return True


def _apply_nmea(state: ReceiverState, name: str, payload: dict[str, Any]) -> None:
    if name.endswith("GGA"):
        state.fix.update({
            "lat": payload.get("lat"),
            "lon": payload.get("lon"),
            "alt_m": payload.get("alt_m"),
            "fix_quality": payload.get("quality_label"),
            "rtk_status": payload.get("quality_label"),
            "num_sats": payload.get("num_sats"),
            "hdop": payload.get("hdop"),
            "time_utc": payload.get("time_utc"),
        })
    elif name.endswith("RMC"):
        state.fix.update({
            "lat": payload.get("lat") or state.fix.get("lat"),
            "lon": payload.get("lon") or state.fix.get("lon"),
            "speed_mps": payload.get("speed_mps"),
            "heading_deg": payload.get("heading_deg"),
            "date_utc": payload.get("date_utc"),
            "valid": payload.get("valid"),
        })
    elif name.endswith("GSA"):
        state.fix.update({
            "fix_type": payload.get("fix_type"),
            "pdop": payload.get("pdop"),
            "hdop": payload.get("hdop"),
            "vdop": payload.get("vdop"),
        })
        used = set(payload.get("used_satellites", []))
        for satellite in state.satellites.values():
            if str(satellite.get("svid")) in used:
                satellite["used"] = True
    elif name.endswith("GSV"):
        for satellite in payload.get("satellites", []):
            key = f"{satellite['gnss']}-{satellite['svid']}"
            current = state.satellites.get(key, {})
            current.update(satellite)
            current["last_seen"] = time.time()
            state.satellites[key] = current
        state.fix["sats_in_view"] = payload.get("sats_in_view")


def _apply_ubx(state: ReceiverState, name: str, payload: bytes) -> None:
    if name == "01-07":
        parsed = _parse_nav_pvt(payload)
        if parsed:
            state.fix.update(parsed)
    elif name == "01-35":
        parsed = _parse_nav_sat(payload)
        for satellite in parsed:
            key = f"{satellite['gnss']}-{satellite['svid']}"
            satellite["last_seen"] = time.time()
            state.satellites[key] = satellite
        if parsed:
            state.fix["sats_in_view"] = len(parsed)
            state.fix["num_sats"] = sum(1 for sat in parsed if sat.get("used"))
    elif name == "0A-04":
        parsed = _parse_mon_ver(payload)
        if parsed:
            state.receiver.update(parsed)
    elif name == "02-32":
        state.rtcm.update(_parse_rxm_rtcm(payload))


def _parse_nmea(sentence: str) -> tuple[str, dict[str, Any]] | None:
    if not sentence.startswith("$") or not _valid_nmea_checksum(sentence):
        return None
    body = sentence[1:].split("*", 1)[0]
    fields = body.split(",")
    if not fields or len(fields[0]) < 5:
        return None
    name = fields[0]
    sentence_type = name[-3:]
    try:
        if sentence_type == "GGA":
            return name, _parse_gga(fields)
        if sentence_type == "RMC":
            return name, _parse_rmc(fields)
        if sentence_type == "GSA":
            return name, _parse_gsa(fields)
        if sentence_type == "GSV":
            return name, _parse_gsv(fields)
    except (IndexError, ValueError):
        return None
    return name, {}


def _parse_gga(fields: list[str]) -> dict[str, Any]:
    quality = _to_int(_field(fields, 6), 0)
    return {
        "time_utc": _format_nmea_time(_field(fields, 1)),
        "lat": _nmea_coord(_field(fields, 2), _field(fields, 3)),
        "lon": _nmea_coord(_field(fields, 4), _field(fields, 5)),
        "quality": quality,
        "quality_label": GGA_QUALITY.get(quality, f"Quality {quality}"),
        "num_sats": _to_int(_field(fields, 7), None),
        "hdop": _to_float(_field(fields, 8), None),
        "alt_m": _to_float(_field(fields, 9), None),
    }


def _parse_rmc(fields: list[str]) -> dict[str, Any]:
    speed_knots = _to_float(_field(fields, 7), None)
    return {
        "time_utc": _format_nmea_time(_field(fields, 1)),
        "valid": _field(fields, 2) == "A",
        "lat": _nmea_coord(_field(fields, 3), _field(fields, 4)),
        "lon": _nmea_coord(_field(fields, 5), _field(fields, 6)),
        "speed_mps": None if speed_knots is None else speed_knots * 0.514444,
        "heading_deg": _to_float(_field(fields, 8), None),
        "date_utc": _format_nmea_date(_field(fields, 9)),
    }


def _parse_gsa(fields: list[str]) -> dict[str, Any]:
    fix_code = _to_int(_field(fields, 2), 1)
    return {
        "fix_type": {1: "No fix", 2: "2D fix", 3: "3D fix"}.get(fix_code, str(fix_code)),
        "used_satellites": [value for value in fields[3:15] if value],
        "pdop": _to_float(_field(fields, 15), None),
        "hdop": _to_float(_field(fields, 16), None),
        "vdop": _to_float(_field(fields, 17), None),
    }


def _parse_gsv(fields: list[str]) -> dict[str, Any]:
    talker = fields[0][:2]
    gnss = NMEA_TALKERS.get(talker, talker)
    satellites = []
    for i in range(4, len(fields), 4):
        svid = _field(fields, i)
        if not svid:
            continue
        satellites.append({
            "gnss": gnss,
            "svid": svid,
            "elev": _to_int(_field(fields, i + 1), None),
            "azim": _to_int(_field(fields, i + 2), None),
            "cno": _to_int(_field(fields, i + 3), None),
            "used": False,
            "quality": None,
            "signal": "NMEA",
        })
    return {
        "sats_in_view": _to_int(_field(fields, 3), None),
        "satellites": satellites,
    }


def _parse_nav_pvt(payload: bytes) -> dict[str, Any] | None:
    if len(payload) < 84:
        return None
    fix_type = payload[20]
    flags = payload[21]
    carr_soln = (flags >> 6) & 0x03
    lon = struct.unpack_from("<i", payload, 24)[0] * 1e-7
    lat = struct.unpack_from("<i", payload, 28)[0] * 1e-7
    height_msl = struct.unpack_from("<i", payload, 36)[0] / 1000
    h_acc = struct.unpack_from("<I", payload, 40)[0] / 1000
    v_acc = struct.unpack_from("<I", payload, 44)[0] / 1000
    ground_speed = struct.unpack_from("<i", payload, 60)[0] / 1000
    heading = struct.unpack_from("<i", payload, 64)[0] * 1e-5
    pdop = struct.unpack_from("<H", payload, 76)[0] * 0.01
    rtk_status = {0: "No carrier solution", 1: "RTK float", 2: "RTK fixed"}.get(carr_soln, "Unknown")
    return {
        "lat": lat,
        "lon": lon,
        "alt_m": height_msl,
        "fix_type": FIX_TYPE.get(fix_type, f"Fix {fix_type}"),
        "valid": bool(flags & 0x01),
        "num_sats": payload[23],
        "h_acc_m": h_acc,
        "v_acc_m": v_acc,
        "speed_mps": ground_speed,
        "heading_deg": heading % 360,
        "pdop": pdop,
        "rtk_status": rtk_status,
    }


def _parse_nav_sat(payload: bytes) -> list[dict[str, Any]]:
    if len(payload) < 8:
        return []
    count = payload[5]
    satellites = []
    for index in range(count):
        offset = 8 + index * 12
        if offset + 12 > len(payload):
            break
        gnss_id = payload[offset]
        svid = payload[offset + 1]
        cno = payload[offset + 2]
        elev = struct.unpack_from("<b", payload, offset + 3)[0]
        azim = struct.unpack_from("<h", payload, offset + 4)[0]
        flags = struct.unpack_from("<I", payload, offset + 8)[0]
        quality = flags & 0x07
        used = bool(flags & 0x08)
        satellites.append({
            "gnss": GNSS_NAMES.get(gnss_id, f"GNSS {gnss_id}"),
            "svid": str(svid),
            "elev": elev,
            "azim": azim,
            "cno": cno,
            "used": used,
            "quality": quality,
            "signal": _quality_label(quality),
        })
    return satellites


def _parse_mon_ver(payload: bytes) -> dict[str, Any]:
    if len(payload) < 40:
        return {}
    software = payload[0:30].split(b"\x00", 1)[0].decode("ascii", errors="ignore").strip()
    hardware = payload[30:40].split(b"\x00", 1)[0].decode("ascii", errors="ignore").strip()
    extensions = []
    for offset in range(40, len(payload), 30):
        text = payload[offset:offset + 30].split(b"\x00", 1)[0].decode("ascii", errors="ignore").strip()
        if text:
            extensions.append(text)
    return {"software": software, "hardware": hardware, "extensions": extensions}


def _parse_rxm_rtcm(payload: bytes) -> dict[str, Any]:
    result = {"last_seen": time.time(), "received": True}
    if len(payload) >= 8:
        result["flags"] = payload[1]
        result["sub_type"] = struct.unpack_from("<H", payload, 2)[0]
        result["ref_station"] = struct.unpack_from("<H", payload, 4)[0]
        result["message_type"] = struct.unpack_from("<H", payload, 6)[0]
    return result


def _valid_ubx_checksum(packet: bytes) -> bool:
    ck_a = 0
    ck_b = 0
    for value in packet[2:-2]:
        ck_a = (ck_a + value) & 0xFF
        ck_b = (ck_b + ck_a) & 0xFF
    return ck_a == packet[-2] and ck_b == packet[-1]


def _valid_nmea_checksum(sentence: str) -> bool:
    if "*" not in sentence:
        return True
    body, checksum = sentence[1:].split("*", 1)
    checksum = checksum[:2]
    if len(checksum) != 2:
        return False
    value = 0
    for char in body:
        value ^= ord(char)
    try:
        return value == int(checksum, 16)
    except ValueError:
        return False


def _nmea_coord(value: str, direction: str) -> float | None:
    if not value or not direction:
        return None
    dot = value.find(".")
    if dot < 0 or dot < 2:
        return None
    degree_len = dot - 2
    degrees = float(value[:degree_len])
    minutes = float(value[degree_len:])
    coord = degrees + minutes / 60
    if direction in ("S", "W"):
        coord *= -1
    return coord


def _format_nmea_time(value: str) -> str | None:
    if len(value) < 6:
        return None
    return f"{value[0:2]}:{value[2:4]}:{value[4:6]} UTC"


def _format_nmea_date(value: str) -> str | None:
    if len(value) != 6:
        return None
    year = int(value[4:6])
    century = 1900 if year >= 80 else 2000
    return f"{century + year:04d}-{value[2:4]}-{value[0:2]}"


def _field(fields: list[str], index: int) -> str:
    return fields[index] if index < len(fields) else ""


def _to_float(value: str, default: float | None) -> float | None:
    if value == "":
        return default
    try:
        return float(value)
    except ValueError:
        return default


def _to_int(value: str, default: int | None) -> int | None:
    if value == "":
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _quality_label(value: int) -> str:
    return {
        0: "No signal",
        1: "Searching",
        2: "Acquired",
        3: "Detected",
        4: "Code lock",
        5: "Code + carrier",
        6: "Code + carrier",
        7: "Code + carrier",
    }.get(value, str(value))


def _port_score(port: Any) -> int:
    text = " ".join(str(part or "") for part in (port.device, port.description, port.manufacturer, port.hwid)).lower()
    score = 0
    for needle, points in (
        ("u-blox", 100),
        ("ublox", 100),
        ("m8", 50),
        ("gnss", 40),
        ("gps", 40),
        ("receiver", 20),
        ("usb serial", 15),
        ("cp210", 10),
        ("ch340", 10),
        ("ftdi", 10),
    ):
        if needle in text:
            score += points
    return score


def _copy_state(state: ReceiverState) -> dict[str, Any]:
    satellites = list(state.satellites.values())
    satellites.sort(key=lambda sat: (not bool(sat.get("used")), -(sat.get("cno") or 0), sat.get("gnss", ""), sat.get("svid", "")))
    active = [sat for sat in satellites if sat.get("last_seen", 0) > time.time() - 20]
    return {
        "connected": state.connected,
        "scanning": state.scanning,
        "port": state.port,
        "baud": state.baud,
        "source": state.source,
        "receiver": dict(state.receiver),
        "fix": dict(state.fix),
        "satellites": active,
        "streams": dict(state.streams),
        "rtcm": dict(state.rtcm),
        "errors": list(state.errors),
        "detected_at": state.detected_at,
        "last_message_at": state.last_message_at,
        "updated_at": state.updated_at,
    }
