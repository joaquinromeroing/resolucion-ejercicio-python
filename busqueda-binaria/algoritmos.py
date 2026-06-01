def burbuja(numeros):
    arr = list(numeros)
    n = len(arr)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio = True
        if not intercambio:
            break
    return arr


def busqueda_binaria(numeros, objetivo):
    izquierda = 0
    derecha = len(numeros) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if numeros[medio] == objetivo:
            return True
        if numeros[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False
