# TFM - Máster en Ingeniería Informática - Universidad de Burgos

# Clasificación de imágenes y explicabilidad

## Descripción del Proyecto

Este proyecto consiste en una página web que permite ejecutar unos modelos de clasificación establecidos basados en redes neuronales convolucionales y aplicar explicabilidad utilizando bibliotecas de explicabilidad ya existentes. Para ello, permite seleccionar entre una serie de modelos y dos bibliotecas de explicabilidad y las aplica a una imagen de entrada. En resumen, el sistema combina tanto la aplicación del modelo de clasificación como la aplicación de explicabilidad. 

Actualmente se han disponibilizado 5 modelos y dos bibliotecas de explicabilidad. 

## Arquitectura

La aplicación estará dividida en varios componentes clave:
- **Frontend (Next.js):** Interfaz de usuario para subir imágenes, seleccionar modelos y bibliotecas y visualizar resultados.
- **Microservicio bff (orquestación) (Fastapi):**  Se comunica directamente con el frontend. Recibe todas las peticiones, las deriva al microservicio correspondiente y devuelve los resultados al frontend. 
- **Microservicios de modelo y explicabilidad (Fastapi):** Cada uno dedicado a un modelo específico de clasificación de imágenes. Aplica la predicción y la biblioteca de explicabilidad seleccionada por el usuario. 
- **Biblioteca para aplicación de bibliotecas de explicabilidad:** Es importada en cada uno de los microservicios de modelo y explicabilidad. Ofrece una intefaz común para la llamada a la función Grad-CAM de las biblitoecas de explicabilidad disponibles. 

## Instalación

### Prerrequisitos

- Git (para la descarga de las fuentes del proyecto)
- [Docker](https://www.docker.com/) (Para el despliegue de los componentes de la aplicación)
- [Docker-compose](https://docs.docker.com/compose/) (Para la orquestación de los componentes de la aplicación)
- [Python](https://www.python.org/) (Para los microservicios backend. Para la ejecución local se pueden utilizar las imágenes Docker disponibles en el proyecto con algunas modificaciones para cargar las fuentes como un volumen, o bien generar un entorno en Miniconda)

### Ejecución local del proyecto

Para la ejecución local del proyecto en primer lugar se debe clonar el repositorio
```
git clone https://github.com/sandralopez/tfm-master-ing-informatica.git
```

Para crear un entorno en Miniconda:
```
conda create --name <nombre_entorno> python=3.9
conda activate <nombre_entorno>
```

Instalar las dependencias del proyecto:
```
conda install requeriments.txt
```

Lanzar los servicios del proyecto: 
```
uvicorn app.main:app --host 0.0.0.0 --port <puerto> --reload
```

Ejecución del frontend: 
```
npm run dev
```

#### A tener en cuenta: 

Es muy importante configurar 
- Los archivos .env de los servicios, 
- El archivo .env del frontend
- El archivo config.json del servicio bff.

### Despliegue del proyecto

En el respositorio se dispone de varios archivos Dockerfile, un docker-compose-example.yaml y el archivo requeriments.txt para facilitar el despliegue mediante el uso de Docker.

### Seguimiento del proyecto

Puedes seguir el desarrollo del proyecto en el tablero creado en [Github Projects](https://github.com/users/sandralopez/projects/4) 

### Bibliotecas de explicabilidad

Gildenblat, J. (2021). pytorch-grad-cam. Repositorio de Github. Recuperado de: https://github.com/jacobgil/pytorch-grad-cam

Meudec, R. (2021). tf-explain. Repositorio de Github. Recuperado de:  https://github.com/sicara/tf-explain

