def ordenamiento_burbuja(arreglo):
    """
    Ordena un arreglo de números enteros de menor a mayor
    utilizando el método de la Burbuja.
    """
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                # Intercambio de elementos en Python (Swap)
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


def busqueda_binaria(arreglo, elemento_buscado):
    """
    Busca un elemento dentro de un arreglo ORDENADO.
    Devuelve True si lo encuentra, False en caso contrario.
    """
    bajo = 0
    alto = len(arreglo) - 1

    while bajo <= alto:
        centro = (bajo + alto) // 2  # División entera
        
        if arreglo[centro] == elemento_buscado:
            return True
        elif elemento_buscado < arreglo[centro]:
            alto = centro - 1  # Descartar mitad derecha
        else:
            bajo = centro + 1  # Descartar mitad izquierda
            
    return False
