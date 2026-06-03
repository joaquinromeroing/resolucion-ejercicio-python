#!/usr/bin/env python3
"""
Algoritmo de ordenamiento Burbuja y Búsqueda Binaria sobre arreglo de enteros.

Autor: Benjamin Juan Miles Rouillon
"""


def cargar_numeros():
    """
    Solicita al usuario ingresar números enteros en el rango 1-100000.
    El ingreso finaliza cuando el usuario ingresa 0.
    Retorna una lista con los números válidos ingresados.
    """
    numeros = []
    while True:
        entrada = input("Ingrese un número (0 para finalizar): ")
        try:
            numero = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

        if numero == 0:
            break
        elif 1 <= numero <= 100000:
            numeros.append(numero)
        else:
            print(f"Error: el número debe estar entre 1 y 100000.")

    return numeros


def ordenamiento_burbuja(numeros):
    """
    Ordena una lista de enteros de menor a mayor usando el método Burbuja.
    No modifica la lista original; retorna una nueva lista ordenada.
    """
    arreglo = numeros[:]
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo


def busqueda_binaria(numeros, objetivo):
    """
    Busca un número entero en una lista ordenada usando Búsqueda Binaria.
    Retorna el índice donde se encontró el número, o -1 si no existe.
    La lista debe estar ordenada de menor a mayor.
    """
    izquierda = 0
    derecha = len(numeros) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if numeros[medio] == objetivo:
            return medio
        elif numeros[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def main():
    print("Carga de números (ingrese 0 para finalizar):")
    numeros = cargar_numeros()

    if not numeros:
        print("No se ingresaron números.")
        return

    numeros_ordenados = ordenamiento_burbuja(numeros)
    print(f"\nArreglo ordenado: {numeros_ordenados}")

    entrada = input("\nIngrese el número a buscar: ")
    try:
        objetivo = int(entrada)
    except ValueError:
        print("Error: debe ingresar un número entero.")
        return

    indice = busqueda_binaria(numeros_ordenados, objetivo)

    if indice != -1:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()
