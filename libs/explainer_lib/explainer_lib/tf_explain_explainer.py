import io 
import base64
import cv2
from tensorflow.keras.layers import Conv2D
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
		last_conv_layer_name = 'conv5_block3_out'
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

	grid = explainer.explain(([img], None), model, class_index=label_index, layer_name=last_conv_layer_name, colormap=cv2.COLORMAP_JET)

	# Convertir a imagen
	image = Image.fromarray(grid)

	# Guardar la imagen en formato jpeg y convertir a base64
	buf = io.BytesIO()
	image.save(buf, format='JPEG')
	buf.seek(0)

	img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

	return img_base64
