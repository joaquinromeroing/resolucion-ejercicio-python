import csv

archivo = open("COMPRAS_supermercado.csv", "r", encoding="utf-8")
lector = csv.reader(archivo)
next(lector)

registros = list(lector)
n = len(registros)
i = 0

TOTALIMP = 0 #para el total de plata en compras
CANSUC = 0 #para contar cuantas sucursales tengo

while i < n:
    sucursal_actual = registros[i][0]
    TOTSUC = 0
    CANSUC += 1

    primera_vez = True

    print(f"\nSUCURSAL: {sucursal_actual}")

    while i < n and registros[i][0] == sucursal_actual:
        producto_actual = registros[i][1]
        TOTUNI = 0
        TOTPES = 0

        while i < n and registros[i][0] == sucursal_actual and registros[i][1] == producto_actual:
            cantidad = int(registros[i][4])
            precio = float(registros[i][5])
            importe = cantidad * precio

            TOTUNI += cantidad
            TOTPES += importe

            i += 1

        print(f"Producto: {producto_actual} - Total unidades: {TOTUNI} - Total pesos: {TOTPES:.2f}")

        TOTSUC += TOTUNI
        TOTALIMP += TOTPES

        if primera_vez:
            MYPROD = producto_actual
            MYIMPOR = TOTPES
            MNPRO = producto_actual
            MNIMPOR = TOTPES
            primera_vez = False
        else:
            if TOTPES > MYIMPOR:
                MYPROD = producto_actual
                MYIMPOR = TOTPES

            if TOTPES < MNIMPOR:
                MNPRO = producto_actual
                MNIMPOR = TOTPES

    print(f"Total unidades sucursal: {TOTSUC}")
    print(f"Mayor compra en pesos: {MYPROD} - {MYIMPOR:.2f}")
    print(f"Menor compra en pesos: {MNPRO} - {MNIMPOR:.2f}")

print("\nTOTALES GENERALES")
print(f"Cantidad de sucursales: {CANSUC}")
print(f"Importe total de todas las sucursales: {TOTALIMP:.2f}")

archivo.close()