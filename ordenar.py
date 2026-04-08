import csv

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][0] > lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

filas = []
with open('COMPRAS_supermercado_desordenado_solo_sucursal.csv', 'r', encoding='utf-8') as f:
    lector = csv.reader(f)
    header = next(lector)
    filas = list(lector)

filas_ordenadas = burbuja(filas)
with open('COMPRAS_ordenado.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(header)
    escritor.writerows(filas_ordenadas)

print("Paso 1: Archivo 'COMPRAS_ordenado.csv' generado.")