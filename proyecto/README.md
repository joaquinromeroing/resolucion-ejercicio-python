# Ejercicio 9 - Docker

## Estructura

proyecto/
├── data/
│   └── datos.csv
├── output/
├── app/
│   └── analisis.py
└── Dockerfile

## Descripción

Script en Python que lee un CSV con valores numéricos, calcula el promedio usando pandas y escribe el resultado en output/resultado.txt.

## Pasos para buildear y correr

cd proyecto

### 1. Buildear la imagen (desde la carpeta proyecto/)

docker build -t ejercicio9 .

### 2. Correr el contenedor con volumen

docker run --rm -v "$(pwd)/output:/output" ejercicio9

### 3. Verificar el resultado

cat output/resultado.txt

Deberías ver: Promedio: 12.5
