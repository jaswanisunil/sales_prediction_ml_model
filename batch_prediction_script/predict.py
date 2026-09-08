from db_operations.create_df_of_prediction_sales import load_data
from common_operations.preprocessing import preprocess
import joblib

# Load model + columns
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

# Load evaluation data (200k)
df = load_data(limit=200000, offset=700000)

X, _ = preprocess(df)

# Fix column mismatch
X = X.reindex(columns=columns, fill_value=0)

predictions = model.predict(X)

print(predictions[:10])