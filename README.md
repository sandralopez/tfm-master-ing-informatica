# TFM - Máster en Ingeniería Informática - Universidad de Burgos

# Clasificación de imágenes y explicabilidad

## Descripción del Proyecto

Este proyecto consistirá en una página web para la clasificación de imágenes y aplicación de librerías de interpretabilidad orientadas a explicar los resultados obtenidos a través de los modelos. 

Los usuarios podrán enviar imágenes, seleccionar entre varios modelos de clasificación entrenados y aplicar diferentes librerías de explicabilidad para obtener resultados y análisis de forma sencilla e intuitiva. En su etapa inicial se tendrán disponibles dos modelos.

La arquitectura estará basada en microservicios para garantizar una fácil mantenibilidad y flexibilidad.

## Arquitectura

La aplicación estará dividida en varios componentes clave:
- **Frontend (Next.js):** Interfaz de usuario para subir imágenes, seleccionar modelos y librerías y visualizar resultados.
- **Servicio de Orquestación:** Manejará la recepción de imágenes y la coordinación entre microservicios.
- **Microservicios de Modelos:** Cada uno dedicado a un modelo específico de clasificación de imágenes.
- **Microservicios de Librerías de Interpretabilidad:** Encargados de aplicar diferentes librerías de interpretabilidad para proveer de explicabilidad a los resultados.

## Instalación

### Prerrequisitos
- [Docker](https://www.docker.com/) (para el despliegue de los componentes de la aplicación)
- [Python](https://www.python.org/) (para microservicios backend)

### Seguimiento del proyecto
Puedes seguir el desarrollo del proyecto en el tablero creado en [Github Projects](https://github.com/users/sandralopez/projects/4) 