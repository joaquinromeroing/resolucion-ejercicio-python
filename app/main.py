from algorithms import ordenamiento_burbuja, busqueda_binaria


def principal():
    numeros = []

    print("Ingrese numeros enteros del 1 al 100000. Ingrese 0 para finalizar.")

    while True:
        entrada = input("Ingrese un numero: ")

        try:
            numero = int(entrada)
        except ValueError:
            print("Error: ingrese un numero entero valido.")
            continue

        if numero == 0:
            break
        elif numero < 1 or numero > 100000:
            print("Error: el numero debe estar entre 1 y 100000.")
        else:
            numeros.append(numero)

    if not numeros:
        print("No se ingresaron numeros.")
        return

    ordenamiento_burbuja(numeros)
    print(f"\nNumeros ordenados: {numeros}")

    try:
        objetivo = int(input("\nIngrese el numero a buscar: "))
    except ValueError:
        print("Error: ingrese un numero entero valido.")
        return

    resultado = busqueda_binaria(numeros, objetivo)

    if resultado != -1:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    principal()
