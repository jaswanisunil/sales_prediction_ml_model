from db_operations.create_df_of_prediction_sales import load_data
from common_operations.preprocessing import preprocess
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor
import joblib
import pandas as pd

# Load training data (700k)
df = load_data(limit=700000)

X, y = preprocess(df)

# Split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Model
model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_val)

print("MAE:", mean_absolute_error(y_val, y_pred))
print("R2:", r2_score(y_val, y_pred))

# Feature importance
importance = pd.Series(model.feature_importances_, index=X.columns)
print("\nTop Features:\n", importance.sort_values(ascending=False).head(10))

# Save model + columns
joblib.dump(model, "model.pkl")
joblib.dump(X.columns, "columns.pkl")

print("✅ Model & columns saved")