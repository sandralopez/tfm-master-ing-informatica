import io 
import base64
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, GlobalMaxPooling2D, Conv2D
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.applications import ResNet50
from PIL import Image
from tf_explain.core.grad_cam import GradCAM
from .explainer_base import Explainer
from .constants import CUSTOM_MODEL, RESNET_50

def explainer_grad_cam_tf_explain(explainer: Explainer):
	model = explainer.model 
	img = explainer.processed_image 
	label_index = explainer.extra_params["label_index"]
	model_type = explainer.extra_params["model_type"]

	# Obtener la última capa convolucional del modelo
	if model_type == RESNET_50:
		resnet50_model = model.get_layer("resnet50")
		resnet50_input = resnet50_model.input

		# Obtener la última capa convolucional de Resnet50
		last_conv_layer = resnet50_model.get_layer("conv5_block3_out").output

		# Crear un modelo que tenga como salida la última capa convolucional
		# Esto lo utilizaremos para poder utilizar su última capa para explain
		conv_model = Model(inputs=resnet50_input, outputs=last_conv_layer)

		last_conv_layer_name = 'conv5_block3_out'

		model = conv_model
	elif model_type == CUSTOM_MODEL:
		conv_layers = []

		for layer in model.layers:
			if isinstance(layer, Conv2D):
				conv_layers.append(layer.name)

		last_conv_layer_name = conv_layers[-1]
	else:
		return None

	# Aplicar la librería de explicabilidad
	explainer = GradCAM()

	grid = explainer.explain(([img], None), model, class_index=label_index, layer_name=last_conv_layer_name)

	# Convertir a imagen
	image = Image.fromarray(grid)

	# Guardar la imagen en formato jpeg y convertir a base64
	buf = io.BytesIO()
	image.save(buf, format='JPEG')
	buf.seek(0)

	img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

	return img_base64
