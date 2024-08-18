from tensorflow.keras.layers import Conv2D
from tf_explain.core.grad_cam import GradCAM
from .explainer_base import Explainer 
from PIL import Image
import io 
import base64

def explainer_grad_cam_tf_explain(explainer: Explainer):
	model = explainer.model 
	img = explainer.processed_image 
	label = explainer.extra_params["label_index"]

	# Obtener los layers convolucionales del modelo
	target_layers = []

	for layer in model.layers:
		if isinstance(layer, Conv2D):
			target_layers.append(layer.name)

	target_layer = target_layers[-1]

	# Aplicar la librería de explicabilidad
	explainer = GradCAM()

	grid = explainer.explain(([img], None), model, class_index=label, layer_name=target_layer)

	# Convertir a imagen
	image = Image.fromarray(grid)

	# Guardar la imagen en un objeto BytesIO
	buf = io.BytesIO()
	image.save(buf, format='JPEG')
	buf.seek(0)

	img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

	return img_base64