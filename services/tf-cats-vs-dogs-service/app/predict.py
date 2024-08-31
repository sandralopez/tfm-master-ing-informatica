import numpy as np
from PIL import Image
from app.schemas import PredictionToExplain
from tensorflow.keras.preprocessing.image import img_to_array
from fastapi import UploadFile, File

def preprocess_image(file: UploadFile = File(...)):
    img_width, img_height = 256, 256

    image = Image.open(file.file)
    image = image.resize((img_width, img_height))
    image = img_to_array(image)
    image /= 255.0

    return image

def predict_image(model, processed_image):
    prediction = model.predict(processed_image)[0]

    index = np.argmax(prediction)

    confidence = round(prediction[index], 2)

    if index == 0:
        label = 'Gato'
    else:
        label = 'Perro'

    return PredictionToExplain(label=label, label_index=index, confidence=confidence)