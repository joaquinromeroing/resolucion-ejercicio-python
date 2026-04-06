# =========================================================
#                 EJERCICIO SUPERMERCADO
# =========================================================

# En un supermercado de la Ciudad se desea obtener una estadística de las compras realizadas en
# un período de tiempo en las diferentes sucursales que posee. La información se encuentra
# almacenada en un archivo COMPRAS cuyo formato de registro es el siguiente (archivo csv):
# SUCURSAL (PRSUC)
# CODIGO DE PRODUCTO (PRCOD)
# FECHA DE COMPRA (PRFEC)
# PROVEEDOR (PRPROV)
# CANTIDAD COMPRADA (PRCANT)
# PRECIO UNITARIO COMPRA (PRPRE)
#
# La información se encuentra ordenada por código de sucursal, producto, fecha de compra y
# proveedor.
# Se debe obtener información sobre:
# a) POR PRODUCTO: De cada producto comprado en cada sucursal indicar el total comprado
#    en unidades (TOTUNI) y en pesos (TOTPES)
# b) POR SUCURSAL: informar el total comprado en unidades (TOTSUC) y el producto de
#    mayor (MYPROD, MYIMPOR) y menor compra (MNPRO, MNIMPOR) en pesos.
# c) A nivel total: total de sucursales del supermercado (CANSUC) y
#    compra total en pesos de todas las sucursales (TOTALIMP)
#
# Imprimir los resultados obtenidos.

import pandas as pd

df = pd.read_csv("COMPRAS_supermercado_ordenado_solo_sucursal.csv")

# Convertimos el DataFrame a lista de registros
registros = df.to_dict(orient="records")

n = len(registros)
i = 0
cansuc = 0
totalimp = 0.0

print("=" * 60)
print("INFORME DE COMPRAS")
print("=" * 60)

while i < n:
    suc_actual = registros[i]["PRSUC"]
    cansuc += 1

    totsuc = 0  # total comprado en unidades en esa sucursal

    myprod = None
    myimpor = -1

    mnprod = None
    mnimpor = float("inf")

    print(f"\nSucursal: {suc_actual}")

    # Mientras siga la misma sucursal
    while i < n and registros[i]["PRSUC"] == suc_actual:
        prod_actual = registros[i]["PRCOD"]

        totuni = 0
        totpes = 0.0

        # Mientras siga el mismo producto dentro de esa sucursal
        while (
            i < n
            and registros[i]["PRSUC"] == suc_actual
            and registros[i]["PRCOD"] == prod_actual
        ):
            cantidad = int(registros[i]["PRCANT"])
            precio = float(registros[i]["PRPRE"])
            importe = cantidad * precio

            totuni += cantidad
            totpes += importe

            i += 1

        # Mostrar resultado por producto
        print(f"  Producto {prod_actual} -> TOTUNI: {totuni} | TOTPES: ${totpes:.2f}")

        # Acumular total de unidades de la sucursal
        totsuc += totuni

        # Acumular total general en pesos
        totalimp += totpes

        # Buscar mayor compra por producto en pesos
        if totpes > myimpor:
            myimpor = totpes
            myprod = prod_actual

        # Buscar menor compra por producto en pesos
        if totpes < mnimpor:
            mnimpor = totpes
            mnprod = prod_actual

    # Mostrar resultado por sucursal
    print(f"  TOTSUC  : {totsuc}")
    print(f"  MYPROD  : {myprod} | MYIMPOR: ${myimpor:.2f}")
    print(f"  MNPROD  : {mnprod} | MNIMPOR: ${mnimpor:.2f}")

print("\n" + "=" * 60)
print("TOTALES GENERALES")
print("=" * 60)
print(f"CANSUC   : {cansuc}")
print(f"TOTALIMP : ${totalimp:.2f}")

#cambio
