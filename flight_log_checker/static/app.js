const $ = (id) => document.getElementById(id);

let appState = null;
let metricCatalog = [];

function setMessage(message, isError = false) {
    const box = $("messageBox");
    box.textContent = message || "";
    box.classList.toggle("error", isError);
}

function setBusy(label) {
    const pill = $("statusPill");
    pill.textContent = label;
    pill.className = "pill busy";
    document.querySelectorAll("button").forEach((button) => button.disabled = true);
}

function setReady(label = "Ready") {
    const pill = $("statusPill");
    pill.textContent = label;
    pill.className = "pill";
    document.querySelectorAll("button").forEach((button) => button.disabled = false);
}

function setError(label = "Error") {
    const pill = $("statusPill");
    pill.textContent = label;
    pill.className = "pill error";
    document.querySelectorAll("button").forEach((button) => button.disabled = false);
}

function fmtSeconds(value) {
    if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
    return `${Number(value).toFixed(2)} s`;
}

function switchTab(tabId) {
    document.querySelectorAll(".tab").forEach((tab) => tab.classList.toggle("active", tab.dataset.tab === tabId));
    document.querySelectorAll(".tab-panel").forEach((panel) => panel.classList.toggle("active", panel.id === tabId));
}

async function loadState() {
    const response = await fetch("/api/state", {cache: "no-store"});
    appState = await response.json();
    metricCatalog = appState.metrics || [];
    render();
}

function render() {
    renderLogs();
    renderMetrics();
    const log = appState?.log || {};
    const win = appState?.window || null;
    $("activeLog").textContent = log.name ? `${log.name} loaded` : "No log selected";
    $("windowState").textContent = win ? "Detected" : "Waiting";
    $("startTime").textContent = fmtSeconds(win?.start_time_s);
    $("endTime").textContent = fmtSeconds(win?.end_time_s);
    $("duration").textContent = fmtSeconds(win?.duration_s);
    $("launchTime").textContent = fmtSeconds(win?.launch_time_s);
    $("landingTime").textContent = fmtSeconds(win?.landing_time_s);
    renderFrame("2d", appState?.outputs?.["2d"]);
    renderFrame("3d", appState?.outputs?.["3d"]);
}

function renderLogs() {
    const select = $("logSelect");
    const current = select.value;
    select.replaceChildren();
    const placeholder = document.createElement("option");
    placeholder.value = "";
    placeholder.textContent = "Select existing log";
    select.appendChild(placeholder);
    (appState?.logs || []).forEach((log) => {
        const option = document.createElement("option");
        option.value = log.path;
        option.textContent = `${log.name} (${log.size_mb} MB, ${log.location})`;
        select.appendChild(option);
    });
    select.value = current || appState?.log?.path || "";
}

function renderMetrics() {
    const root = $("metricList");
    if (root.childElementCount) {
        updateParamCount();
        return;
    }
    metricCatalog.forEach((metric) => {
        const label = document.createElement("label");
        label.className = "metric-option";
        label.innerHTML = `
            <input type="checkbox" value="${metric.id}" ${metric.default ? "checked" : ""}>
            <span class="swatch" style="background:${metric.color}"></span>
            <span><strong>${metric.label}</strong><span>${metric.id} · ${metric.unit}</span></span>
        `;
        label.querySelector("input").addEventListener("change", updateParamCount);
        root.appendChild(label);
    });
    updateParamCount();
}

function selectedMetrics() {
    return [...document.querySelectorAll("#metricList input:checked")].map((item) => item.value);
}

function updateParamCount() {
    $("paramCount").textContent = `${selectedMetrics().length} selected`;
}

function renderFrame(kind, url) {
    const frame = $(`frame${kind}`);
    const empty = $(`empty${kind}`);
    if (!url) {
        frame.classList.remove("active");
        frame.removeAttribute("src");
        empty.classList.remove("hidden");
        return;
    }
    frame.src = url;
    frame.classList.add("active");
    empty.classList.add("hidden");
}

async function selectLog(event) {
    event.preventDefault();
    const form = new FormData();
    const file = $("fileInput").files[0];
    const customPath = $("pathInput").value.trim();
    const selectedPath = $("logSelect").value;

    if (file) {
        form.append("log_file", file);
    } else {
        form.append("log_path", customPath || selectedPath);
    }

    await runTask("Detecting flight window", async () => {
        const response = await fetch("/api/select-log", {method: "POST", body: form});
        await consumeStateResponse(response);
        setMessage("Flight window detected. Generate a 2D or 3D log from the selected file.");
    });
}

async function detectWindow() {
    await runTask("Detecting flight window", async () => {
        const response = await fetch("/api/detect-window", {method: "POST"});
        await consumeStateResponse(response);
        setMessage("Flight window refreshed.");
    });
}

async function generate2d() {
    await runTask("Generating 2D log", async () => {
        const response = await fetch("/api/generate/2d", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({metrics: selectedMetrics()})
        });
        await consumeStateResponse(response);
        setMessage("2D flight log generated.");
        switchTab("view2d");
    });
}

async function generate3d() {
    await runTask("Generating 3D log", async () => {
        const response = await fetch("/api/generate/3d", {method: "POST"});
        await consumeStateResponse(response);
        setMessage("3D flight replay generated.");
        switchTab("view3d");
    });
}

async function runTask(label, task) {
    try {
        setBusy(label);
        setMessage(label);
        await task();
        setReady();
    } catch (error) {
        setError();
        setMessage(error.message, true);
    }
}

async function consumeStateResponse(response) {
    const payload = await response.json();
    if (!response.ok) {
        throw new Error(payload.error || "Request failed");
    }
    appState = payload;
    metricCatalog = payload.metrics || metricCatalog;
    render();
}

function setMetricSelection(mode) {
    const inputs = [...document.querySelectorAll("#metricList input")];
    inputs.forEach((input) => {
        const metric = metricCatalog.find((item) => item.id === input.value);
        if (mode === "all") input.checked = true;
        if (mode === "clear") input.checked = false;
        if (mode === "defaults") input.checked = Boolean(metric?.default);
    });
    updateParamCount();
}

document.querySelectorAll(".tab").forEach((tab) => tab.addEventListener("click", () => switchTab(tab.dataset.tab)));
$("selectForm").addEventListener("submit", selectLog);
$("detectBtn").addEventListener("click", detectWindow);
$("generate2dBtn").addEventListener("click", generate2d);
$("generate3dBtn").addEventListener("click", generate3d);
$("refreshBtn").addEventListener("click", loadState);
$("selectDefaultsBtn").addEventListener("click", () => setMetricSelection("defaults"));
$("selectAllBtn").addEventListener("click", () => setMetricSelection("all"));
$("clearParamsBtn").addEventListener("click", () => setMetricSelection("clear"));

loadState()
    .then(() => setReady("Idle"))
    .catch((error) => {
        setError();
        setMessage(error.message, true);
    });
