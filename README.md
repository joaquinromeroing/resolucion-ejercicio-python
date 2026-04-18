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


----------------------

# Ejercicio Docker (Ejercicio 9)

## Instrucciones

1. Crear una rama con la siguiente nomenclatura: docker-napellido  

2. Subir la rama al repositorio:  
```bash
git add .
git commit -m "Entrega ejercicio Docker"
git push origin nombre-de-la-rama
```

## Instrucciones para ejecutar el ejercicio:

1. Pararse en la carpeta del ejercicio.
```bash
cd proyecto
```

2. Buildear la imagen.
```bash
docker build -t docker_ej09 .
```

3. Correr el contenedor con volumen.
```bash
docker run -v $(pwd)/output:/output docker_ej09
```

4. Ver el resultado.
```bash
cat output/resultado.txt
```
