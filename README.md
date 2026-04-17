# Ejercicio Docker: build y ejecución

## 1) Build de la imagen

```bash
docker build -t ejercicio-analisis .
```

## 2) Ejecutar el contenedor con volúmenes

```bash
docker run --rm \
  -v "$(pwd)/data:/data" \
  -v "$(pwd)/output:/output" \
  ejercicio-analisis
```