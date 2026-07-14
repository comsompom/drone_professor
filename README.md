# 🚁 Drone Professor: Local ArduPilot AI Assistant

**Drone Professor** is a fully local, privacy-first AI assistant designed to act as an expert avionics engineer for ArduPilot fixed-wing drones. 

Instead of relying on cloud-based LLMs that might hallucinate parameters, this project builds a custom **Knowledge Base (KB)** directly from the official ArduPilot documentation and uses **Retrieval-Augmented Generation (RAG)** alongside a local LLM (Llama 3) to give you accurate parameter settings and hardware wiring instructions.

---

## 📂 Project Structure

Before you begin, ensure your project directory looks like this:

```text
drone_professor/
│
├── venv/                      # Python Virtual Environment (Created in Step 1)
├── kb/                        # Knowledge Base folder (Created in Step 2)
│   ├── ardupilot_kb.md
│   └── ardupilot_hardware_kb.md
│
├── chroma_db/                 # Vector Database (Auto-generated in Step 5)
│
├── scripts/
│   ├── parameter_scraper.py   # Scrapes software parameters
│   ├── hardware_scraper.py    # Scrapes hardware & UART pinouts
│   └── drone_assistant.py     # The main Local LLM RAG application
│
├── gps_checker/               # Flask GPS receiver checker/dashboard
│   ├── app.py                 # Flask server and API routes
│   ├── gps_reader.py          # Serial auto-detection and GPS protocol parsing
│   ├── requirements.txt       # GPS checker dependencies
│   ├── templates/             # Dashboard HTML
│   └── static/                # Dashboard CSS and JavaScript
│
├── flight_log_checker/        # Flask ArduPilot log checker/dashboard
│   ├── app.py                 # Flask server and API routes
│   ├── flight_tools.py        # Wrapper around flight analysis scripts
│   ├── requirements.txt       # Flight log checker dependencies
│   ├── generated/             # Generated 2D/3D HTML output files
│   ├── uploads/               # Uploaded .BIN logs
│   ├── templates/             # Dashboard HTML
│   └── static/                # Dashboard CSS and JavaScript
│
└── README.md                  # This file
```

---

## 🛠 Step 1: Environment Setup

To avoid conflicting with macOS/Linux system Python packages, we will use a Python Virtual Environment (`venv`).

**1. Open your terminal and navigate to your project folder:**
```bash
cd /Users/olegbourdo/Development/Python/drone_professor/
```

**2. Create the Virtual Environment:**
```bash
python3 -m venv venv
```

**3. Activate the Virtual Environment:**
*(You must do this every time you open a new terminal to work on this project)*
```bash
source venv/bin/activate
```

**4. Install all required dependencies:**
```bash
pip install requests beautifulsoup4 langchain langchain-community langchain-huggingface langchain-text-splitters chromadb sentence-transformers
```

---

## 🕷 Step 2: Build the Knowledge Base (Scrapers)

We need to fetch the latest data from the official ArduPilot documentation. 

**1. Create a directory to hold your Knowledge Base files:**
```bash
mkdir kb
```

**2. Run the Parameter Scraper:**
This script downloads all ArduPilot Plane parameters, descriptions, and allowed ranges.
```bash
python scripts/parameter_scraper.py
```

**3. Run the Hardware Scraper:**
This script crawls the ArduPilot hardware pages to map out flight controllers, UARTs, and pinouts.
```bash
python scripts/hardware_scraper.py
```

**4. Move the generated Markdown files to your `kb` folder:**
```bash
mv ardupilot_kb.md kb/
mv ardupilot_hardware_kb.md kb/
```
*(Note: You can safely delete the `.json` files if you only plan to use the local LLM, as the LLM uses the `.md` files).*

---

## 🧠 Step 3: A Note on Fine-Tuning vs. RAG

You might wonder: *"Should I fine-tune the local LLM on this data?"*

**The short answer is No. We use RAG (Retrieval-Augmented Generation) instead.**
* **Fine-Tuning** teaches an AI *how* to talk (tone, style, formatting). It is notoriously bad at memorizing exact facts and will frequently "hallucinate" fake parameters (e.g., guessing `BATT_VOLT_PIN` instead of the correct `BATT_VOLTMULT`).
* **RAG** acts like an "Open-Book Exam". When you ask a question, our script searches your `kb/` folder, grabs the exact paragraphs containing the hardware/parameter specs, and hands them to the LLM. The LLM is strictly instructed to answer *only* using those provided facts. **This guarantees accuracy and prevents hallucinations.**

---

## 🦙 Step 4: Install Local LLM (Ollama)

We use **Ollama** to run the LLM (Large Language Model) locally on your machine. It is highly optimized for Mac Apple Silicon (M1/M2/M3) and standard PC hardware.

