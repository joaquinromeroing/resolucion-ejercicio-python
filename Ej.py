import csv

archivo = open("COMPRAS_supermercado.csv", "r", newline="", encoding="utf-8")
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