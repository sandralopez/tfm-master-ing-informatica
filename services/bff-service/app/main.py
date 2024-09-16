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

    if model_name not in config["models"]:
        return JSONResponse(status_code=400, content={"message" : "El modelo seleccionado no existe"})

    # Validar tipo y tamaño del archivo
    MAX_FILE_SIZE = 5 * 1024 * 1024;
    ALLOWED_TYPES = ["image/png", "image/jpeg", "image/jpg", "image/gif", "png", "jpeg", "jpg", "gif"]

    if file.content_type not in ALLOWED_TYPES:
        return JSONResponse(status_code=400, content={"message" : "El archivo seleccionado debe ser una imagen en formato PNG, JPEG o GIF"})

    file_size = await file.read()

    if len(file_size) > MAX_FILE_SIZE:
        return JSONResponse(status_code=400, content={"message" : "El tamaño de la imagen debe ser menor a 5MB"})

    file.file.seek(0)

    # Obtener el modelo seleccionado
    model = config["models"][model_name]

    # Llamar al servicio correspondiente
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(model["service"], data={"library_name" : library_name}, files={"file": (file.filename, file.file)})

    response_dict = json.loads(response.content)

    # Devolver la respuesta del servicio
    return JSONResponse(status_code=response.status_code, content=response_dict)

# Obtener el listado de modelos
@app.get('/models', tags=['models'], response_model=List[FrontModel], status_code=200)
def get_models(x_api_key: str = Header(...)):
    # Verificar API Key
    if x_api_key != api_key_env:
        raise HTTPException(status_code=401, detail="Acceso no autorizado: clave API incorrecta")

    models = [
        FrontModel(id=elem["id"], name=elem["name"], description=elem["description"], type=elem['type'], library=elem["library"])

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
        FrontLibrary(id=elem["id"], name=elem["name"], description=elem["description"],type=elem['type'])

        for elem in config["libraries"].values()
    ]

    libraries_dict = [library.dict() for library in libraries]

    return JSONResponse(status_code=200, content=libraries_dict)
