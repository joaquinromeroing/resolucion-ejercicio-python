# Ejercicio 9: Docker

Este proyecto contiene la resolución del Ejercicio 9 de la práctica de Docker.

## Instrucciones para ejecutar el proyecto

Siga estos pasos detallados desde una terminal (WSL/Linux/PowerShell) dentro de la carpeta del proyecto:

### 1. Buildear la imagen de Docker

Este comando instalará las dependencias necesarias y preparará el entorno de ejecución.

```bash
docker build -t ejercicio9-docker .
```

### 2. Ejecución con volúmenes

```bash
docker run --name contenedor-ejercicio -v "$(pwd)/data:/data" -v "$(pwd)/output:/output" ejercicio9-docker
```

### 3. Verificación

Una vez finalizada la ejecución ("Análisis terminado"), podrá encontrar los archivos de salida en la carpeta local output/:

- temp_archivo_ordenado.csv: Dataset generado tras aplicar el algoritmo de ordenación.
- resultado.txt: Reporte detallado con los indicadores de ventas, unidades por producto, mayor/menor compra y totales generales.
