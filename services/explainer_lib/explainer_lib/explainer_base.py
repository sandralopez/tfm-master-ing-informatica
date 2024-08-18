from typing import Dict, Any
import numpy as np 

class Explainer:
    def __init__(self, library_name: str, model: Any, processed_image: np.ndarray, extra_params: Dict[str, Any] = None):
        self.library_name = library_name.lower()
        self.model = model
        self.processed_image = processed_image
        self.extra_params = extra_params if extra_params is not None else {}

    def explain(self):
        if self.library_name == 'tf-explain':
            from .tf_explain_explainer import explainer_grad_cam_tf_explain
            return explainer_grad_cam_tf_explain(self)
        elif self.library_name == 'pytorch-grad-cam':
            from .torch_grad_cam_explainer import explainer_grad_cam_pytorch_grad_cam
            return explainer_grad_cam_pytorch_grad_cam(self)
        else:
            raise ValueError(f"Librería de explicabilidad '{self.library_name}' no soportada.")

