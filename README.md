Ejercicio 9 Pasos a Seguir

Buildear la imagen: usar docker build -f DockerfileEj -t ejercicio-supermercado

Crear la carpeta del output: mkdir -p output

Correr el contenedor con volumen asociado: docker run -v "$(pwd)/output":/output ejercicio-supermercado

Y para verificar que se creo el archivo usar: cat output/salida.txt
