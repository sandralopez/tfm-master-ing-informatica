#%%
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet import preprocess_input

#%%
# Cargar el modelo
model = tf.keras.models.load_model(os.getenv('MODEL_PATH'))

#%%
# Cargar y preprocesar la imagen
img_path = os.getenv('IMG_PATH')

# Cargar la imagen con tamaño (224, 224)
img = image.load_img(img_path, target_size=(224, 224))

# Convertir la imagen a un array de numpy
img_array = image.img_to_array(img)


# Aplicar preprocess_input
img_array = preprocess_input(img_array)

# Expandir las dimensiones para que coincida con la entrada del modelo (1, 224, 224, 3)
img_array = np.expand_dims(img_array, axis=0)

#%%
# Hacer la predicción
prediction = model.predict(img_array)[0]

index = np.argmax(prediction)

#%%
confidence = float("{:.2f}".format(prediction[index], 2))

if index == 0:
    label = 'Gato'
else:
    label = 'Perro'
    
print(confidence)
print(label)