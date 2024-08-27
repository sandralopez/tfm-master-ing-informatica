#%%
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

#%%
# Cargar el modelo
model = tf.keras.models.load_model(os.getenv('MODEL_PATH'))

#%%
# Cargar y preprocesar la imagen
img_path = os.getenv('IMG_PATH')

img_width, img_height = 150, 150

img = image.load_img(img_path, target_size=(img_width, img_height))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0
#%%
# Hacer la predicción
prediction = model.predict(img_array)

if prediction[0] > 0.5:
    print("Perro")
else:
    print("Gato")

print(prediction[0])