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
## Resolución Ejercicio 9 - Docker

### Estructura utilizada

- `data/datos.csv`
- `app/analisis.py`
- `output/`
- `Dockerfile`

### Build de la imagen

```bash
sudo docker build -t ejercicio9 .
