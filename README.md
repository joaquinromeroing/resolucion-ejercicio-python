# Ejercicio 9 - Dockerización y Volúmenes (wtejerina)

Este ejercicio consiste en la contenedorización de un script de Python que utiliza la librería `pandas` para procesar datos y devolver un resultado mediante el uso de volúmenes mapeados.

## 🚀 Estructura del Proyecto
- `/app`: Contiene el código fuente (`analisis.py`).
- `/data`: Carpeta de entrada para el archivo de datos (`datos.csv`).
- `/output`: Carpeta de salida donde se genera el archivo de resultados (`resultado.txt`).
- `Dockerfile`: Receta para construir la imagen con Python 3.9 y Pandas.

## 🛠️ Instrucciones de Ejecución

Para correr este proyecto en Windows (PowerShell), siga estos pasos:

Importante: Antes de comenzar, asegúrese de estar situado en la carpeta del proyecto:
```powershell
cd proyecto
```
### 1. Construir la Imagen
```powershell
docker build -t ejercicio9-wtejerina .

```
### 2. Ejecutar el Contenedor con Volúmenes
```
docker run --rm -v "${PWD}/data:/data" -v "${PWD}/output:/output" ejercicio9-wtejerina
```
### 3. Verificar Resultados
Una vez finalizado, podrá encontrar el archivo **resultado.txt** dentro de la carpeta local `output/`.