**1. Download and Install Ollama:**
Go to [ollama.com](https://ollama.com/) and download the installer for your OS.

**2. Download the Llama 3 Model:**
Open a new terminal window (you don't need to be in your `venv` for this) and run:
```bash
ollama run llama3
```
*Wait for the download to finish. Once you see the `>>>` prompt, type `/bye` to exit. The model is now running in the background.*

---

## 🚀 Step 5: Run the Drone Assistant

Now that your Knowledge Base is built and your local AI is running, it's time to start the assistant!

**1. Ensure your Virtual Environment is active:**
```bash
source venv/bin/activate
```

**2. Run the AI application:**
```bash
python scripts/drone_assistant.py
```

**What happens next?**
* **On the First Run:** The script will read your Markdown files, split them into chunks, convert them into mathematical vectors, and save them in a local folder called `chroma_db`. This takes a minute or two.
* **On Subsequent Runs:** It will instantly load the existing database.

### 💬 Example Questions to Ask:
Once the `You:` prompt appears, try asking:
* *"I am using a Matek H743-Wing. Which physical port should I use to connect my GPS, and what are the exact ArduPilot parameters I need to change to enable it?"*
* *"How do I configure my plane for a hand launch to ensure the motor doesn't spin up while I am still holding it?"*
* *"What parameter controls my minimum airspeed during an auto mission?"*

---

## 📡 GPS Checker: u-blox / Here RTK M8P Dashboard

The repository now includes a separate Flask application in `gps_checker/` for checking a connected GPS/GNSS receiver from a browser. It is intended to provide a lightweight alternative to desktop tools such as u-blox u-center when you want to see live receiver status from Python.

The GPS Checker can:
* Auto-detect connected serial GPS receivers.
* Read common NMEA sentences.
* Read useful u-blox UBX messages such as `NAV-PVT`, `NAV-SAT`, `MON-VER`, and `RXM-RTCM`.
* Show fix type, RTK fixed/float status, position, altitude, horizontal/vertical accuracy, satellite count, sky view, C/N0 signal bars, and satellite details.

### Run the GPS Checker

**1. Install the GPS Checker dependencies:**
```bash
pip install -r gps_checker/requirements.txt
```

**2. Start the Flask app:**
```bash
python gps_checker/app.py
```

**3. Open the dashboard:**
```text
http://127.0.0.1:5050
```

If port `5050` is already in use, run it on another port:
```bash
GPS_CHECKER_PORT=5051 python gps_checker/app.py
```

Then open:
```text
http://127.0.0.1:5051
```

### Force a Known GPS Port

Auto-detection scans serial ports and common GPS baud rates. If you already know the receiver port, you can force it.

On macOS/Linux:
```bash
GPS_PORT=/dev/tty.usbmodem1101 GPS_BAUD=115200 python gps_checker/app.py
```

On Windows:
```powershell
$env:GPS_PORT="COM7"; $env:GPS_BAUD="115200"; python gps_checker/app.py
```

### GPS Output Notes

For the richest dashboard data, configure the receiver to output UBX `NAV-PVT` and `NAV-SAT`. If the receiver outputs only NMEA, the app can still display position and satellite data when `GGA`, `RMC`, `GSA`, and `GSV` sentences are enabled.

---

## 🛰 Flight Log Checker: 2D/3D ArduPilot Log Dashboard

The repository also includes a separate Flask application in `flight_log_checker/` for inspecting ArduPilot DataFlash `.BIN` flight logs from a browser.

The Flight Log Checker can:
* Select an existing log from `logs/*.BIN`.
* Upload a new `.BIN` log through the browser.
* Accept a custom log path.
* Automatically detect the flight start/end window before creating charts.
* Generate a 3D replay using `scripts/flight_3d_replay.py`.
* Generate a configurable 2D chart using telemetry extracted through `scripts/flight_2d_chart.py`.
* Show generated 2D and 3D HTML outputs inside separate dashboard tabs.

The main dashboard has:
* **Main** tab for selecting the log, detecting the flight window, and creating 2D/3D outputs.
* **2D Parameters** tab for selecting which telemetry parameters appear in the 2D chart.
* **2D Log** tab for viewing the generated 2D HTML chart.
* **3D Log** tab for viewing the generated 3D HTML replay.

In the detected flight window panel, `Launch` and `Landing` are displayed on the same row, with `Duration` shown below them.

### Run the Flight Log Checker

**1. Install the Flight Log Checker dependencies:**
```bash
pip install -r flight_log_checker/requirements.txt
```

**2. Start the Flask app:**
```bash
python flight_log_checker/app.py
```

**3. Open the dashboard:**
```text
http://127.0.0.1:5080
```

The app uses port `5080` by default because browser vendors block some local ports, including `5060`, as unsafe.

If port `5080` is already in use, run it on another browser-safe port:
```bash
FLIGHT_LOG_CHECKER_PORT=5081 python flight_log_checker/app.py
```

Then open:
```text
http://127.0.0.1:5081
```

### Flight Log Output Notes

Generated charts are written to `flight_log_checker/generated/`, and uploaded logs are written to `flight_log_checker/uploads/`. Both folders contain local `.gitignore` files so generated HTML files and uploaded logs are not committed by default.

---

## 🛠 Maintenance & Updates

When a new version of ArduPilot is released (e.g., v4.7):
1. Update the `URL` variables inside the two scraper scripts to point to the new documentation.
2. Re-run the scrapers and move the new `.md` files into the `kb/` folder.
3. Delete the `chroma_db/` folder so the AI is forced to rebuild its vector database with the new data:
   ```bash
   rm -rf chroma_db/
   ```
4. Run `python scripts/drone_assistant.py` again!

For GPS Checker changes:
1. Keep its code isolated inside `gps_checker/`.
2. Add new GPS-specific dependencies to `gps_checker/requirements.txt`.
3. Do not commit generated `__pycache__/` files.

For Flight Log Checker changes:
1. Keep its code isolated inside `flight_log_checker/`.
2. Reuse the existing analysis scripts in `scripts/` when possible.
3. Add new flight-log-specific dependencies to `flight_log_checker/requirements.txt`.
4. Do not commit generated HTML files, uploaded `.BIN` logs, or `__pycache__/` files.
