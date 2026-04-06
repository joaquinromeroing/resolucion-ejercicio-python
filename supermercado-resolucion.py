import csv

with open("COMPRAS_supermercado.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    compras = list(lector)

# si el archivo estuviera desordenado, aca agregamos:
compras.sort(key=lambda x: (x["PRSUC"], x["PRCOD"]))
# para ordenar la lista por sucursal y por producto.

if len(compras) == 0:
    print("El archivo esta vacio")
else:
    totalimp = 0
    cansuc = 0
    i = 0

    while i < len(compras):
        sucursal = compras[i]["PRSUC"]
        cansuc = cansuc + 1
        totsuc = 0
        myprod = ""
        myimpor = -1
        mnprod = ""
        mnimpor = -1

        print("\nSUCURSAL", sucursal)

        while i < len(compras) and compras[i]["PRSUC"] == sucursal:
            producto = compras[i]["PRCOD"]
            totuni = 0
            totpes = 0

            while i < len(compras) and compras[i]["PRSUC"] == sucursal and compras[i]["PRCOD"] == producto:
                cantidad = int(compras[i]["PRCANT"])
                precio = float(compras[i]["PRPRE"])
                importe = cantidad * precio

                totuni = totuni + cantidad
                totpes = totpes + importe
                i = i + 1
            
            print("Producto: ", producto, "Total de unidades: ", totuni, "Total de pesos: $", round(totpes, 2))

            totsuc = totsuc + totuni
            totalimp = totalimp + totpes

            if totpes > myimpor:
                myimpor = totpes
                myprod = producto

            if mnimpor == -1 or totpes < mnimpor:
                mnimpor = totpes
                mnprod = producto

        print("Total comprado en unidades: ", totsuc)
        print("Producto de mayor compra en pesos: ", myprod, "- $", round(myimpor, 2))
        print("Producto de menor compra en pesos: ", mnprod, "- $", round(mnimpor, 2))

    print("\nTOTAL GENERAL")
    print("Cantidad de sucursales: ", cansuc)
    print("Compra total en pesos: $", round(totalimp, 2))


        

























