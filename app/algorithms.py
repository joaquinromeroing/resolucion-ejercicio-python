def ordenamiento_burbuja(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo


def busqueda_binaria(arreglo, objetivo):
    izquierda = 0
    derecha = len(arreglo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arreglo[medio] == objetivo:
            return medio
        elif arreglo[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1
