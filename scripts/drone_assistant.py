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
        retriever=vectorstore.as_retriever(search_kwargs={"k": 6}),  # Retrieve top 6 most relevant chunks
        chain_type_kwargs={"prompt": PROMPT}
    )

    return qa_chain


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("🚁 Local ArduPilot AI Assistant Initialization 🚁")
    print("=" * 50 + "\n")

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
