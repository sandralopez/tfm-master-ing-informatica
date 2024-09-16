import torch

def load_model(model_path: str):
    model = torch.load(model_path)

    return model
