from PIL import Image
from app.schemas import Prediction
from torchvision import transforms
from fastapi import UploadFile, File
import cv2
import numpy as np
from io import BytesIO
import torch

img_width, img_height = 28, 28

async def preprocess_image(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(BytesIO(contents))
    
    preprocess = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
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

    label = index.item()
    confidence = round(confidence.item(), 2)

    return Prediction(label=str(label), confidence=confidence)