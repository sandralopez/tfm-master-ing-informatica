from PIL import Image
from app.schemas import PredictionToExplain
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet import preprocess_input
from fastapi import UploadFile, File
import numpy as np

def preprocess_image(file: UploadFile = File(...)):
    img_width, img_height = 224, 224

    image = Image.open(file.file)
    image = image.resize((img_width, img_height))
    image = img_to_array(image)
    image = preprocess_input(image)

    return image

def predict_image(model, processed_image):
    prediction = model.predict(processed_image)[0]

    index = np.argmax(prediction)

    confidence = float("{:.2f}".format(prediction[index], 2))

    if index == 0:
        label = 'Gato'
    else:
        label = 'Perro'

    return PredictionToExplain(label=label, label_index=index, confidence=confidence)