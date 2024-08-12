from PIL import Image
from app.schemas import Prediction
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img

def preprocess_image(image: Image.Image):
    img_width, img_height = 150, 150

    image = image.resize((img_width, img_height))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image /= 255.0

    return image

def predict_image(file, model):
    img = Image.open(file.file)

    img_array = preprocess_image(img)

    prediction = model.predict(img_array)[0]
    prediction = float(prediction)

    if prediction > 0.5:
        label = "Perro"
        confidence = round(prediction)
    else:
        label = "Gato"
        confidence = round(1 - prediction, 2)

    return Prediction(label=label, confidence=confidence)