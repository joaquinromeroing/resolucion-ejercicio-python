# Ejercicio Docker (Ejercicio 9)

## Instrucciones

1. Crear una rama con la siguiente nomenclatura: docker-napellido  

2. Subir la rama al repositorio:  
```bash
git add .
git commit -m "Entrega ejercicio Docker"
git push origin nombre-de-la-rama
```

# Ejercicio Docker

## Importante

Para construir la imagen y correr el contenedor, primero hay que pararse en la **raíz del repositorio**, es decir, en la carpeta donde están el archivo `Dockerfile`.

## Pasos para ejecutar

### 1. Pararse en la carpeta `proyecto`, dentro del repositorio, ya que allí se encuentra el archivo `Dockerfile`.

```bash
cd resolucion-ejercicio-python/proyecto
```

### 2. Construir la imagen

```bash
docker build -t ejercicio9-btorregiani .
```

### 3. Ejecutar el contenedor

```bash
docker run --rm -v "$(pwd)/data:/data" -v "$(pwd)/output:/output" ejercicio9-btorregiani
```

## Ver el resultado

```bash
cat output/resultado.txt
```

## Resultado esperado

```text
Promedio: 12.5
```