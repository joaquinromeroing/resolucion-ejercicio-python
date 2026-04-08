import csv

ENTRADA = 'COMPRAS_supermercado_desordenado_solo_sucursal.csv'
SALIDA  = 'COMPRAS_ordenado.csv'

datos = []
with open(ENTRADA, newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    campos = lector.fieldnames
    for fila in lector:
        datos.append(fila)

n = len(datos)
for i in range(n - 1):
    for j in range(n - 1 - i):
        a = datos[j]
        b = datos[j + 1]
        clave_a = (a['PRSUC'], a['PRCOD'], a['PRFEC'], a['PRPROV'])
        clave_b = (b['PRSUC'], b['PRCOD'], b['PRFEC'], b['PRPROV'])
        if clave_a > clave_b:
            datos[j], datos[j + 1] = datos[j + 1], datos[j]

with open(SALIDA, 'w', newline='', encoding='utf-8') as f:
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(datos)

print(f"Archivo ordenado guardado en: {SALIDA}")
