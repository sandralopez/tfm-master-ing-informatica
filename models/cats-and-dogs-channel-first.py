# Importación de librerías
import tensorflow as tf
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Rutas a los directorios de training y de test
train_dir = os.getenv('TRAIN_DIR')
test_dir = os.getenv('TEST_DIR')

#%%
# Conversión a channel-first para posterior transformación a modelo Pytorch
class ChannelFirstDataGenerator:
    def __init__(self, generator):
        self.generator = generator
        self.samples = generator.samples
        self.batch_size = generator.batch_size
        self.class_indices = generator.class_indices
        self.num_classes = generator.num_classes
        self.target_size = generator.target_size
        self.data_format = 'channels_first'

    def __len__(self):
        return len(self.generator)

    def __iter__(self):
        return self

    def __next__(self):
        images, labels = next(self.generator)
        
        images = np.transpose(images, (0, 3, 1, 2))  # De [B, H, W, C] a [B, C, H, W]
        
        return images, labels

#%%
# Parámetros
img_width, img_height = 256, 256
batch_size = 64

# Definir data augmentation para train
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    horizontal_flip=True,
    rotation_range=40,
    zoom_range=0.1,
    shear_range=0.2
)

# Definir normalización
test_datagen = ImageDataGenerator(
    rescale=1.0/255,
)

# Generadores de datos
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

train_generator = ChannelFirstDataGenerator(train_generator)
test_generator = ChannelFirstDataGenerator(test_generator)

#%%
images, labels = next(train_generator)

#%%
# Modelo
model = tf.keras.models.Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(3, img_width, img_height), data_format='channels_first'),
    MaxPooling2D(pool_size=(2, 2), data_format='channels_first'),
    Conv2D(64, (3, 3), activation='relu', data_format='channels_first'),
    MaxPooling2D(pool_size=(2, 2), data_format='channels_first'),
    Conv2D(128, (3, 3), activation='relu', data_format='channels_first'),
    MaxPooling2D(pool_size=(2, 2), data_format='channels_first'),
    Conv2D(256, (3, 3), activation='relu', data_format='channels_first'),
    MaxPooling2D(pool_size=(2, 2), data_format='channels_first'),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')
])

# Resumen del modelo
model.summary()
#%%
# Compilación del modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenamiento
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=20,
    validation_data=test_generator,
    validation_steps=test_generator.samples // test_generator.batch_size
)

#%%
# Guardado del modelo
# model.save('nombre-modelo.h5')