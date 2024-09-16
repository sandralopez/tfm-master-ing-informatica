# Importación de librerías
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalMaxPooling2D
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.models import Sequential
import tensorflow as tf
from tensorflow.keras import layers

# Rutas a los directorios de training y de test
train_dir = os.getenv('TRAIN_DIR')
test_dir = os.getenv('TEST_DIR')

#%%
# Parámetros
img_width, img_height = 224, 224
batch_size = 64

# Preprocesamiento
train_datagen = ImageDataGenerator(dtype = 'float32', preprocessing_function=preprocess_input)
test_datagen = ImageDataGenerator(dtype = 'float32', preprocessing_function=preprocess_input)

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

#%%
# Modelo (basado en Resnet50)
inp = layers.Input(shape=(img_width, img_height, 3))

base_model = ResNet50(include_top=False, weights='imagenet', input_tensor=inp, input_shape=(img_width, img_height, 3))

prediction = layers.Dense(2, activation='softmax', name='output')

global_mac_pooling = tf.keras.layers.GlobalMaxPooling2D()

conv5_block3_out = base_model.get_layer('conv5_block3_out')
x = global_mac_pooling(conv5_block3_out.output)
x = prediction(x)

model = tf.keras.models.Model(inputs = inp, outputs = x)

for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

#%%
# Entrenamiento
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,
    validation_data=test_generator,
    validation_steps=test_generator.samples // test_generator.batch_size
)

#%%
# Guardado del modelo
# model.save('nombre-modelo.h5')