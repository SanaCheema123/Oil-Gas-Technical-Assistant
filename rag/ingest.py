import os
from pathlib import Path

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBEDDING_MODEL,
    UPLOAD_DIR,
    VECTORSTORE_DIR,
)


@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def load_and_split(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(pages)

    source_name = Path(pdf_path).name
    for chunk in chunks:
        chunk.metadata["source"] = source_name
        chunk.metadata["page"] = chunk.metadata.get("page", 0) + 1

    return chunks


def ingest_pdf(pdf_path: str):
    """Load a single PDF, split it, embed it, and add it to the persistent vector store."""
    chunks = load_and_split(pdf_path)
    store = get_vectorstore()
    store.add_documents(chunks)
    return len(chunks)


@st.cache_resource
def get_vectorstore():
    os.makedirs(VECTORSTORE_DIR, exist_ok=True)
    return Chroma(
        collection_name="oilgas_docs",
        embedding_function=get_embeddings(),
        persist_directory=VECTORSTORE_DIR,
    )


def save_upload(uploaded_file) -> str:
    """Save a Streamlit UploadedFile to disk and return the saved path."""
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    dest = Path(UPLOAD_DIR) / uploaded_file.name
    with open(dest, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return str(dest)
