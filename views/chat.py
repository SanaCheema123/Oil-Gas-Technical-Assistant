from html import escape
from pathlib import Path

import streamlit as st

from config import UPLOAD_DIR
from rag.chain import answer_question
from rag.ingest import ingest_pdf, save_upload

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- Left column: document repository (mirrors the PetroRAG console design) ----
with st.sidebar:
    st.markdown(
        """
        <div class="brand">
          <div class="brand-icon">🛢️</div>
          <div class="brand-text">
            <h2>PetroRAG Engine</h2>
            <span>Upstream Engineering</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_files = st.file_uploader(
        "Drop technical manuals (PDF)",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )
    if uploaded_files and st.button("Ingest documents", use_container_width=True):
        with st.spinner("Indexing documents..."):
            total_chunks = 0
            for uploaded_file in uploaded_files:
                path = save_upload(uploaded_file)
                total_chunks += ingest_pdf(path)
        st.success(f"Indexed {len(uploaded_files)} document(s), {total_chunks} chunks.")
        st.rerun()

    st.markdown('<div class="doc-section"><h3>Active indexed manuals</h3></div>', unsafe_allow_html=True)

    upload_dir = Path(UPLOAD_DIR)
    existing_files = sorted(upload_dir.glob("*.pdf")) if upload_dir.exists() else []
    if not existing_files:
        st.caption("No documents indexed yet.")
    else:
        items_html = "".join(
            f'<li class="doc-item">'
            f'<span class="doc-item-title">{escape(f.name)}</span>'
            f'<span class="doc-badge">Indexed</span>'
            f"</li>"
            for f in existing_files
        )
        st.markdown(f'<ul class="doc-list">{items_html}</ul>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="safety-disclaimer">
          <strong>⚠️ Safety Advisory:</strong> Recommendations provided by this AI
          engine are derived from documentation extracts and require sign-off by a
          certified plant engineer prior to execution.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---- Right column: technical operations console ----
top_col1, top_col2 = st.columns([5, 1])
with top_col1:
    st.markdown(
        """
        <div class="chat-header">
          <div>
            <h2>Technical Operations Console</h2>
            <p class="chat-header-sub">Ask about a manual, procedure, or troubleshooting step.</p>
          </div>
          <div class="chat-status">
            <span class="status-dot status-dot-online"></span> Vector Index Online
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_col2:
    if st.button("Clear chat"):
        st.session_state.chat_history = []
        st.rerun()

for role, content, citations in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(content)
        if citations:
            tags_html = "".join(f'<span class="citation-tag">{escape(c)}</span>' for c in citations)
            st.markdown(f'<div class="citations"><span>Sources:</span>{tags_html}</div>', unsafe_allow_html=True)

question = st.chat_input("Ask about maintenance intervals, troubleshooting, or technical specifications...")
if question:
    st.session_state.chat_history.append(("user", question, []))
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents and generating answer..."):
            try:
                answer, sources = answer_question(question)
            except Exception as e:
                answer = f"Something went wrong while generating the answer: {e}"
                sources = []

        st.markdown(answer)

        citation_tags = [
            f'{doc.metadata.get("source", "unknown")} — p.{doc.metadata.get("page", "?")}'
            for doc in sources
        ]
        if citation_tags:
            tags_html = "".join(f'<span class="citation-tag">{escape(c)}</span>' for c in citation_tags)
            st.markdown(f'<div class="citations"><span>Sources:</span>{tags_html}</div>', unsafe_allow_html=True)
            with st.expander("View excerpts"):
                for doc in sources:
                    st.caption(doc.page_content[:400] + "...")

    st.session_state.chat_history.append(("assistant", answer, citation_tags))
