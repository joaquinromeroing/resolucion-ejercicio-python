## Ejercicio 9 - Dockerfile + Volúmenes

### Requisitos
- Docker instalado

### Pasos para buildear y correr

**1. Buildear la imagen:**
```bash
docker build -t ejercicio9 .
```

**2. Correr el contenedor con volumen:**
```bash
docker run --rm -v "$(pwd)/output":/output ejercicio9
```

**3. Ver el resultado:**
```bash
cat output/resultado.txt
```
El archivo `resultado.txt` aparecerá en la carpeta `output/` local con el promedio calculado. 