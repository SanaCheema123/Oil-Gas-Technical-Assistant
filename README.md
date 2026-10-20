# Oil & Gas Technical Assistant

A RAG-based chatbot that lets oil and gas professionals upload PDF manuals, maintenance
reports, and safety guidelines, then ask natural-language questions. Answers are grounded
in the uploaded documents and cite the source document and page.

> All safety-critical recommendations must be verified by qualified personnel before use.

## Stack

- **UI:** Streamlit
- **Orchestration:** LangChain
- **Vector store:** ChromaDB (persisted locally in `data/vectorstore`)
- **Embeddings:** sentence-transformers (`all-MiniLM-L6-v2`, runs locally, no API key)
- **LLM:** Groq (via `GROQ_API_KEY`, Llama 3.3 70B by default)

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and add your `GROQ_API_KEY`.
3. Run the app:
   ```
   streamlit run app.py
   ```
4. Use the top navigation bar to open **Upload Documents**, add PDFs and click
   **Ingest documents**, then go to **Chat Assistant** to ask questions.

## Project layout

```
app.py                Entry point: page config, theme, top navigation
views/landing.py       Home page (overview, feature cards, CTAs)
views/upload.py        PDF upload + document library page
views/chat.py          Chat assistant page
views/risk.py          Equipment failure risk page
config.py              Env-driven settings and the system prompt
rag/ingest.py           PDF loading, chunking, embedding, vector store
rag/chain.py             Retrieval + Groq answer generation
data/uploads/            Saved PDFs
data/vectorstore/        Persisted Chroma DB
```
