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

## 🛠 Maintenance & Updates

When a new version of ArduPilot is released (e.g., v4.7):
1. Update the `URL` variables inside the two scraper scripts to point to the new documentation.
2. Re-run the scrapers and move the new `.md` files into the `kb/` folder.
3. Delete the `chroma_db/` folder so the AI is forced to rebuild its vector database with the new data:
   ```bash
   rm -rf chroma_db/
   ```
4. Run `python scripts/drone_assistant.py` again!

