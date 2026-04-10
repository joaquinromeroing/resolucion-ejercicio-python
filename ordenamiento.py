import csv

# Abrimos el archivo
with open('COMPRAS_supermercado_desordenado_solo_sucursal.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    cabecera = next(lector)  # Guardamos el encabezado aparte
    filas = list(lector)     # Convertimos el resto en una lista de listas
    
# 2. Implementación del algoritmo de Burbuja
n = len(filas)
for i in range(n):
    # El último i elementos ya están en su lugar
    for j in range(0, n - i - 1):
        # Comparamos el valor de la sucursal (índice 0)
        # Si el elemento actual es mayor que el siguiente, los intercambiamos
        if filas[j][0] > filas[j + 1][0]:
            filas[j], filas[j + 1] = filas[j + 1], filas[j]

# 3. Guardamos los datos ordenados en un nuevo archivo
with open('COMPRAS_supermercado_ordenado.csv', mode='w', newline='', encoding='utf-8') as archivo_salida:
    escritor = csv.writer(archivo_salida)
    escritor.writerow(cabecera)  # Escribimos el encabezado original
    escritor.writerows(filas)    # Escribimos las filas ya ordenadas

print("El archivo ha sido ordenado por sucursal exitosamente.")
