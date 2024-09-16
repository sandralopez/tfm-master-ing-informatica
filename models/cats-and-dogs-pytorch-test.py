#%%
import os
from PIL import Image
from torchvision import transforms
import torch

#%%
# Cargar y preprocesar la imagen
img_path = os.getenv('IMG_PATH')
img_width, img_height = 256, 256

image = Image.open(img_path)

# Al hacer resize, aplicar el mismo método de interpolación usado en TensorFlow
preprocess = transforms.Compose([
    transforms.Resize((img_height, img_width), interpolation=Image.NEAREST),
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

confidence, index = torch.max(output, dim=1)

index = index.item()

if index == 0:
    label = 'Gato'
else:
    label = 'Perro'
    
print(label)
print(confidence.item())
