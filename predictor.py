import os

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

from analysis import load_data
from logger_config import get_logger

logger = get_logger("predictor")

FEATURES = ["study_hours", "attendance", "internal1",
            "internal2", "assignment"]
TARGET = "semester_score"
MODEL_PATH = "saved_model/model.pkl"


def train_model():
    os.makedirs("saved_model", exist_ok=True)
    df = load_data()
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    joblib.dump(model, MODEL_PATH)
    logger.info(f"Model trained. R2={r2:.3f}, MAE={mae:.2f}")
    return model, r2, mae


def predict_score(study_hours, attendance, internal1, internal2, assignment):
    if not os.path.exists(MODEL_PATH):
        train_model()
    model = joblib.load(MODEL_PATH)
    values = pd.DataFrame(
        [[study_hours, attendance, internal1, internal2, assignment]],
        columns=FEATURES
    )
    result = model.predict(values)[0]
    return round(min(max(result, 0), 100), 1)


if __name__ == "__main__":
    model, r2, mae = train_model()
    print("R2 score:", round(r2, 3))
    print("Average error (MAE):", round(mae, 2), "marks")
    print()
    print("How much each thing adds to the score:")
    for name, coef in zip(FEATURES, model.coef_):
        print(f"  {name}: {coef:.2f}")
    print()
    print("Prediction for a new student:")
    print(predict_score(6, 85, 22, 25, 17), "out of 100")