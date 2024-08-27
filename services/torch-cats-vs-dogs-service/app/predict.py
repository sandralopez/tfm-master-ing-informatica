import cv2
import numpy as np
from PIL import Image
from app.schemas import Prediction
from torchvision import transforms
from fastapi import UploadFile, File
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
    prediction = prediction.item()
    prediction = round(prediction, 2)

    if prediction >= 0.5:
        label = "Perro"
        confidence = prediction
    else:
        label = "Gato"
        confidence = 1 - prediction

    return Prediction(label=label, confidence=confidence)
