import csv

def ordenar_burbuja_por_sucursal(filas):
    n = len(filas)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if filas[j]["PRSUC"] > filas[j + 1]["PRSUC"]:
                aux = filas[j]
                filas[j] = filas[j + 1]
                filas[j + 1] = aux

    return filas


archivo = open("COMPRAS_supermercado_desordenado_solo_sucursal.csv", encoding="utf-8")
lector = csv.DictReader(archivo)
filas = list(lector)
encabezados = lector.fieldnames
archivo.close()

filas = ordenar_burbuja_por_sucursal(filas)


# GRABAR ARCHIVO ORDENADO
archivo = open("COMPRAS_ordenado.csv", "w", newline="", encoding="utf-8")
escritor = csv.DictWriter(archivo, fieldnames=encabezados)
escritor.writeheader()
escritor.writerows(filas)
archivo.close()

# LEER ARCHIVO ORDENADO
archivo = open("COMPRAS_ordenado.csv", encoding="utf-8")
lector = csv.DictReader(archivo)
filas = list(lector)
archivo.close()

n = len(filas)
i = 0
CANSUC = 0
TOTALIMP = 0

while i < n:
    suc_actual = filas[i]["PRSUC"]
    TOTSUC = 0
    IMP_SUC = 0
    MYPROD = ""
    MYIMPOR = -1
    MNPROD = ""
    MNIMPOR = 10000000000

    while i < n and filas[i]["PRSUC"] == suc_actual:
        prod_actual = filas[i]["PRCOD"]

        TOTUNI = 0
        TOTPES = 0

        while (i < n and filas[i]["PRSUC"] == suc_actual and filas[i]["PRCOD"] == prod_actual):
            cantidad = int(filas[i]["PRCANT"])
            precio = float(filas[i]["PRPRE"])

            TOTUNI += cantidad
            TOTPES += cantidad * precio

            i += 1

       #A
        print(f"Producto {prod_actual}")
        print(f"  Total unidades: {TOTUNI}")
        print(f"  Total pesos: ${TOTPES:.2f}")

        TOTSUC += TOTUNI
        IMP_SUC += TOTPES

        # Mayor compra en pesos
        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = prod_actual

        # Menor compra en pesos
        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD = prod_actual

   #B
    print(f"\nResumen sucursal {suc_actual}:")
    print(f"Total comprado en unidades: {TOTSUC}")
    print(f"Producto de mayor compra: {MYPROD} con ${MYIMPOR:.2f}")
    print(f"Producto de menor compra: {MNPROD} con ${MNIMPOR:.2f}")

    #C
    CANSUC += 1
    TOTALIMP += IMP_SUC


print("\n=== TOTALES GENERALES ===")
print(f"Cantidad de sucursales: {CANSUC}")
print(f"Compra total en pesos: ${TOTALIMP:.2f}")