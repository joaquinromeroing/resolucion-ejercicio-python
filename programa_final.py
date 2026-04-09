import csv
import os

# ─────────────────────────────────────────────
# FUNCIÓN: Bubble Sort
# ─────────────────────────────────────────────
def bubble_sort(filas):
    n = len(filas)
    print(f"\nOrdenando {n} registros con Bubble Sort...")
    for i in range(n - 1):
        for j in range(n - 1 - i):
            clave_actual    = (filas[j]['PRSUC'],   filas[j]['PRCOD'],   filas[j]['PRFEC'])
            clave_siguiente = (filas[j+1]['PRSUC'], filas[j+1]['PRCOD'], filas[j+1]['PRFEC'])
            if clave_actual > clave_siguiente:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
        if i % 500 == 0:
            print(f"  Pasada {i + 1} de {n - 1}...")
    print("Ordenamiento completado.\n")
    return filas

# ─────────────────────────────────────────────
# FUNCIÓN: Procesar CSV (tu código original)
# ─────────────────────────────────────────────
def procesar(path_csv):
    archivo = open(path_csv, "r", newline="", encoding="utf-8")
    reader = csv.DictReader(archivo)

    reg = next(reader, None)

    cansuc = 0
    totalimp = 0

    while reg is not None:
        suc_actual = reg["PRSUC"]
        cansuc += 1

        totsuc = 0
        myprod = ""
        myimpor = -1
        mnprod = ""
        mnimpor = None

        print("\n---------------------------------")
        print("SUCURSAL:", suc_actual)
        print("PRODUCTO\tTOTUNI\tTOTPES")

        while reg is not None and reg["PRSUC"] == suc_actual:
            prod_actual = reg["PRCOD"]

            totuni = 0
            totpes = 0

            while reg is not None and reg["PRSUC"] == suc_actual and reg["PRCOD"] == prod_actual:
                cantidad = int(reg["PRCANT"])
                precio = float(reg["PRPRE"])

                totuni += cantidad
                totpes += cantidad * precio

                reg = next(reader, None)

            print(f"{prod_actual}\t\t{totuni}\t{totpes:.2f}")

            totsuc += totuni
            totalimp += totpes

            if totpes > myimpor:
                myimpor = totpes
                myprod = prod_actual

            if mnimpor is None or totpes < mnimpor:
                mnimpor = totpes
                mnprod = prod_actual

        print("TOTAL UNIDADES SUCURSAL:", totsuc)
        print("PRODUCTO DE MAYOR COMPRA:", myprod, "-", f"{myimpor:.2f}")
        print("PRODUCTO DE MENOR COMPRA:", mnprod, "-", f"{mnimpor:.2f}")

    print("\n=================================")
    print("CANTIDAD DE SUCURSALES:", cansuc)
    print("IMPORTE TOTAL DEL SUPERMERCADO:", f"{totalimp:.2f}")

    archivo.close()

# ─────────────────────────────────────────────
# MENÚ PRINCIPAL
# ─────────────────────────────────────────────
path_csv = input("Indique el path del csv: ").strip()

if not os.path.exists(path_csv):
    print(f"Error: no se encontró el archivo '{path_csv}'")
else:
    ordenado = input("El archivo esta ordenado (Y/N): ").strip().upper()

    if ordenado == 'N':
        # Leer, ordenar y grabar archivo temporal
        with open(path_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            filas = list(reader)
            encabezado = reader.fieldnames

        filas = bubble_sort(filas)

        path_temporal = "archivo_temporal_ordenado.csv"
        with open(path_temporal, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=encabezado)
            writer.writeheader()
            writer.writerows(filas)

        procesar(path_temporal)

    elif ordenado == 'Y':
        procesar(path_csv)

    else:
        print("Opcion no valida. Ingrese Y o N.")
