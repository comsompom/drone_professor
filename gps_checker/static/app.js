const state = {
    lastStreams: null,
    lastTick: Date.now()
};

const $ = (id) => document.getElementById(id);

function fmt(value, suffix = "", digits = 1) {
    if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
    return `${Number(value).toFixed(digits)}${suffix}`;
}

function setText(id, value) {
    $(id).textContent = value === null || value === undefined || value === "" ? "--" : value;
}

async function fetchState() {
    try {
        const response = await fetch("/api/state", {cache: "no-store"});
        render(await response.json());
    } catch (error) {
        setStatus(false, false, "Backend offline");
    }
}

async function rescan() {
    await fetch("/api/rescan", {method: "POST"});
    fetchState();
}

function setStatus(connected, scanning, label) {
    const pill = $("statusPill");
    pill.textContent = label;
    pill.className = "pill";
    if (!connected) pill.classList.add(scanning ? "muted" : "error");
}

function render(data) {
    const fix = data.fix || {};
    const satellites = data.satellites || [];
    const usedCount = satellites.filter((sat) => sat.used).length;

    setStatus(data.connected, data.scanning, data.connected ? "Connected" : (data.scanning ? "Scanning" : "Disconnected"));
    setText("receiverLine", data.connected ? `${data.port} at ${data.baud} baud` : data.source);
    setText("fixType", fix.fix_type || fix.fix_quality);
    setText("rtkStatus", fix.rtk_status || fix.fix_quality);
    setText("satUsed", `${fix.num_sats ?? usedCount} / ${fix.sats_in_view ?? satellites.length}`);
    setText("accuracy", `${fmt(fix.h_acc_m, " m")} / ${fmt(fix.v_acc_m, " m")}`);
    setText("position", fix.lat && fix.lon ? `${Number(fix.lat).toFixed(7)}, ${Number(fix.lon).toFixed(7)}` : "--");
    setText("altitude", fmt(fix.alt_m, " m"));
    setText("satInView", `${satellites.length} in view`);
    setText("signalSummary", satellites.length ? `${usedCount} used, best C/N0 ${bestCno(satellites)}` : "No satellites");
    setText("port", data.port ? `${data.port} (${data.baud})` : "--");
    setText("protocol", data.source);
    setText("software", data.receiver?.software);
    setText("hardware", data.receiver?.hardware);
    setText("rtcm", data.rtcm?.received ? `Message ${data.rtcm.message_type ?? "--"}` : "--");
    setText("bytes", data.streams?.bytes ?? 0);

    renderMessageRate(data.streams || {});
    renderSky(satellites);
    renderSignals(satellites);
    renderTable(satellites);
    renderErrors(data.errors || []);
}

function bestCno(satellites) {
    const values = satellites.map((sat) => Number(sat.cno || 0));
    return values.length ? Math.max(...values) : 0;
}

function renderMessageRate(streams) {
    const now = Date.now();
    if (!state.lastStreams) {
        state.lastStreams = streams;
        state.lastTick = now;
        setText("messageRate", "Collecting messages");
        return;
    }
    const seconds = Math.max((now - state.lastTick) / 1000, 0.1);
    const messages = (streams.nmea + streams.ubx) - (state.lastStreams.nmea + state.lastStreams.ubx);
    setText("messageRate", `${Math.max(messages / seconds, 0).toFixed(1)} msg/s`);
    state.lastStreams = streams;
    state.lastTick = now;
}

function renderSky(satellites) {
    const canvas = $("skyCanvas");
    const rect = canvas.getBoundingClientRect();
    const scale = window.devicePixelRatio || 1;
    canvas.width = Math.floor(rect.width * scale);
    canvas.height = Math.floor(rect.height * scale);
    const ctx = canvas.getContext("2d");
    ctx.scale(scale, scale);
    const width = rect.width;
    const height = rect.height;
    const cx = width / 2;
    const cy = height / 2;
    const radius = Math.min(width, height) * 0.42;

    ctx.clearRect(0, 0, width, height);
    ctx.strokeStyle = "#d9dee5";
    ctx.lineWidth = 1;
    [1, 0.66, 0.33].forEach((r) => {
        ctx.beginPath();
        ctx.arc(cx, cy, radius * r, 0, Math.PI * 2);
        ctx.stroke();
    });

    ctx.beginPath();
    ctx.moveTo(cx - radius, cy);
    ctx.lineTo(cx + radius, cy);
    ctx.moveTo(cx, cy - radius);
    ctx.lineTo(cx, cy + radius);
    ctx.stroke();

    ctx.fillStyle = "#64707d";
    ctx.font = "12px system-ui, sans-serif";
    ctx.fillText("N", cx - 4, cy - radius - 8);
    ctx.fillText("S", cx - 4, cy + radius + 18);
    ctx.fillText("W", cx - radius - 18, cy + 4);
    ctx.fillText("E", cx + radius + 10, cy + 4);

    satellites.forEach((sat) => {
        if (sat.azim === null || sat.azim === undefined || sat.elev === null || sat.elev === undefined) return;
        const az = Number(sat.azim) * Math.PI / 180;
        const elev = Math.max(Math.min(Number(sat.elev), 90), 0);
        const r = radius * (1 - elev / 90);
        const x = cx + Math.sin(az) * r;
        const y = cy - Math.cos(az) * r;
        const cno = Math.max(Number(sat.cno || 0), 0);
        const dot = 7 + Math.min(cno / 10, 5);

        ctx.beginPath();
        ctx.fillStyle = sat.used ? "#1f8f5f" : "#2467d1";
        ctx.arc(x, y, dot, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#14171a";
        ctx.font = "11px system-ui, sans-serif";
        ctx.fillText(String(sat.svid), x + dot + 3, y + 4);
    });
}

function renderSignals(satellites) {
    const root = $("signalBars");
    root.replaceChildren();
    satellites.slice(0, 28).forEach((sat) => {
        const cno = Math.max(Number(sat.cno || 0), 0);
        const bar = document.createElement("div");
        bar.className = `bar ${sat.used ? "used" : ""}`;
        bar.innerHTML = `
            <div class="bar-fill-wrap"><div class="bar-fill" style="height:${Math.min(cno / 55 * 100, 100)}%"></div></div>
            <div class="bar-value">${cno}</div>
            <div class="bar-label">${sat.gnss} ${sat.svid}</div>
        `;
        root.appendChild(bar);
    });
}

function renderTable(satellites) {
    const body = $("satTable");
    body.replaceChildren();
    satellites.forEach((sat) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${sat.gnss ?? "--"}</td>
            <td>${sat.svid ?? "--"}</td>
            <td class="${sat.used ? "used" : "not-used"}">${sat.used ? "Yes" : "No"}</td>
            <td>${sat.cno ?? "--"}</td>
            <td>${sat.elev ?? "--"}</td>
            <td>${sat.azim ?? "--"}</td>
            <td>${sat.signal ?? "--"}</td>
        `;
        body.appendChild(row);
    });
}

function renderErrors(errors) {
    const root = $("errors");
    root.replaceChildren();
    errors.forEach((message) => {
        const div = document.createElement("div");
        div.textContent = message;
        root.appendChild(div);
    });
}

$("rescanBtn").addEventListener("click", rescan);
window.addEventListener("resize", fetchState);
fetchState();
setInterval(fetchState, 1000);
