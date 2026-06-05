#!/usr/bin/env python3

def burbuja(arr: list[int]) -> list[int]:
    resultado = arr[:]
    n = len(resultado)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    return resultado


def busqueda_binaria(arr: list[int], objetivo: int) -> int:
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def cargar_numeros() -> list[int]:
    numeros: list[int] = []
    print("Ingrese números enteros entre 1 y 100000.")
    print("Ingrese 0 para finalizar.\n")

    while True:
        entrada = input("Número: ").strip()
        try:
            valor = int(entrada)
        except ValueError:
            print("  Error: ingrese un número entero válido.\n")
            continue

        if valor == 0:
            break
        elif 1 <= valor <= 100000:
            numeros.append(valor)
        else:
            print(f"  Error: {valor} está fuera del rango permitido (1–100000).\n")

    return numeros


def main() -> None:
    Numeros = cargar_numeros()
    
    if not Numeros:
        print("\nNo se ingresaron números. Fin del programa.")
        return

    print(f"\nNúmeros ingresados : {Numeros}")

    Numeros = burbuja(Numeros)
    print(f"Arreglo ordenado   : {Numeros}")

    while True:
        entrada = input("\nIngrese el número a buscar: ").strip()
        try:
            objetivo = int(entrada)
            break
        except ValueError:
            print("  Error: ingrese un número entero válido.")

    indice = busqueda_binaria(Numeros, objetivo)

    if indice != -1:
        print(f"\nNumero encontrado (posición {indice} del arreglo ordenado).")
    else:
        print("\nNumero no encontrado.")

if __name__ == "__main__":
    main()