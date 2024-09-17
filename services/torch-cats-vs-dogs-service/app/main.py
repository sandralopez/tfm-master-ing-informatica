import os
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from app.models import load_model
from app.predict import predict_image, preprocess_image
from app.schemas import PredictionResponse
from explainer_lib import Explainer 

load_dotenv()

model_path = os.getenv('MODEL_PATH')
if not model_path:
    raise ValueError("Environment var 'MODEL_PATH' is not set")

model = load_model(model_path)

app = FastAPI()
app.title = "Pytorch Cats vs Dogs Prediction API"
app.version = "0.1.0"

@app.post("/predict", response_model=PredictionResponse)
async def predict( library_name : str = Form(...), file: UploadFile = File(...)):
    try:
        # Preprocesar imagen (redimensionar, normalizar..)
        processed_image, rgb_image = await preprocess_image(file)

        # Predicción: aplicar np.expand_dims dado que sólo usaremos una imagen para predecir
        prediction = predict_image(model, processed_image)

        explain = Explainer(
            library_name = library_name,
            model = model,
            processed_image = processed_image,
            extra_params = { "label_index": prediction.label_index, "rgb_image" : rgb_image }
        )

        # Aplicar la librería de explicabilidad
        image_explanation = explain.explain()

        return {
            "prediction": prediction,
            "image": image_explanation
        }
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": "Ha ocurrido un error al procesar la petición"})