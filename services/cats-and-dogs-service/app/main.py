import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv
from app.models import load_model
from app.predict import predict_image
from app.schemas import Prediction

load_dotenv()

model_path = os.getenv('MODEL_PATH')
if not model_path:
    raise ValueError("Environment var 'MODEL_PATH' is not set")

model = load_model(model_path)

app = FastAPI()
app.title = "Cats vs Dogs Prediction API"
app.version = "0.1.0"

@app.post("/predict", response_model=Prediction)
async def predict( file: UploadFile = File(...)):
    try:
        prediction = predict_image(file, model)

        return prediction
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=str(e)
        )
