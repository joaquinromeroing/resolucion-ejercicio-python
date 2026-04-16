
# Ejercicio Docker (Ejercicio 9)

## Rama
docker-vmarull

## Estructura

proyecto/
- app/analisis.py
- data/datos.csv
- output/
- Dockerfile

## Libreria
Se usa pandas para calcular el promedio.

## Build

docker build -t ejercicio9-docker proyecto

## Run

docker run --rm -v "$(pwd)/proyecto/output:/output" ejercicio9-docker

## Resultado

se genera:
proyecto/output/resultado.txt

contenido:
promedio: 12.5
