# Resolución Ejercicio 9 - Docker

## Estructura del proyecto

licenciatura-cdallago/

data/
datos.csv

output/

app/
analisis.py

Dockerfile
requirements.txt

## Descripción

Este proyecto utiliza Docker para ejecutar un script de Python que calcula el promedio de valores contenidos en un archivo CSV.

El script lee los datos desde la carpeta `data` y guarda el resultado en la carpeta `output`.

## Construir la imagen Docker

Desde la carpeta del proyecto ejecutar:

docker build -t analisis-python .

## Ejecutar el contenedor

docker run -v "$(pwd)/data:/data" -v "$(pwd)/output:/output" analisis-python

## Resultado

El contenedor ejecuta el script `analisis.py` y genera el archivo:

output/resultado.txt

con el promedio de los valores del archivo CSV.
