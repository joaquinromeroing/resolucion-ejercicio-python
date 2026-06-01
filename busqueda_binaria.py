def ordenar_burbuja(numeros):
    numeros = numeros.copy()

    for i in range(len(numeros) - 1):
        for j in range(len(numeros) - 1 - i):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    return numeros


def busqueda_binaria(numeros, buscado):
    inicio = 0
    fin = len(numeros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if numeros[medio] == buscado:
            return True
        elif buscado < numeros[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return False


def cargar_numeros():
    Numeros = []

    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 100000, o 0 para finalizar: "))
        except ValueError:
            print("Error: debe ingresar un número entero")
            continue

        if numero == 0:
            break

        if numero < 1 or numero > 100000:
            print("Error: el número debe estar entre 1 y 100000")
            continue

        Numeros.append(numero)

    return Numeros


def main():
    Numeros = cargar_numeros()

    Numeros = ordenar_burbuja(Numeros)

    print("Numeros ordenados:", Numeros)

    try:
        numero_buscado = int(input("Ingrese el número a buscar: "))
    except ValueError:
        print("Error: debe ingresar un número entero")
        return

    if busqueda_binaria(Numeros, numero_buscado):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()