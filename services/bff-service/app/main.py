from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Header
from fastapi.responses import JSONResponse, Response
from typing import List
from app.schemas import PredictionResponse, FrontModel, FrontLibrary
from dotenv import load_dotenv
import httpx
import json
import os

app = FastAPI()
app.title = "ExplAIn API"
app.version = "0.1.0"

load_dotenv()

api_key_env = os.getenv('API_KEY')

if not api_key_env:
    raise ValueError("La variable de entorno 'API_KEY' no está configurada")

config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

with open(config_path, 'r') as f:
    config = json.load(f)

@app.post("/predict", response_model=PredictionResponse)
async def predict(model_name: str = Form(...), library_name: str = Form(...), file: UploadFile = File(...), x_api_key: str = Header(...) ):
    # Verificar API Key
    if x_api_key != api_key_env:
        raise HTTPException(status_code=401, detail="Acceso no autorizado: clave API incorrecta")

    if model_name not in config['models']:
        return JSONResponse(status_code=400, content={"message": "Modelo no encontrado"})

    if library_name not in config['libraries']:
        return JSONResponse(status_code=400, content={"message": "Librería no encontrada"})

    # Obtener el modelo seleccionado
    model = config["models"][model_name]

    # Llamar al servicio correspondiente
    async with httpx.AsyncClient() as client:
        response = await client.post(model["service"], data={"library_name" : library_name}, files={"file": (file.filename, file.file)})

    # Devolver la respuesta del servicio
    return Response(
        status_code=response.status_code,
        content=response.content,
        media_type=response.headers['Content-Type']
    )

# Obtener el listado de modelos
@app.get('/models', tags=['models'], response_model=List[FrontModel], status_code=200)
def get_models(x_api_key: str = Header(...)):
    # Verificar API Key
    if x_api_key != api_key_env:
        raise HTTPException(status_code=401, detail="Acceso no autorizado: clave API incorrecta")

    models = [
        FrontModel(name=elem["name"], description=elem["description"], type=elem['type'])
        for elem in config["models"].values()
    ]

    models_dict = [model.dict() for model in models]

    return JSONResponse(status_code=200, content=models_dict)

# Obtener el listado de librerías de explicabilidad
@app.get('/libraries', tags=['libraries'], response_model=List[FrontLibrary], status_code=200)
def get_libraries(x_api_key: str = Header(...)):
    # Verificar API Key
    if x_api_key != api_key_env:
        raise HTTPException(status_code=401, detail="Acceso no autorizado: clave API incorrecta")

    libraries = [
        FrontLibrary(name=elem["name"], description=elem["description"],type=elem['type'])
        for elem in config["libraries"].values()
    ]

    libraries_dict = [library.dict() for library in libraries]

    return JSONResponse(status_code=200, content=libraries_dict)
