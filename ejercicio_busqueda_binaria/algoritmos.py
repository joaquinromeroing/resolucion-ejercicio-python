def ordenar_burbuja(numeros):
    numeros = numeros.copy()

    for i in range(len(numeros)):
        for j in range(0, len(numeros) - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    return numeros


def busqueda_binaria(numeros, numero_buscado):
    inicio = 0
    fin = len(numeros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if numeros[medio] == numero_buscado:
            return True
        elif numeros[medio] < numero_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False