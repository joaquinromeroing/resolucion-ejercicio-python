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

## Cómo ejecutar el proyecto en otra PC

### Requisitos
Tener instalado:

- Docker Desktop en Windows
- WSL habilitado si se va a usar desde Ubuntu/WSL
- Git para clonar el repositorio

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>

El proyecto debe tener esta estructura:

proyecto/
├── data/
│   └── datos.csv
├── output/
├── app/
│   └── analisis.py
└── Dockerfile


1. docker build -t analisis-promedio .
2. docker run --rm -v "$(pwd)/data:/data" -v "$(pwd)/output:/output" analisis-promedio
3. cat output/resultado.txt

Si sale Promedio: 12.5 esta correcto
