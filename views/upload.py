import os
from html import escape
from pathlib import Path

import streamlit as st

from config import UPLOAD_DIR
from rag.ingest import ingest_pdf, save_upload

st.markdown(
    """
    <p class="section-intro">
      Upload PDF equipment manuals, maintenance reports, or safety guidelines. Each
      document is split into chunks, embedded, and added to the local vector store so
      the Chat Assistant can retrieve and cite it when answering questions.
    </p>
    """,
    unsafe_allow_html=True,
)

uploaded_files = st.file_uploader(
    "Upload PDF manuals or reports",
    type=["pdf"],
    accept_multiple_files=True,
)

if uploaded_files and st.button("Ingest documents", type="primary"):
    with st.spinner("Processing documents..."):
        total_chunks = 0
        for uploaded_file in uploaded_files:
            path = save_upload(uploaded_file)
            total_chunks += ingest_pdf(path)
    st.success(f"Ingested {len(uploaded_files)} document(s), {total_chunks} chunks indexed.")

st.markdown('<h2 class="landing-section-title">Document library</h2>', unsafe_allow_html=True)

upload_dir = Path(UPLOAD_DIR)
existing_files = sorted(upload_dir.glob("*.pdf")) if upload_dir.exists() else []

if not existing_files:
    st.markdown(
        '<p class="section-intro">No documents uploaded yet. Add a PDF above to get started.</p>',
        unsafe_allow_html=True,
    )
else:
    for file_path in existing_files:
        size_kb = os.path.getsize(file_path) / 1024
        st.markdown(
            f"""
            <div class="doc-card">
              <span class="doc-card-icon">📄</span>
              <span class="doc-card-name">{escape(file_path.name)}</span>
              <span class="doc-card-size">{size_kb:,.0f} KB</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
