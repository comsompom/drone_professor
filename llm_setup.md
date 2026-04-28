


### An Important Note: Fine-Tuning vs. RAG
Before we build this, we need to address **Fine-Tuning**. 

For technical documentation like ArduPilot parameters and hardware pinouts, **Fine-tuning is actually the wrong approach.** 
* **Fine-tuning** teaches an LLM *how* to talk (e.g., formatting, tone, personality). However, it is terrible at remembering exact facts. If you fine-tune, the LLM will likely hallucinate and invent parameter names (e.g., guessing `BATT_VOLT_PIN` instead of the correct `BATT_VOLTMULT`).
* **RAG (Retrieval-Augmented Generation)** is the industry standard for this. With RAG, the LLM acts as an "open-book" student. When you ask a question, a script searches your Knowledge Base files instantly, grabs the exact paragraphs related to your question, gives them to the LLM, and says: *"Answer the user's question using ONLY these exact facts."*

Here is the step-by-step guide to building a **Local RAG System** on your Mac.

---

### Step 1: Install Ollama (The Local LLM Engine)
Ollama is the easiest way to run local LLMs (like Llama 3) on a Mac, as it automatically uses Apple Silicon (M-series chips) for hardware acceleration.

1. Go to [ollama.com](https://ollama.com/) and download the macOS app. Install it.
2. Open your terminal and download a highly capable model (we will use **Llama 3**):
   ```bash
   ollama run llama3
   ```
   *(This will download the model. Once it opens a chat prompt `>>>`, you can type `/bye` to exit. The model is now saved on your Mac).*

---

### Step 2: Install the Python AI Libraries
Activate your virtual environment and install **LangChain** (the RAG framework) and **ChromaDB** (the local vector database that makes text searchable).

```bash
# Activate your environment
source /Users/olegbourdo/Development/Python/drone_professor/venv/bin/activate

# Install the necessary libraries
pip install langchain langchain-community langchain-huggingface langchain-text-splitters chromadb sentence-transformers
```

---

### Step 3: Organize Your Files
Your Python script needs to know where your Knowledge Base is. 
1. Inside your `drone_professor` folder, create a folder named `kb`.
2. Move the two Markdown files we created earlier (`ardupilot_kb.md` and `ardupilot_hardware_kb.md`) into this `kb` folder.

Your folder structure should look like this:
```text
drone_professor/
│
├── venv/
├── kb/
│   ├── ardupilot_kb.md
│   └── ardupilot_hardware_kb.md
│
└── scripts/
    ├── parameter_scraper.py
    ├── hardware_scraper.py
    └── drone_assistant.py  <-- (We are creating this next)
```

---

### Step 4: Create the Local LLM Script
Create a new file in your `scripts` folder named `drone_assistant.py` and paste the following code:

```python
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Configuration
KB_FOLDER = "/Users/olegbourdo/Development/Python/drone_professor/kb"
DB_DIR = "/Users/olegbourdo/Development/Python/drone_professor/chroma_db"
LLM_MODEL = "llama3"

def build_or_load_vector_db():
    # Use HuggingFace's lightweight, fast embedding model to convert text to vectors
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # If the database already exists, just load it (saves time)
    if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
        print("Loading existing Knowledge Base database...")
        vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
        return vectorstore

    print("Building Vector Database from Markdown files (This takes a moment)...")
    
    # 1. Load all Markdown files from the kb folder
    loader = DirectoryLoader(KB_FOLDER, glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    
    # 2. Split the documents into readable chunks for the LLM
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200,
        separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    
    # 3. Create the Chroma Vector Database and save it locally
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=DB_DIR
    )
    print(f"Successfully embedded {len(chunks)} text chunks into the database!")
    return vectorstore

def create_drone_assistant():
    vectorstore = build_or_load_vector_db()
    
    # Initialize the local LLM running via Ollama
    llm = Ollama(model=LLM_MODEL)
    
    # Define the strict System Prompt
    prompt_template = """You are an expert avionics engineer specializing in ArduPilot Fixed-Wing drones.
    You have access to a verified Knowledge Base containing hardware specifications and software parameters.
    
    RULES:
    1. Use ONLY the retrieved Context below to answer the user's question.
    2. If the Context does not contain the answer, say "I cannot find this in my ArduPilot knowledge base." Do NOT invent or guess parameters.
    3. Always format parameter names in EXACT UPPERCASE (e.g., SERIAL1_BAUD).
    4. If hardware wiring is involved, mention the specific UART or Pin.

    Context:
    {context}

    Question: {question}

    Expert Answer:"""
    
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    
    # Create the Retrieval chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 6}), # Retrieve top 6 most relevant chunks
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return qa_chain

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚁 Local ArduPilot AI Assistant Initialization 🚁")
    print("="*50 + "\n")
    
    assistant = create_drone_assistant()
    
    print("\nAssistant is ready! Type 'quit' or 'exit' to stop.\n")
    
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['quit', 'exit']:
            print("Shutting down avionics assistant. Goodbye!")
            break
            
        print("\nThinking...")
        try:
            # Query the Local LLM with RAG
            response = assistant.invoke({"query": user_query})
            print("\nArduPilot AI:\n" + response["result"] + "\n")
        except Exception as e:
            print(f"\n[Error]: {e}\n")
```

---

### Step 5: Test Your Local AI Assistant

Run the script from your terminal:
```bash
python scripts/drone_assistant.py
```

**How it works:**
1. **First Run:** The script will read your `kb/` folder, break your Markdown files into logical chunks (keeping hardware and parameters grouped), and convert them into mathematical vectors using `all-MiniLM-L6-v2`. It saves this data in the `chroma_db` folder. 
2. **Subsequent Runs:** It skips the building process and loads instantly from `chroma_db`.
3. **When you ask a question:** It converts your question into a vector, searches the `chroma_db` for the 6 most highly matching paragraphs, bundles those paragraphs together, and sends them to local **Llama 3** with strict instructions to answer *only* based on what it just found.

**Try asking it questions like:**
* *"I have a Matek H743-Wing. Which port should I use for my GPS, and what are the exact ArduPilot parameters I need to set to enable it?"*
* *"What parameter controls the minimum acceleration required for a hand launch, and what is the range of allowed values?"*

