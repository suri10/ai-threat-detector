from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model.pkl")
model = joblib.load(MODEL_PATH)

app = FastAPI()

# Input schema
class PredictRequest(BaseModel):
    bytes_transferred: float

# Prediction endpoint with confidence
@app.post("/predict")
def predict_threat(data: PredictRequest):
    input_data = [[data.bytes_transferred]]
    prediction = model.predict(input_data)[0]
    
    # Check if model supports probability prediction
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_data)[0]
        confidence = max(proba)
    else:
        confidence = None  # fallback if model doesn't support it

    result = "Threat" if prediction == 1 else "No Threat"
    
    return {
        "prediction": result,
        "confidence": round(confidence, 3) if confidence is not None else "N/A"
    }
