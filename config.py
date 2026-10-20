import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-120b")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "data/uploads")
VECTORSTORE_DIR = os.getenv("VECTORSTORE_DIR", "data/vectorstore")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
RETRIEVAL_K = 4

SYSTEM_PROMPT = (
    "You are a technical assistant for oil and gas field engineers and maintenance staff. "
    "Answer only using the provided document excerpts. If the answer is not contained in the "
    "excerpts, say so clearly instead of guessing. Always cite the source document and page "
    "number for each claim. For any safety-critical, troubleshooting, or maintenance "
    "recommendation, explicitly remind the user that the guidance must be verified by qualified "
    "personnel before being acted on."
)
