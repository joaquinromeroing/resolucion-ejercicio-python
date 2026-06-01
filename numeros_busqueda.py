def es_numero_valido(numero):
    return numero == 0 or 1 <= numero <= 100000


def ordenar_burbuja(Numeros):
    n = len(Numeros)

    for i in range(n):
        for j in range(0, n - i - 1):
            if Numeros[j] > Numeros[j + 1]:
                Numeros[j], Numeros[j + 1] = Numeros[j + 1], Numeros[j]

    return Numeros


def busqueda_binaria(Numeros, buscado):
    inicio = 0
    fin = len(Numeros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if Numeros[medio] == buscado:
            return True
        elif buscado < Numeros[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return False


def cargar_numeros():
    Numeros = []

    while True:
        numero = int(input("Ingrese un número entre 1 y 100000, o 0 para finalizar: "))

        if numero == 0:
            break

        if es_numero_valido(numero):
            Numeros.append(numero)
        else:
            print("Error: el número debe estar entre 1 y 100000")

    return Numeros


def main():
    Numeros = cargar_numeros()

    Numeros = ordenar_burbuja(Numeros)

    print("Números ordenados:", Numeros)

    buscado = int(input("Ingrese el número a buscar: "))

    encontrado = busqueda_binaria(Numeros, buscado)

    if encontrado:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()