# #!/usr/bin/python3

import csv

archivo = open("compras_ordenado.csv", "r")
reader = csv.reader(archivo)

next(reader)
fila = next(reader, None)

CANSUC = 0
TOTALIMP = 0

while fila is not None:
    PRSUC = fila[0]
    CANSUC += 1

    print(f"\nSucursal: {PRSUC}")

    TOTSUC = 0

    MYIMPOR = -1
    MNIMPOR = float("inf")

    MYPROD = ""
    MNPROD = ""

    while fila is not None and fila[0] == PRSUC:
        PRCOD = fila[1]

        TOTUNI = 0
        TOTPES = 0

        while fila is not None and fila[0] == PRSUC and fila[1] == PRCOD:
            PRCANT = int(fila[4])
            PRPRE = float(fila[5])

            TOTUNI += PRCANT
            TOTPES += PRCANT * PRPRE

            fila = next(reader, None)

        print(f"Producto: {PRCOD} | Unidades: {TOTUNI} | Importe: {TOTPES}")
        TOTSUC += TOTUNI
        TOTALIMP += TOTPES  # MODIFICADO: TOTALIMP suma pesos, no unidades

        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = PRCOD

        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD = PRCOD

    print(f"Total sucursal: {TOTSUC}")
    print(f"Mayor compra: {MYPROD} - {MYIMPOR}")
    print(f"Menor compra: {MNPROD} - {MNIMPOR}")

    # MODIFICADO:TOTSUC son unidades, no pesos
    # TOTALIMP += TOTSUC


archivo.close()

print("\n=== TOTALES GENERALES ===")
print(f"Cantidad de sucursales: {CANSUC}")
print(f"Importe total: {TOTALIMP}")
