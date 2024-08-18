from PIL import Image
from app.schemas import Prediction
from torchvision import transforms
from fastapi import UploadFile, File
import cv2
import numpy as np
from io import BytesIO

img_width, img_height = 150, 150

async def preprocess_image(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(BytesIO(contents))
    
    preprocess = transforms.Compose([
        transforms.Resize((img_height, img_width), interpolation=Image.NEAREST),
        transforms.ToTensor()
    ])
    
    rgb_image = preprocess(image)
    img_tensor = rgb_image.unsqueeze(0)
    rgb_image = rgb_image.numpy().transpose(1, 2, 0)

    return img_tensor, rgb_image

def predict_image(model, processed_image):
    prediction = model(processed_image)

    if prediction.item() >= 0.5:
        label = "Perro"
    else:
        label = "Gato"

    confidence = prediction.item()

    return Prediction(label=label, confidence=confidence)
