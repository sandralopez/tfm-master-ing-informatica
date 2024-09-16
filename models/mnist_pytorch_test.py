#%%
import os
from PIL import Image
from torchvision import transforms
import torch

#%%
# Cargar y preprocesar la imagen
img_path = os.getenv('IMG_PATH')
img_width, img_height = 28, 28

image = Image.open(img_path)

# Al hacer resize, aplicar el mismo método de interpolación usado en TensorFlow
preprocess = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((img_width, img_height), interpolation=Image.NEAREST),
    transforms.ToTensor()
])

img_tensor = preprocess(image)
img_tensor = img_tensor.unsqueeze(0)

#%%
model = torch.load(os.getenv('MODEL_PATH'))
model.eval()

#%%
# Hacer la predicción
output = model(img_tensor)

_, predicted_class = torch.max(output, 1)

print(predicted_class.item())


