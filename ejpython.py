import csv

# ================================
# CODIGO DEL ARCHIVO ejbubble.py
# ================================
def ordenar_csv(path_entrada, path_salida):
    archivo = open(path_entrada, "r")
    reader = csv.reader(archivo)
    next(reader)

    datos = list(reader)
    archivo.close()

    n = len(datos)

    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j][0] > datos[j + 1][0]:
                temp = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = temp

    archivo_out = open(path_salida, "w", newline="")
    writer = csv.writer(archivo_out)

    writer.writerow(["PRSUC", "PRCOD", "PRFEC", "PRPROV", "PRCANT", "PRPRE"])
    writer.writerows(datos)
    archivo_out.close()


# ==================================
# CODIGO DEL ARCHIVO ejpython.py
# ==================================
def procesar_csv(path_archivo):
    archivo = open(path_archivo, "r")
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
            TOTALIMP += TOTPES

            if TOTPES > MYIMPOR:
                MYIMPOR = TOTPES
                MYPROD = PRCOD

            if TOTPES < MNIMPOR:
                MNIMPOR = TOTPES
                MNPROD = PRCOD

        print(f"Total sucursal: {TOTSUC}")
        print(f"Mayor compra: {MYPROD} - {MYIMPOR}")
        print(f"Menor compra: {MNPROD} - {MNIMPOR}")

    archivo.close()

    print("\n=== TOTALES GENERALES ===")
    print(f"Cantidad de sucursales: {CANSUC}")
    print(f"Importe total: {TOTALIMP}")


# ================================
path_csv = input("Indique el path del csv: ")
ordenado = input("El archivo esta ordenado? Y/N: ").upper()

if ordenado == "N":
    archivo_temporal = "compras_ordenado.csv"
    ordenar_csv(path_csv, archivo_temporal)
    procesar_csv(archivo_temporal)
else:
    procesar_csv(path_csv)