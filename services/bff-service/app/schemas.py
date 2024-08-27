from pydantic import BaseModel
from typing import List, Dict, Any

class PredictionRequest(BaseModel):
    data: List[float]
    model_name: str
    explainer_name: str
    extra_params: Dict[str, Any] = {}

class PredictionResponse(BaseModel):
    prediction: Any
    explanation: Any

class FrontModel(BaseModel):
    id: int
    name: str
    description: str
    type: str
    library: int

class FrontLibrary(BaseModel):
    id: int
    name: str
    description: str
    type: str

class Model(BaseModel):
    id: int
    name: str
    description: str
    service: str
    type: str
    library: int

class Library(BaseModel):
    id: int
    name: str
    description: str
    type: str