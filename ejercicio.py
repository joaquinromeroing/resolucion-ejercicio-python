archivo = open("COMPRAS_supermercado.csv", "r")
linea = archivo.readline().strip()

canSuc = 0
totalImp = 0

while linea != "":

    data = linea.split(",")

    sucActual = data[0]
    canSuc += 1

    totSuc = 0

    myImport = -1
    mnImport = float("inf")

    while linea != "" and data[0] == sucActual:

        prodActual = data[1]

        totUni = 0
        totPes = 0

        while linea != "" and data[0] == sucActual and data[1] == prodActual:

            cant = int(data[4])
            prec = float(data[5])

            totUni += cant
            totPes += cant * prec
            totSuc += cant
            totalImp += cant * prec

            linea = archivo.readline().strip()
            if linea != "":
                data = linea.split(",")

        print(f"Sucursal {sucActual} - Producto {prodActual}")
        print(f"  Total unidades: {totUni}")
        print(f"  Total pesos: {totPes}")

        # Mayor / menor
        if totPes > myImport:
            myImport = totPes
            myProd = prodActual

        if totPes < mnImport:
            mnImport = totPes
            mnProd = prodActual

    print("-----------------------------------")
    print(f"Sucursal: {sucActual}")
    print(f"Total Unidades: {totSuc}")
    print(f"Mayor producto: {myProd} - ${myImport}")
    print(f"Menor producto: {mnProd} - ${mnImport}")
    print("-----------------------------------")


print("===================================")
print(f"Total sucursales: {canSuc}")
print(f"Total importe: ${totalImp}")
print("===================================")