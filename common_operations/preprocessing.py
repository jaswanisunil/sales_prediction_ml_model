import pandas as pd

TARGET = "Sales"

def preprocess(df):
    df = df.copy()

    # Fill missing values
    df = df.fillna(0)

    # Handle Date
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month
        df["Day"] = df["Date"].dt.day
        df = df.drop("Date", axis=1)

    # Separate target
    if TARGET in df.columns:
        y = df[TARGET]
        df = df.drop(TARGET, axis=1)
    else:
        y = None  # important for prediction

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    return df, y