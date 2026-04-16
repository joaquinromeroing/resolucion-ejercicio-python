# Ejercicio Docker (Ejercicio 9)

## Instrucciones

1. Crear una rama con la siguiente nomenclatura: docker-napellido  

2. Subir la rama al repositorio:  
```bash
git add .
git commit -m "Entrega ejercicio Docker"
git push origin nombre-de-la-rama
```

----------------------

# Resolución Ejercicio Docker - (Ejercicio 9)

En la carpeta `proyecto` se encuentra la implementación completa del ejercicio, junto con los archivos necesarios para construir la imagen, ejecutar el contenedor y verificar el resultado.


## Pasos para ejecutar

### 1. Entrar a la carpeta del proyecto

```bash
cd proyecto
```

### 2. Buildear la imagen

```bash
docker build -t ejercicio9-docker-salmiron .
```

### 3. Ejecutar el contenedor

```bash
docker run --rm -v "$(pwd)/output:/app/output" ejercicio9-docker-salmiron
```

### 4. Verificar el resultado

```bash
cat output/resultado.txt
```
