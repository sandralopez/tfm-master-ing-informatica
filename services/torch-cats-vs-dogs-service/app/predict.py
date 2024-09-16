import cv2
import numpy as np
from PIL import Image
from app.schemas import PredictionToExplain
from torchvision import transforms
from fastapi import UploadFile, File
from io import BytesIO
import torch

img_width, img_height = 256, 256

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

    confidence, index = torch.max(prediction, dim=1)

    index = index.item()

    if index == 0:
        label = 'Gato'
    else:
        label = 'Perro'

    confidence = float("{:.2f}".format(confidence.item(), 2))

    return PredictionToExplain(label=label, label_index=index, confidence=confidence)
