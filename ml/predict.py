"""Loads the trained failure-risk model and serves predictions + metrics to the UI.

Trains and caches artifacts on first use if `ml/artifacts/` is missing or stale.
"""

import json

import joblib
import pandas as pd
import streamlit as st

from ml.dataset import FEATURE_COLUMNS
from ml.train import METRICS_PATH, MODEL_PATH, train_and_save

RISK_LEVELS = [
    (0.33, "Low"),
    (0.66, "Medium"),
    (1.01, "High"),
]


def _ensure_artifacts() -> None:
    if not MODEL_PATH.exists() or not METRICS_PATH.exists():
        train_and_save()


@st.cache_data
def get_model_metrics() -> dict:
    _ensure_artifacts()
    return json.loads(METRICS_PATH.read_text())


@st.cache_resource
def _load_model():
    _ensure_artifacts()
    return joblib.load(MODEL_PATH)


def risk_level(probability: float) -> str:
    for upper_bound, label in RISK_LEVELS:
        if probability < upper_bound:
            return label
    return "High"


def predict_failure_risk(
    pressure_psi: float,
    temperature_f: float,
    vibration_mm_s: float,
    runtime_hours_since_service: float,
    equipment_age_years: float,
) -> dict:
    model = _load_model()
    features = pd.DataFrame(
        [[pressure_psi, temperature_f, vibration_mm_s, runtime_hours_since_service, equipment_age_years]],
        columns=FEATURE_COLUMNS,
    )
    probability = float(model.predict_proba(features)[0, 1])
    return {
        "probability": probability,
        "risk_level": risk_level(probability),
    }
