from algoritmos import burbuja, busqueda_binaria


MIN_VALOR = 1
MAX_VALOR = 100000


def cargar_numeros():
    Numeros = []
    print(f"Ingrese numeros enteros entre {MIN_VALOR} y {MAX_VALOR}. Ingrese 0 para finalizar.")
    while True:
        entrada = input("Numero: ").strip()
        try:
            valor = int(entrada)
        except ValueError:
            print("Error: debe ingresar un numero entero.")
            continue

        if valor == 0:
            break

        if valor < MIN_VALOR or valor > MAX_VALOR:
            print(f"Error: el numero debe estar entre {MIN_VALOR} y {MAX_VALOR}.")
            continue

        Numeros.append(valor)
    return Numeros


def pedir_numero_a_buscar():
    while True:
        entrada = input("Ingrese el numero a buscar: ").strip()
        try:
            return int(entrada)
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def main():
    Numeros = cargar_numeros()

    if not Numeros:
        print("No se cargaron numeros. Fin del programa.")
        return

    Numeros = burbuja(Numeros)
    print(f"Arreglo ordenado: {Numeros}")

    objetivo = pedir_numero_a_buscar()

    if busqueda_binaria(Numeros, objetivo):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()
