from __future__ import annotations

from typing import Iterable, List, Optional

RANGO_MINIMO = 1
RANGO_MAXIMO = 100000


def bubble_sort(numeros: List[int]) -> List[int]:
    """Ordena una lista de enteros usando el método burbuja."""
    ordenados = numeros[:]
    cantidad = len(ordenados)

    for i in range(cantidad):
        intercambiado = False
        for j in range(0, cantidad - i - 1):
            if ordenados[j] > ordenados[j + 1]:
                ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]
                intercambiado = True
        if not intercambiado:
            break

    return ordenados


def binary_search(numeros: List[int], objetivo: int) -> bool:
    """Busca un entero dentro de una lista ordenada usando búsqueda binaria."""
    inicio = 0
    fin = len(numeros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor = numeros[medio]

        if valor == objetivo:
            return True
        if valor < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False


def leer_numeros(input_func=input, print_func=print) -> List[int]:
    numeros: List[int] = []

    while True:
        try:
            texto = input_func("Ingrese un numero (0 para finalizar): ")
            numero = int(texto)
        except ValueError:
            print_func("Error: debe ingresar un numero entero valido.")
            continue

        if numero == 0:
            break

        if not RANGO_MINIMO <= numero <= RANGO_MAXIMO:
            print_func(f"Error: el numero debe estar entre {RANGO_MINIMO} y {RANGO_MAXIMO}.")
            continue

        numeros.append(numero)

    return numeros


def pedir_numero_a_buscar(input_func=input, print_func=print) -> int:
    while True:
        try:
            texto = input_func("Ingrese el numero a buscar: ")
            numero = int(texto)
        except ValueError:
            print_func("Error: debe ingresar un numero entero valido.")
            continue

        return numero


def ejecutar(input_func=input, print_func=print) -> None:
    numeros = leer_numeros(input_func=input_func, print_func=print_func)
    numeros = bubble_sort(numeros)
    numero_a_buscar = pedir_numero_a_buscar(input_func=input_func, print_func=print_func)

    if binary_search(numeros, numero_a_buscar):
        print_func("Numero encontrado")
    else:
        print_func("Numero no encontrado")


if __name__ == "__main__":
    ejecutar()
