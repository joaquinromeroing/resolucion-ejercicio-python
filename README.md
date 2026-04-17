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

## Ejercicio Docker

La resolucion del ejercicio 9 esta en la carpeta [proyecto](./proyecto) y reutiliza el dataset del supermercado dentro de la estructura pedida:

```text
proyecto/
|-- app/
|   |-- analisis.py
|-- data/
|   |-- datos.csv
|-- output/
|   |-- .gitkeep
|-- Dockerfile
`-- requirements.txt
```

El script usa `pandas` para leer el CSV, calcular los totales del ejercicio y grabar el resultado en `resultado.txt`.
La rama preparada para esta entrega es `docker-sanfilippo`.

### Build de la imagen

Desde la raiz del repo:

```powershell
docker build -t docker-sanfilippo ./proyecto
```

### Correr el contenedor con volumenes

El siguiente comando monta la carpeta local de datos en `/data` y la carpeta local de salida en `/output`:

```powershell
docker run --rm `
  -v "$(Resolve-Path .\proyecto\data):/data:ro" `
  -v "$(Resolve-Path .\proyecto\output):/output" `
  docker-sanfilippo
```

### Verificar el resultado

Cuando termine la ejecucion, el archivo queda en la carpeta local `proyecto/output`.

```powershell
Get-Content "$(Resolve-Path .\proyecto\output\resultado.txt)"
```
