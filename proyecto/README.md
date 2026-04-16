# Ejercicio 9 - Docker


## Build de la imagen

sudo docker build -t ejercicio-9-docker .


## Run del contenedor

sudo docker run -it -v $(pwd)/data:/data -v $(pwd)/output:/output ejercicio-9-docker


## Resultado

El archivo resultado.txt se genera en:

proyecto/output/resultado.txt

Contenido esperado:

Promedio: 12.5
