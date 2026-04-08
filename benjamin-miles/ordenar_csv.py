import pandas as pd


#funcion de ordenamiento burbuja
def bubble_sort(data, col_index):
    n = len(data)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][col_index] > data[j + 1][col_index]:
                data[j], data[j + 1] = data[j + 1], data[j]
    
    return data


# Leer archivo desordenado
df = pd.read_csv('D:/Users/Eugenia/Documents/Facus/3 ano/Computacion I/supermercado_ej/COMPRAS_supermercado_desordenado_solo_sucursal.csv')

# Convertir a lista
data = df.values.tolist()
columnas = df.columns

# Obtener índice de PRSUC
col_index = df.columns.get_loc("PRSUC")

# Ordenar
data_ordenada = bubble_sort(data, col_index)

# Convertir a DataFrame
df_ordenado = pd.DataFrame(data_ordenada, columns=columnas)

# Guardar archivo ordenado
df_ordenado.to_csv("compras_ordenadas.csv", index=False)

print("Archivo ordenado generado correctamente.")
