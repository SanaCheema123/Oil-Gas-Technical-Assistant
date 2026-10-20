import streamlit as st

from ml.predict import get_model_metrics, predict_failure_risk

try:
    model_metrics = get_model_metrics()
except Exception:
    model_metrics = None

st.markdown(
    """
    <p class="section-intro">
      Estimate the near-term failure risk of a piece of rotating equipment (e.g. a pump
      or compressor) from its live sensor readings. This is a demo model trained on
      synthetic data for illustration — it is <strong>not</strong> validated against
      real fleet data and must not be used for safety-critical decisions.
    </p>
    """,
    unsafe_allow_html=True,
)

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        pressure = st.slider("Operating pressure (psi)", 200, 800, 450, step=5)
        temperature = st.slider("Operating temperature (°F)", 90, 320, 180, step=2)
        vibration = st.slider("Vibration (mm/s RMS)", 0.0, 25.0, 3.5, step=0.1)
    with col2:
        runtime_hours = st.slider("Runtime hours since last service", 0, 4000, 400, step=10)
        age_years = st.slider("Equipment age (years)", 0.0, 20.0, 5.0, step=0.5)

    submitted = st.form_submit_button("Assess failure risk", type="primary")

if submitted:
    result = predict_failure_risk(
        pressure_psi=pressure,
        temperature_f=temperature,
        vibration_mm_s=vibration,
        runtime_hours_since_service=runtime_hours,
        equipment_age_years=age_years,
    )
    probability_pct = result["probability"] * 100
    risk_level = result["risk_level"]
    risk_class = f"risk-badge risk-{risk_level.lower()}"

    st.markdown(
        f"""
        <div class="card prediction-result">
          <div class="prediction-result-row">
            <span class="prediction-label">Predicted failure risk (next 30 days)</span>
            <span class="{risk_class}">{risk_level}</span>
          </div>
          <div class="prediction-probability">{probability_pct:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(min(max(result["probability"], 0.0), 1.0))

    if model_metrics:
        st.caption(
            f"Model: {model_metrics['model_name']} · "
            f"Accuracy: {model_metrics['accuracy'] * 100:.1f}% · "
            f"ROC AUC: {model_metrics['roc_auc']:.3f} · "
            f"Evaluated on {model_metrics['n_test']} held-out samples."
        )
