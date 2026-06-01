def burbuja(numeros):
    n = len(numeros)

    for i in range(n):
        for j in range(0, n - i - 1):

            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    return numeros


def busqueda_binaria(numeros, objetivo):

    izquierda = 0
    derecha = len(numeros) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if numeros[medio] == objetivo:
            return True

        elif numeros[medio] < objetivo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return False


def main():

    numeros = []

    while True:

        numero = int(input("Ingrese un número (0 para terminar): "))

        if numero == 0:
            break

        if numero < 1 or numero > 100000:
            print("Error. Debe ingresar un número entre 1 y 100000.")
            continue

        numeros.append(numero)

    burbuja(numeros)

    print("Lista ordenada:")
    print(numeros)

    buscar = int(input("Ingrese número a buscar: "))

    if busqueda_binaria(numeros, buscar):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()