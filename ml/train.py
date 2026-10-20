"""Trains the equipment failure-risk demo model and saves it with its metrics.

Run directly (`python -m ml.train`) to regenerate `ml/artifacts/`, or call
`train_and_save()` programmatically — `ml/predict.py` does this automatically the
first time a prediction is requested and no saved model exists yet.
"""

import json
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split

from ml.dataset import FEATURE_COLUMNS, generate_dataset

ARTIFACTS_DIR = Path(__file__).parent / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "failure_model.joblib"
METRICS_PATH = ARTIFACTS_DIR / "metrics.json"


def train_and_save(random_state: int = 42) -> dict:
    df = generate_dataset(random_state=random_state)
    X = df[FEATURE_COLUMNS]
    y = df["failure_within_30_days"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        random_state=random_state,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    metrics = {
        "model_name": "RandomForestClassifier",
        "target": "failure_within_30_days",
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
        "precision": round(float(precision_score(y_test, y_pred)), 4),
        "recall": round(float(recall_score(y_test, y_pred)), 4),
        "f1": round(float(f1_score(y_test, y_pred)), 4),
        "roc_auc": round(float(roc_auc_score(y_test, y_proba)), 4),
    }

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(metrics, indent=2))

    return metrics


if __name__ == "__main__":
    result = train_and_save()
    print(json.dumps(result, indent=2))
