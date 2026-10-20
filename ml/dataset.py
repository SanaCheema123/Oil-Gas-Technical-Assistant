"""Synthetic equipment-sensor dataset for the failure-risk demo model.

There is no real sensor/maintenance log in this project (only PDF manuals), so this
generates a labeled dataset with a realistic, physically-motivated signal: failure risk
rises with vibration, pressure and temperature deviation from nominal, runtime hours since
the last service, and equipment age. Gaussian noise keeps classes from being linearly
separable so reported metrics stay meaningful.
"""

import numpy as np
import pandas as pd

FEATURE_COLUMNS = [
    "pressure_psi",
    "temperature_f",
    "vibration_mm_s",
    "runtime_hours_since_service",
    "equipment_age_years",
]

NOMINAL_PRESSURE_PSI = 450.0
NOMINAL_TEMPERATURE_F = 180.0


def generate_dataset(n_samples: int = 4000, random_state: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)

    pressure = rng.normal(loc=NOMINAL_PRESSURE_PSI, scale=60, size=n_samples).clip(200, 800)
    temperature = rng.normal(loc=NOMINAL_TEMPERATURE_F, scale=25, size=n_samples).clip(90, 320)
    vibration = rng.gamma(shape=2.0, scale=1.8, size=n_samples).clip(0, 25)
    runtime_hours = rng.exponential(scale=400, size=n_samples).clip(0, 4000)
    age_years = rng.uniform(0, 20, size=n_samples)

    risk_score = (
        0.028 * (vibration**1.4)
        + 0.010 * np.abs(pressure - NOMINAL_PRESSURE_PSI)
        + 0.015 * np.abs(temperature - NOMINAL_TEMPERATURE_F)
        + 0.0022 * runtime_hours
        + 0.11 * age_years
    )
    risk_score += rng.normal(loc=0, scale=0.6, size=n_samples)

    threshold = np.quantile(risk_score, 0.72)
    failure_within_30_days = (risk_score > threshold).astype(int)

    df = pd.DataFrame(
        {
            "pressure_psi": pressure,
            "temperature_f": temperature,
            "vibration_mm_s": vibration,
            "runtime_hours_since_service": runtime_hours,
            "equipment_age_years": age_years,
            "failure_within_30_days": failure_within_30_days,
        }
    )
    return df
