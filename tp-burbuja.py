import csv

# 1. Leer CSV
lista = []

with open("COMPRAS_supermercado_desordenado_solo_sucursal.csv", newline="", encoding="utf-8") as f:
    archivo = csv.DictReader(f)

    for fila in archivo:
        fila["PRCANT"] = int(fila["PRCANT"])
        fila["PRPRE"] = float(fila["PRPRE"])
        lista.append(fila)

# 2. Burbuja
n = len(lista)

for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j]["PRSUC"] > lista[j + 1]["PRSUC"]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

# 3. Guardar resultado
with open("COMPRAS_ordenado.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["PRSUC", "PRCOD", "PRFEC", "PRPROV", "PRCANT", "PRPRE"]
    writer = csv.DictWriter(f, fieldnames=campos)

    writer.writeheader()

    for fila in lista:
        writer.writerow(fila)

print("Archivo ordenado generado correctamente")