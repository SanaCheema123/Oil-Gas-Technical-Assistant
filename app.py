import streamlit as st

from config import LLM_MODEL
from ml.predict import get_model_metrics
from theme import CSS

st.set_page_config(
    page_title="Oil & Gas Technical Assistant",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(CSS, unsafe_allow_html=True)

try:
    model_metrics = get_model_metrics()
except Exception:
    model_metrics = None

accuracy_pct = f"{model_metrics['accuracy'] * 100:.1f}%" if model_metrics else "—"

st.markdown(
    f"""
    <div class="status-bar">
      <div class="status-bar-group">
        <span class="status-chip">
          <span class="status-dot status-dot-online"></span> System Online
        </span>
        <span class="status-chip">Answer Engine: {LLM_MODEL}</span>
        <span class="status-chip status-chip-accent">
          Failure-Risk Model Accuracy: {accuracy_pct}
        </span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

pages = [
    st.Page("views/landing.py", title="Home", icon="🏠", default=True),
    st.Page("views/upload.py", title="Upload Documents", icon="📄"),
    st.Page("views/chat.py", title="Chat Assistant", icon="💬"),
    st.Page("views/risk.py", title="Equipment Failure Risk", icon="📈"),
]

pg = st.navigation(pages, position="top")
pg.run()
