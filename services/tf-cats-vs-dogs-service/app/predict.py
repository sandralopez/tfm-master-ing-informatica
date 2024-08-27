from PIL import Image
from app.schemas import PredictionToExplain
from tensorflow.keras.preprocessing.image import img_to_array
from fastapi import UploadFile, File

def preprocess_image(file: UploadFile = File(...)):
    img_width, img_height = 150, 150

    image = Image.open(file.file)
    image = image.resize((img_width, img_height))
    image = img_to_array(image)
    image /= 255.0

    return image

def predict_image(model, processed_image):
    prediction = model.predict(processed_image)[0]
    prediction = float(prediction)
    prediction = round(prediction, 2)

    if prediction > 0.5:
        label = "Perro"
        label_index = 1
        confidence = prediction
    else:
        label = "Gato"
        label_index = 0
        confidence = 1 - prediction

    return PredictionToExplain(label=label, label_index=label_index, confidence=confidence)