import streamlit as st

from config import GROQ_API_KEY

st.markdown(
    """
    <div class="hero-banner">
      <h1>Oil &amp; Gas Technical Assistant</h1>
      <p>Upload equipment manuals and technical documents, then ask questions in plain
      language. Answers are grounded in your documents and cite the source — and a
      separate model flags rising equipment failure risk from live sensor readings.</p>
      <div class="hero-badges">
        <span class="badge-pill">Retrieval-Augmented</span>
        <span class="badge-pill">Source-Cited</span>
        <span class="badge-pill">Human Verification Required</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if not GROQ_API_KEY:
    st.warning(
        "No GROQ_API_KEY found. Copy `.env.example` to `.env` and add your key before asking questions.",
        icon="⚠️",
    )

cta_col1, cta_col2, cta_col3 = st.columns(3)
with cta_col1:
    st.page_link("views/upload.py", label="Upload documents", icon="📄")
with cta_col2:
    st.page_link("views/chat.py", label="Ask the assistant", icon="💬")
with cta_col3:
    st.page_link("views/risk.py", label="Check failure risk", icon="📈")

st.markdown("<div style='height: 8px'></div>", unsafe_allow_html=True)

st.markdown('<h2 class="landing-section-title">What you can do here</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="feature-grid">
      <div class="feature-card">
        <div class="feature-icon">📄</div>
        <h3>Upload documents</h3>
        <p>Add equipment manuals, maintenance reports, and safety guidelines as PDFs.
        They're chunked, embedded, and indexed into a local vector store.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">💬</div>
        <h3>Ask questions</h3>
        <p>Chat in plain language about procedures or troubleshooting steps. Every
        answer is grounded in your documents and cites the source page.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">📈</div>
        <h3>Predict failure risk</h3>
        <p>Enter live sensor readings for a pump or compressor to estimate near-term
        failure risk, backed by a trained scikit-learn model.</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h2 class="landing-section-title">How it works</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="steps-row">
      <div class="step-card">
        <div class="step-number">1</div>
        <div>
          <h4>Upload a PDF</h4>
          <p>Go to the Upload Documents page and add one or more manuals or reports.</p>
        </div>
      </div>
      <div class="step-card">
        <div class="step-number">2</div>
        <div>
          <h4>Ask a question</h4>
          <p>Open the Chat Assistant and ask about a procedure, spec, or fault code.</p>
        </div>
      </div>
      <div class="step-card">
        <div class="step-number">3</div>
        <div>
          <h4>Verify and act</h4>
          <p>Review the cited sources, then confirm any safety-critical step with
          qualified personnel before acting on it.</p>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
