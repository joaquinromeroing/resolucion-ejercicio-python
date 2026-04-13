#!/bin/env python3
import csv

# Leer el archivo desordenado
nombre_entrada = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
nombre_salida = "COMPRAS_supermercado_ordenado.csv"

with open(nombre_entrada, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    filas = list(reader)
    encabezados = reader.fieldnames

# Algoritmo de ordenamiento burbuja
# Ordenamos por PRSUC (sucursal) y luego por PRFEC (fecha)
n = len(filas)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        clave_actual = (filas[j]["PRSUC"], filas[j]["PRFEC"])
        clave_siguiente = (filas[j + 1]["PRSUC"], filas[j + 1]["PRFEC"])
        if clave_actual > clave_siguiente:
            filas[j], filas[j + 1] = filas[j + 1], filas[j]

# Grabar el archivo ordenado
with open(nombre_salida, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=encabezados)
    writer.writeheader()
    writer.writerows(filas)

print(f"Archivo ordenado guardado como: {nombre_salida}")
print(f"Total de filas procesadas: {n}")
