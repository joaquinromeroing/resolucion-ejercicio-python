def ordenar_burbuja(numeros):
    n = len(numeros)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numeros[j] > numeros[j + 1]:
                aux = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = aux

    return numeros


def busqueda_binaria(numeros, buscado):
    inicio = 0
    fin = len(numeros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if numeros[medio] == buscado:
            return True

        if buscado < numeros[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return False


def cargar_numeros():
    numeros = []

    while True:
        numero = int(input("Ingrese un numero entre 1 y 100000 (0 para finalizar): "))

        if numero == 0:
            break

        if numero < 1 or numero > 100000:
            print("Error: el numero debe estar entre 1 y 100000")
        else:
            numeros.append(numero)

    return numeros


def main():
    Numeros = cargar_numeros()

    ordenar_burbuja(Numeros)

    buscado = int(input("Ingrese el numero a buscar: "))

    if busqueda_binaria(Numeros, buscado):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()