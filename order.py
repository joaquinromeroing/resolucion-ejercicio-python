import csv

def bubbleSearch(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j][0] > list[j+1][0]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

with open('COMPRAS_supermercado_desordenado_solo_sucursal.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    datos = list(reader)

datos_ordenados = bubbleSearch(datos)

with open('COMPRAS_ordenado.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(datos_ordenados)

print("Archivo ordenado generado")