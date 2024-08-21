from PIL import Image
from app.schemas import PredictionToExplain
from tensorflow.keras.preprocessing.image import img_to_array
from fastapi import UploadFile, File
import numpy as np 

def preprocess_image(file: UploadFile = File(...)):
    img_width, img_height = 28, 28

    image = Image.open(file.file)
    image = image.convert('L')
    image = image.resize((img_width, img_height))
    image = img_to_array(image)
    image /= 255.0

    return image

def predict_image(model, processed_image):
    prediction = model.predict(processed_image)[0]

    index = np.argmax(prediction)

    confidence = prediction[index]

    return PredictionToExplain(label=str(index), label_index=index, confidence=confidence)