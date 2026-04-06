#   Cortes de Control:


# Enunciado: 

# En un supermercado de la Ciudad se desea obtener una estadística de las compras realizadas en
# un período de tiempo en las diferentes sucursales que posee. La información se encuentra
# almacenada en un archivo COMPRAS cuyo formato de registro es el siguiente (archivo csv):
# SUCURSAL (PRSUC)
# CODIGO DE PRODUCTO (PRCOD)
# FECHA DE COMPRA (PRFEC)
# PROVEEDOR (PRPROV)
# CANTIDAD COMPRADA (PRCANT)
# PRECIO UNITARIO COMPRA (PRPRE)

# La información se encuentra ordenada por código de sucursal, producto, fecha de compra y
# proveedor.
# Se debe obtener información sobre:
# a) POR PRODUCTO: De cada producto comprado en cada sucursal indicar el total comprado
# en unidades (TOTUNI) y en pesos (TOTPES)
# b) POR SUCURSAL: l informar el total comprado en unidades (TOTSUC) y el producto de
# mayor (MYPROD, MYIMPOR) y menor compra (MNPRO,MNIMPOR) en pesos.
# c) Por otro lado indicar a nivel total: total de sucursales del supermercado (CANSUC) y
# compra total en pesos de todas las sucursales (TOTALIMP)

# Imprimir los resultados obtenidos.


import csv

archivo = open("COMPRAS_supermercado.csv", encoding="utf-8")
lector = csv.DictReader(archivo)

filas = list(lector)
archivo.close()

i = 0
CANSUC = 0
TOTALIMP = 0

while i < len(filas):
    suc_actual = filas[i]["PRSUC"]
    TOTSUC = 0
    IMP_SUC = 0
    MYPROD = ""
    MYIMPOR = -1
    MNPROD = ""
    MNIMPOR = 10000000000

    while i < len(filas) and filas[i]["PRSUC"] == suc_actual:
        prod_actual = filas[i]["PRCOD"]

        TOTUNI = 0
        TOTPES = 0

        while (i < len(filas)and filas[i]["PRSUC"] == suc_actual and filas[i]["PRCOD"] == prod_actual):
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