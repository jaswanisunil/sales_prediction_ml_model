from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from common_operations.preprocessing import preprocess
from db_operations.create_df_of_prediction_sales import load_data

app = FastAPI(title="Sales Prediction API")

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

# -------------------------
# 1. Real-time prediction
# -------------------------
class SalesInput(BaseModel):
    Store: int
    DayOfWeek: int
    Date: str
    Customers: int
    Open: int
    Promo: int
    StateHoliday: str
    SchoolHoliday: int

@app.post("/predict")
def predict(data: SalesInput):
    df = pd.DataFrame([data.dict()])

    X, _ = preprocess(df)
    X = X.reindex(columns=columns, fill_value=0)

    prediction = model.predict(X)

    return {"predicted_sales": float(prediction[0])}

# -------------------------
# 2. Batch prediction from DB
# -------------------------
class DBInput(BaseModel):
    db_path: str
    limit: int = 10
    offset: int = 0

@app.post("/predict-from-db")
def predict_from_db(data: DBInput):
    df = load_data(data.db_path, data.limit, data.offset)

    original_df = df.copy()  # keep original for response

    X, _ = preprocess(df)
    X = X.reindex(columns=columns, fill_value=0)

    predictions = model.predict(X)

    # Attach predictions to original data
    original_df["PredictedSales"] = predictions

    # Convert to readable JSON
    result = original_df.head(10).to_dict(orient="records")

    return {
        "total_records": len(predictions),
        "predictions_sample": result
    }