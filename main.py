def cargar_numeros():

    numeros = []

    while True:

        numero = int(input("Ingrese un numero (0 para finalizar): "))

        if numero == 0:
            break

        if 1 <= numero <= 100000:
            numeros.append(numero)
        else:
            print("Error: el numero debe estar entre 1 y 100000")

    return numeros


def burbuja(numeros):

    n = len(numeros)

    for i in range(n):

        for j in range(0, n - i - 1):

            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    return numeros


def busqueda_binaria(numeros, buscado):

    izquierda = 0
    derecha = len(numeros) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if numeros[medio] == buscado:
            return True

        elif buscado < numeros[medio]:
            derecha = medio - 1

        else:
            izquierda = medio + 1

    return False

def main():

    numeros = cargar_numeros()

    burbuja(numeros)

    numero_buscado = int(input("Ingrese el numero a buscar: "))

    if busqueda_binaria(numeros, numero_buscado):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()