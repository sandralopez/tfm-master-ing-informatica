from pydantic import BaseModel
from typing import Dict

class Prediction(BaseModel):
    label: str
    confidence: float

class PredictionToExplain(Prediction):
    label_index: int

class PredictionResponse(BaseModel):
    prediction: Prediction
    image: str