# Ejercicio Python

**Objetivo:** Entregar el ejercicio como una rama en este repositorio.  

https://github.com/joaquinromeroing/resolucion-ejercicio-python

---

## Enunciado

Desarrollar un algoritmo que permita ingresar números enteros por teclado.

El algoritmo debe cumplir con los siguientes requisitos:

1. Solicitar al usuario el ingreso de números.
2. Cada número ingresado debe estar dentro del rango **1 a 100000**.
3. Si el usuario ingresa un valor fuera de ese rango, excepto el cero, se debe informar el error y solicitar un nuevo número.
4. El proceso de carga finaliza cuando el usuario ingresa el valor **0**.
5. Cada número válido ingresado debe almacenarse en un arreglo llamado **Numeros**.
6. Luego, ordenar los números ingresados utilizando el método de ordenamiento **Burbuja**.
7. Una vez ordenado el arreglo, solicitar al usuario que ingrese un número a buscar.
8. Buscar dicho número dentro del arreglo **Numeros** utilizando el algoritmo de **Búsqueda Binaria**.
9. Si el número existe en el arreglo, mostrar el mensaje: **"Numero encontrado"**
10. Si el número no existe en el arreglo, mostrar el mensaje: **"Numero no encontrado"**
11. Realizar **unit testing** sobre las funciones de ordenamiento y búsqueda, verificando el correcto funcionamiento del método Burbuja y de la Búsqueda Binaria.

---

## Estructura del proyecto

```
.
├── app/
│   ├── algorithms.py   # Implementación de Burbuja y Búsqueda Binaria
│   └── main.py         # Programa principal (entrada/salida por consola)
└── tests/
    └── test_algorithms.py  # Unit tests con pytest (18 casos)
```

## Cómo ejecutar

```bash
# Programa principal
python3 app/main.py

# Tests
python3 -m pytest tests/ -v
```

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