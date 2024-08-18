import io
from PIL import Image
from .explainer_base import Explainer 
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
import torch.nn as nn
import base64

def explainer_grad_cam_pytorch_grad_cam(explainer: Explainer):
    model = explainer.model 
    img = explainer.processed_image 
    rgb_img = explainer.extra_params['rgb_image']
    
    # Obtener los layers convolucionales del modelo
    target_layers = []

    for name, module in model.named_modules():
        if isinstance(module, nn.Conv2d):
            target_layers.append(model._modules.get(name))

    # Aplicar la librería de explicabilidad
    cam = GradCAM(model=model, target_layers=target_layers)

    grayscale_cam = cam(input_tensor=img, targets=None)
    grayscale_cam = grayscale_cam[0, :]

    cam_image = show_cam_on_image(rgb_img, grayscale_cam)

    # Convertir a imagen
    image = Image.fromarray(cam_image)

    # Guardar la imagen en un objeto BytesIO
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    buf.seek(0)

    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return img_base64
    