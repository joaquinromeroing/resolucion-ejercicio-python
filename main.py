def burbuja(numeros):
    n = len(numeros)

    for i in range(n):
        for j in range(0, n - i - 1):
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
        elif numeros[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False


def main():
    Numeros = []

    while True:
        numero = int(
            input("Ingrese un número entre 1 y 100000 (0 para finalizar): ")
        )

        if numero == 0:
            break

        if numero < 1 or numero > 100000:
            print("Error: el número debe estar entre 1 y 100000")
        else:
            Numeros.append(numero)

    burbuja(Numeros)

    print("Números ordenados:", Numeros)

    buscado = int(input("Ingrese el número a buscar: "))

    if busqueda_binaria(Numeros, buscado):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()