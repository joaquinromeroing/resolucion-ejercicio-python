# Ejercicio 9 - Docker

## Pasos para correr el proyecto

1. Clonar el repositorio y entrar a la carpeta
git clone https://github.com/joaquinromeroing/resolucion-ejercicio-python.git
cd resolucion-ejercicio-python

2. Pararse en la rama
git checkout docker-nyema

3. Buildear la imagen
docker build -t imagen-analisis .

4. Correr el contenedor
docker run -v $(pwd)/output:/output imagen-analisis

5. Ver el resultado
cat output/resultado.txt
