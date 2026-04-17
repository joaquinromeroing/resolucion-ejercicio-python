# Ejercicio Python

**Objetivo:** Entregar el ejercicio como una rama en este repositorio.  

https://github.com/joaquinromeroing/resolucion-ejercicio-python

## Instrucciones

1. Crear una rama con la siguiente nomenclatura: carrera-napellido  
    Ejemplo:  
            a. tecnicatura-jromero  
            b. licenciatura-gmazzaglia  

2. Subir la rama al repositorio:  
```bash
git add .
git commit -m "Entrega ejercicio Python"
git push origin nombre-de-la-rama
```

Para ejecutar el ejercicio:

1. Buildear la imagen:
```bash
cd proyecto
docker build -t docker-ej9 .
```

2. Ejecutar el contenedor con volumen
```bash
docker run --name Docker-Ej9 -v "$(pwd)/output:/output" docker-ej9
```
