import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

   # Debug: Print data preview
def train_model():
    df = pd.read_csv("data.csv", header=None, names=["ip", "timestamp", "bytes_transferred"])   # Keep this for now
    print("📊 Raw columns from CSV:", df.columns.tolist())
    print("🧪 Sample rows:")
    print(df.head())



    # Use only numeric feature
    X = df[["bytes_transferred"]]

    # Train Isolation Forest
    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(X)

    # Save model to disk
    joblib.dump(model, "model.pkl")
    print("✅ Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_model()
