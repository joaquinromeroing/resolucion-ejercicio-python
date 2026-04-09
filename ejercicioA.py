import csv

archivo = open("COMPRAS_supermercado.csv", "r")  

linea = archivo.readline().strip()

sucuActual = None
productActual = None

myProd = None
myImport = -1

mnProd = None
mnImport = float("inf")

totUni = 0
totPes = 0
totSuc = 0

canSuc = 0
totaLimp = 0

while linea != "":
    data = linea.split(",")

    suc = data[0]
    prod = data[1]
    cant = int(data[4])
    prec = float(data[5])

    if sucuActual == None:
        canSuc += 1

        sucuActual = suc
        productActual = prod

    if suc != sucuActual or prod != productActual:
        print(f"Sucursal {sucuActual} - Producto {productActual}")
        print(f"  Total unidades: {totUni}")
        print(f"  Total pesos: {totPes}")

        if totPes > myImport:
            myImport = totPes
            myProd = productActual

        if totPes < mnImport:
            mnImport = totPes
            mnProd = productActual

        if suc != sucuActual:
            canSuc += 1

            print("-----------------------------------")
            print(f"Scursal: {sucuActual}")
            print(f"Total Unidasdes: {totSuc}")
            print(f"Mayor producto comprado: {myProd} - ${myImport}")
            print(f"Menor producto comprado: {mnProd} - ${mnImport}")
            print("-----------------------------------")

            totSuc = 0
            myImport = -1
            mnImport = float("inf")

        totUni = 0
        totPes = 0

        sucuActual = suc
        productActual = prod

    totUni += cant
    totPes += cant * prec
    totSuc += cant
    totaLimp += cant * prec

    linea = archivo.readline().strip()

print("-----------------------------------")
print(f"Total sucursales: {canSuc}")
print(f"Total de pesos en compras: ${totaLimp}")
print("-----------------------------------")


