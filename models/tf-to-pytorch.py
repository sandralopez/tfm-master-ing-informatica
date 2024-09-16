import os
import tensorflow as tf
import tf2onnx
import torch
from onnx2pytorch import ConvertModel

#%%
# Cargar el modelo TensorFlow
model = tf.keras.models.load_model(os.getenv('TF_MODEL_PATH'))

#%%
# Convertir a ONNX
onnx_model, _ = tf2onnx.convert.from_keras(model)

#%%
# Convertir a PyTorch
pytorch_model = ConvertModel(onnx_model)

#%%
# Guardar el modelo PyTorch
torch.save(pytorch_model, os.getenv('PYTORCH_MODEL_PATH'))