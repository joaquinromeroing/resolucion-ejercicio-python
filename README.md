# Resolución Ejercicio 9 - Docker

Este proyecto contiene la resolución del Ejercicio 9 de la práctica de Docker, donde se realiza un análisis de datos simple utilizando Python y Pandas dentro de un contenedor, con persistencia de resultados mediante volúmenes.

**Alumno:** Marcos Ziadi
**Carrera:** Licenciatura en Ciencia de Datos

## Estructura del Proyecto
- `app/`: Contiene el script `analisis.py`.
- `data/`: Contiene el archivo de entrada `datos.csv`.
- `output/`: Carpeta donde se generará el resultado del análisis.
- `Dockerfile`: Archivo de configuración para construir la imagen.

## Instrucciones para ejecutar

Para ejecutar este proyecto utilizando Docker, siga estos pasos desde la carpeta `proyecto`:

1. **Buildear la imagen:**
   ```bash
   docker build -t ejercicio-docker-ziadi .
   ```

2. **Correr el contenedor con volúmenes**   
   ```bash
   docker run --rm -v "$(pwd)/data:/data" -v "$(pwd)/output:/output" ejercicio-docker-ziadi
   ```
