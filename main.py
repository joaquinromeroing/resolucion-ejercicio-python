from busqueda_binaria import burbuja, busqueda_binaria


def cargar_numeros():
    numeros = []
    print("Ingrese números entre 1 y 100000. Ingrese 0 para finalizar.\n")

    while True:
        entrada = input("Ingrese un número: ")

        if not entrada.lstrip('-').isdigit():
            print("  Error: debe ingresar un número entero.\n")
            continue

        numero = int(entrada)

        if numero == 0:
            break

        if numero < 1 or numero > 100000:
            print(f"  Error: {numero} está fuera del rango (1 a 100000).\n")
            continue

        numeros.append(numero)
        print(f"  ✓ Número {numero} agregado.\n")

    return numeros


def main():
    numeros = cargar_numeros()

    if len(numeros) == 0:
        print("No se ingresaron números. Fin del programa.")
        return

    print(f"\nNúmeros ingresados: {numeros}")

    numeros = burbuja(numeros)
    print(f"Números ordenados:  {numeros}")

    entrada = input("\nIngrese el número a buscar: ")

    if not entrada.lstrip('-').isdigit():
        print("Entrada inválida.")
        return

    objetivo = int(entrada)
    resultado = busqueda_binaria(numeros, objetivo)

    if resultado != -1:
        print(f"\nNumero encontrado (posición {resultado})")
    else:
        print("\nNumero no encontrado")


if __name__ == "__main__":
    main()