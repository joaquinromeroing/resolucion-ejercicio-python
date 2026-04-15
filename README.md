# Ejercicio Docker

## Pasos para buildear y correr

1. Clonar el repositorio y pararse en esta rama:

   git clone https://github.com/joaquinromeroing/resolucion-ejercicio-python.git
   cd resolucion-ejercicio-python
   git checkout docker-egarcia

2. Buildear la imagen:

   docker build -t analisis-python .

3. Correr el contenedor con volumen:

   docker run --rm -v $(pwd)/output:/output analisis-python

4. Ver el resultado:

   cat output/resultado.txt
