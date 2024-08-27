from setuptools import setup, find_packages

setup(
    name="explainer_lib",
    version="0.1.0",
    description="An internal library to run other libraries of explainability techniques on convolutional neural network models",
    packages=find_packages(),
    install_requires=[ 
        "numpy",
        "torch",
        "tensorflow",
        "Pillow",
        "tf-explain",
        "grad-cam"
    ],
    python_requires='>=3.10',
)
