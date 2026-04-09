import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ARCHIVO_ENTRADA  = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
ARCHIVO_ORDENADO = "COMPRAS_supermercado_ordenado.csv"

with open(ARCHIVO_ENTRADA, newline="", encoding="utf-8-sig") as f:
    lector = csv.DictReader(f)
    campos = lector.fieldnames
    registros = list(lector)

n = len(registros)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if registros[j]["PRSUC"] > registros[j + 1]["PRSUC"]:
            registros[j], registros[j + 1] = registros[j + 1], registros[j]

with open(ARCHIVO_ORDENADO, "w", newline="", encoding="utf-8-sig") as f:
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(registros)

print(f"Archivo ordenado grabado como: {ARCHIVO_ORDENADO}")
