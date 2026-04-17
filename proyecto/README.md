# Ejercicio 9 - Docker


## Build de la imagen
sudo docker build -t ejercicio-9-docker .

## Ejecutar el contenedor ---> Desde la carpeta proyecto
sudo docker run -it -v "$(pwd)/data:/data" -v "$(pwd)/output:/output" ejercicio-9-docker

## Resultado ---> El archivo resultado.txt se genera en ---> proyecto/output/resultado.txt

## Contenido esperado ---> Promedio: 12.5

## Verificación
cat output/resultado.txt
