# Docker - Resolución Ejercicio 9 

Este proyecto corresponde a la resolución del ejercicio de Docker, donde se implementa un script en Python que procesa datos utilizando la librería pandas dentro de un contenedor. 

El objetivo es calcular el promedio de una serie de valores almacenados en un archivo CSV y guardar el resultado en un archivo de salida, utilizando volúmenes para persistir la información.

## Alumna
Ines Medina  
Carrera: Licenciatura en Ciencia de Datos  

---

## Estructura del Proyecto

- `proyecto/app/analisis.py` → Script principal en Python  
- `proyecto/data/datos.csv` → Archivo de entrada con los datos  
- `proyecto/output/` → Carpeta donde se genera el resultado  
- `proyecto/Dockerfile` → Configuración para construir la imagen  

---

## Requisitos

- Tener Docker instalado y funcionando

---

## Pasos para ejecutar

1. Posicionarse en la carpeta del proyecto:

```bash
cd proyecto
```
2. Construir la imgen de Docker:
```bash
docker build -t ejercicio-docker-imedina .
```
3. Correr el contenedor con volúmenes
```bash
docker run --rm -v "$(pwd)/data:/data" -v "$(pwd)/output:/output" ejercicio-docker-imedina
``` 
