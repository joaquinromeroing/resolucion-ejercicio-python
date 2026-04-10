import pandas as pd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Especifica el nombre del archivo CSV aquí
filename = pd.read_csv('COMPRASD.csv')

# Leer la lista desde el archivo CSV (asumiendo una columna de números)
data = filename.iloc[:, 0].tolist()

# Ordenar la lista usando bubble sort
sorted_data = bubble_sort(data)

# Imprimir la lista ordenada
print("Lista ordenada:", sorted_data)