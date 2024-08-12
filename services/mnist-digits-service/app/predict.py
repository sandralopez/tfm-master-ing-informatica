from PIL import Image
from app.schemas import Prediction
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img

def preprocess_image(image: Image.Image):
    img_width, img_height = 28, 28

    image = image.resize((img_width, img_height))
    image = image.convert('L')
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image /= 255.0

    return image

def predict_image(file, model):
    img = Image.open(file.file)

    img_array = preprocess_image(img)

    prediction = model.predict(img_array)

    predicted_class_index = np.argmax(prediction)

    label = str(predicted_class_index)
    confidence = round(prediction[0][predicted_class_index], 2)
    confidence = str(confidence)

    return Prediction(label=label, confidence=confidence)