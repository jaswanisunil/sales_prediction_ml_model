# 🏪 Sales Prediction by Store (ML + FastAPI + Flask)

This project builds a Machine Learning model to predict store sales based on features like store details, promotions, holidays, and customer count.

It supports:

* ✅ Batch prediction from SQLite DB
* ✅ Real-time prediction via API
* ✅ FastAPI with Swagger UI
* ✅ Flask API

---

# 🚀 1. Project Setup

## 🔹 Clone the Repository

```bash
git clone <your-repo-url>
cd Sales_Prediction_By_Store
```

---

## 🔹 Install Dependencies (Using uv)

Make sure Python 3.12+ is installed.

```bash
pip install uv
uv sync
```

---

# 📂 2. Project Structure

```
Sales_Prediction_By_Store/
│
├── db_operations/              # SQLite data loading
├── common_operations/          # Preprocessing logic
├── model_training/             # Training script
├── batch_prediction_script/    # Batch prediction
│
├── app.py                      # Flask API
├── fastapi_app.py              # FastAPI (Swagger)
│
├── model.pkl                   # Trained model
├── columns.pkl                 # Feature columns
├── regression.db               # SQLite database
├── pyproject.toml
```

---

# 🧠 3. Train the Model

Train using first 700k records:

```bash
uv run python -m model_training.train_model
```

This will:

* Train XGBoost model
* Save `model.pkl`
* Save `columns.pkl`

---

# 📊 4. Batch Prediction

Run prediction on next 200k records:

```bash
uv run python -m batch_prediction_script.predict
```

---

# ⚡ 5. Run FastAPI (Recommended)

Start API:

```bash
uv run uvicorn fastapi_app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 🔮 6. Real-Time Prediction API

### Endpoint:

```
POST /predict
```

### Sample Request:

```json
{
  "Store": 1,
  "DayOfWeek": 3,
  "Date": "2024-01-15",
  "Customers": 200,
  "Open": 1,
  "Promo": 1,
  "StateHoliday": "0",
  "SchoolHoliday": 0
}
```

### Sample Response:

```json
{
  "predicted_sales": 5352.22
}
```

---

# 🗄️ 7. Batch Prediction from SQLite DB

### Endpoint:

```
POST /predict-from-db
```

### Sample Request:

```json
{
  "db_path": "D:/path/to/regression.db",
  "limit": 10,
  "offset": 0
}
```

### Sample Response:

```json
{
  "total_records": 10,
  "predictions_sample": [
    {
      "Store": 1,
      "Date": "2015-07-31",
      "Customers": 555,
      "Promo": 1,
      "PredictedSales": 5352.22
    }
  ]
}
```

---

# 🌐 8. Run Flask API (Alternative)

```bash
uv run python app.py
```

Endpoint:

```
POST http://127.0.0.1:5000/predict
```

---

# ⚠️ 9. Important Notes

* Ensure `regression.db` path is correct
* Always use valid date format:

  ```
  YYYY-MM-DD
  ```
* Model uses:

  * Feature engineering (Date → Year, Month, Day)
  * One-hot encoding
* Column consistency handled via `columns.pkl`

---

# 📈 10. Model Details

* Model: XGBoost Regressor
* Evaluation Metrics:

  * MAE (Mean Absolute Error)
  * R² Score
* Features:

  * Store, Customers, Promo, Holidays, Date features

---

# 🏁 11. End-to-End Flow

```
SQLite DB → Preprocessing → Model Training → Save Model
                                   ↓
                           API Prediction
```

---

# 🤖 12. Machine Learning Model Details

---

## 🔹 ML Model Selected

The project uses **XGBoost Regressor** for predicting store sales.

### Why XGBoost?

* Works very well for **structured/tabular data**
* Handles **non-linear relationships**
* Provides **high accuracy** compared to traditional models
* Built-in support for **feature importance**
* Efficient for **large datasets (1M records)**

---

## 🔹 Features Selected

### Original Features Used:

* **Store** → Store ID
* **DayOfWeek** → Day of the week
* **Customers** → Number of customers visiting the store
* **Open** → Whether store is open or closed
* **Promo** → Promotion running (1/0)
* **StateHoliday** → State holiday indicator
* **SchoolHoliday** → School holiday indicator

---

### Feature Engineering:

The `Date` column was transformed into:

* **Year**
* **Month**
* **Day**

👉 This helps the model learn:

* Seasonal trends
* Monthly sales patterns
* Daily variations

---

### Encoding:

* Categorical features like `StateHoliday` are converted using:

  ```python
  pd.get_dummies()
  ```

---

## 🔹 Feature Importance

Feature importance is extracted using:

```python
model.feature_importances_
```

### Key Observations:

* **Customers** → Most influential feature (higher customers = higher sales)
* **Promo** → Promotions significantly increase sales
* **Open** → Sales occur only when store is open
* **Month / Day** → Capture seasonal trends
* **DayOfWeek** → Weekly behavior patterns

---

## 🔹 Evaluation of the Model

The model is evaluated using:

### 1. Mean Absolute Error (MAE)

* Measures average prediction error
* Lower value = better performance

Example:

```
MAE: 800
```

👉 On average, predictions are off by ~800 sales units.

---

### 2. R² Score (R-Squared)

* Measures how well the model explains variance
* Range: 0 to 1

Example:

```
R2: 0.92
```

👉 Model explains **92% of the variation in sales data**.

---

## 🔹 Data Splitting Strategy

* **700,000 records** → Training
* **200,000 records** → Validation
* **100,000 records** → Simulated production

---

## 🔹 Deployment

The model is deployed using:

* **Batch prediction script** (for bulk processing)
* **Flask API** (real-time prediction)
* **FastAPI (Swagger UI)** (interactive API testing)

---

## 🔹 Summary

* XGBoost model provides high accuracy for sales prediction
* Feature engineering improves model performance
* Evaluation metrics confirm strong predictive capability
* APIs enable both batch and real-time predictions

# 👨‍💻 Author

Sunil Jaswani
