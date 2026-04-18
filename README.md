# Guía de Ejecución (Docker)

Para buildear la imagen y correr el contenedor verificando los resultados.

### 1. Buildear la imagen ###
Ejecute el siguiente comando para generar la imagen local:

```bash
docker build -t mi-proyecto-python . 


# 2. Correr el contenedor #

```bash
 docker run --rm --name entrega-final -v "$(pwd)/output:/app/output" mi-proyecto-python

