from flask import Flask, request, jsonify
import pandas as pd
import joblib
from common_operations.preprocessing import preprocess

app = Flask(__name__)

# Load model + columns
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    df = pd.DataFrame([data])

    X, _ = preprocess(df)

    # Fix column mismatch
    X = X.reindex(columns=columns, fill_value=0)

    prediction = model.predict(X)

    return jsonify({
        "predicted_sales": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)