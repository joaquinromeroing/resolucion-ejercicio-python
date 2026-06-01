def ordenar_burbuja(Numeros):
    """
    Ordena una lista de números enteros usando el método Burbuja.
    Devuelve una nueva lista ordenada, sin modificar la original.
    """
    numeros_ordenados = Numeros.copy()

    n = len(numeros_ordenados)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numeros_ordenados[j] > numeros_ordenados[j + 1]:
                aux = numeros_ordenados[j]
                numeros_ordenados[j] = numeros_ordenados[j + 1]
                numeros_ordenados[j + 1] = aux

    return numeros_ordenados


def busqueda_binaria(Numeros, numero_buscado):
    """
    Busca un número dentro de una lista ordenada usando Búsqueda Binaria.
    Devuelve True si lo encuentra y False si no lo encuentra.
    """
    inicio = 0
    fin = len(Numeros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if Numeros[medio] == numero_buscado:
            return True
        elif numero_buscado < Numeros[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return False


def cargar_numeros():
    """
    Solicita números al usuario.
    Solo acepta valores entre 1 y 100000.
    Finaliza cuando el usuario ingresa 0.
    """
    Numeros = []

    numero = int(input("Ingrese un número entero entre 1 y 100000. Ingrese 0 para finalizar: "))

    while numero != 0:
        if numero >= 1 and numero <= 100000:
            Numeros.append(numero)
        else:
            print("Error: el número debe estar entre 1 y 100000")

        numero = int(input("Ingrese un número entero entre 1 y 100000. Ingrese 0 para finalizar: "))

    return Numeros


def main():
    Numeros = cargar_numeros()

    Numeros = ordenar_burbuja(Numeros)

    print("Numeros ordenados:", Numeros)

    numero_buscado = int(input("Ingrese el número a buscar: "))

    encontrado = busqueda_binaria(Numeros, numero_buscado)

    if encontrado:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()
