from ejercicio_busqueda_binaria.algoritmos import ordenar_burbuja, busqueda_binaria


def cargar_numeros():
    Numeros = []

    while True:
        numero = int(input("Ingrese un número entero entre 1 y 100000. Ingrese 0 para finalizar: "))

        if numero == 0:
            break

        if numero < 1 or numero > 100000:
            print("Error: el número debe estar entre 1 y 100000.")
        else:
            Numeros.append(numero)

    return Numeros


def main():
    Numeros = cargar_numeros()

    Numeros = ordenar_burbuja(Numeros)

    print("Números ordenados:", Numeros)

    numero_buscado = int(input("Ingrese un número a buscar: "))

    encontrado = busqueda_binaria(Numeros, numero_buscado)

    if encontrado:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()