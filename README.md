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

## Pasos para buildear y correr el Docker

1. Moverse a la carpeta del docker:

```bash
cd resolucion-ejercicio-python/proyecto
```

2. Buildear la imagen
Desde la terminal, situado en la raíz del proyecto, ejecute:

```bash
docker build -t ejercicio9-smalatini .
```

3. Ejecutar el contenedor:

```bash
docker run ejercicio9-smalatini
```