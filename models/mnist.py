from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

#%%
# Función para invertir los colores de la imagen (negro/blanco)
def invert_colors(image):
    return 1 - image

#%%
# Cargar el dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#%%
# Normalizar las imágenes para que los valores de los píxeles sean 0 o 1
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

#%%
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

#%%
# Convertir las etiquetas a one-hot encoding
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

#%%
# Invertir los colores de las imágenes para añadirlas al dataset
# Así podremos utilizar imágenes con blanco sobre fondo negro
# y también imágenes con negro sobre fondo blanco
x_train_inverted = invert_colors(x_train)
y_train_inverted = y_train

x_train_combined = np.concatenate((x_train, x_train_inverted), axis=0)
y_train_combined = np.concatenate((y_train, y_train_inverted), axis=0)

#%%
# Aplicar data augmentation al conjunto de entrenamiento
train_datagen = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.1,
    shear_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    fill_mode='nearest'
)

#%%
# Definir el modelo
model = keras.Sequential([
          keras.Input(shape=(28, 28, 1)),
          layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
          layers.MaxPooling2D(pool_size=(2, 2)),
          layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
          layers.MaxPooling2D(pool_size=(2, 2)),
          layers.Flatten(),
          layers.Dropout(0.5),
          layers.Dense(10, activation='softmax')
])

model.summary()

#%%
# Entrenar el modelo
batch_size = 64
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(train_datagen.flow(x_train_combined, y_train_combined, batch_size=batch_size), epochs=epochs, validation_data=(x_test, y_test))

#%%
# Guardar el modelo
# model.save('NOMBRE_MODELO.h5')
