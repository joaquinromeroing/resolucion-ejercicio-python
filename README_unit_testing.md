# Ejercicio Unit Testing - Supermercado

Modularización del ejercicio del supermercado en funciones, con unit tests usando pytest.

## Estructura

- `main.py` — funciones del programa (carga de CSV, ordenamiento burbuja, procesamiento de sucursales).
- `test_main.py` — unit tests de las funciones de lógica (`ordenar_burbuja` y `procesar_sucursal`).

## Cómo correr el proyecto

### 1. Crear y activar el entorno virtual

```bash
python3 -m venv myfirstproject
source myfirstproject/Scripts/activate   # Windows (Git Bash)
# source myfirstproject/bin/activate     # Linux / Mac
```

### 2. Instalar dependencias

```bash
pip install pytest pytest-mock
```

### 3. Ejecutar los tests

```bash
pytest
```

### 4. Ejecutar el programa

```bash
python main.py
```