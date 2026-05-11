import csv
import pandas as pd



# ORDENAMIENTO DEL ARCHIVO


print("Cargando archivo...")

archivo = open("COMPRAS_supermercado_desordenado_solo_sucursal.csv", "r")
lector = csv.reader(archivo)

encabezado = next(lector)

filas = []

for fila in lector:
    filas.append(fila)

archivo.close()

print("Archivo cargado.")
print("Comenzando ordenamiento...")



# ORDENAMIENTO BURBUJA OPTIMIZADO


n = len(filas)

for i in range(n - 1):

    hubo_intercambio = False

    for j in range(n - 1 - i):

        f1 = filas[j]
        f2 = filas[j + 1]

        intercambiar = False

        if f1[0] > f2[0]:
            intercambiar = True

        elif f1[0] == f2[0]:

            if f1[1] > f2[1]:
                intercambiar = True

            elif f1[1] == f2[1]:

                if f1[2] > f2[2]:
                    intercambiar = True

                elif f1[2] == f2[2]:

                    if f1[3] > f2[3]:
                        intercambiar = True

                    elif f1[3] == f2[3]:

                        if int(f1[4]) > int(f2[4]):
                            intercambiar = True

                        elif int(f1[4]) == int(f2[4]):

                            if float(f1[5]) > float(f2[5]):
                                intercambiar = True

        if intercambiar:

            aux = filas[j]
            filas[j] = filas[j + 1]
            filas[j + 1] = aux

            hubo_intercambio = True

    if hubo_intercambio == False:
        break


print("Ordenamiento terminado.")



# GUARDAR ARCHIVO ORDENADO


archivo = open("COMPRAS_supermercado_ordenado.csv", "w", newline="")
escritor = csv.writer(archivo)

escritor.writerow(encabezado)

for fila in filas:
    escritor.writerow(fila)

archivo.close()

print("Archivo ordenado guardado.")
print("")



# LEER ARCHIVO ORDENADO


df = pd.read_csv("COMPRAS_supermercado_ordenado.csv")



# CORTE DE CONTROL POR PRODUCTO


print("CORTE POR PRODUCTO")
print("")

i = 0

while i < len(df):

    suc = df["PRSUC"][i]
    prod = df["PRCOD"][i]

    totuni = 0
    totpes = 0

    while i < len(df) and df["PRSUC"][i] == suc and df["PRCOD"][i] == prod:

        totuni = totuni + df["PRCANT"][i]
        totpes = totpes + df["PRCANT"][i] * df["PRPRE"][i]

        i = i + 1

    print("Sucursal:", suc,
          "| Producto:", prod,
          "| Unidades:", totuni,
          "| Total $:", totpes)

print("")



# CORTE DE CONTROL POR SUCURSAL


print("CORTE POR SUCURSAL")
print("")

i = 0

while i < len(df):

    suc = df["PRSUC"][i]

    totsuc = 0

    myprod = ""
    myimpor = 0

    mnprod = ""
    mnimpor = 999999999

    while i < len(df) and df["PRSUC"][i] == suc:

        prod = df["PRCOD"][i]

        totuni = 0
        totpes = 0

        while i < len(df) and df["PRSUC"][i] == suc and df["PRCOD"][i] == prod:

            totuni = totuni + df["PRCANT"][i]
            totpes = totpes + df["PRCANT"][i] * df["PRPRE"][i]

            i = i + 1

        totsuc = totsuc + totuni

        if totpes > myimpor:

            myimpor = totpes
            myprod = prod

        if totpes < mnimpor:

            mnimpor = totpes
            mnprod = prod

    print("Sucursal:", suc)
    print("Total unidades:", totsuc)
    print("Mayor producto:", myprod, "| Importe:", myimpor)
    print("Menor producto:", mnprod, "| Importe:", mnimpor)
    print("")



# TOTALES GENERALES


print("TOTALES GENERALES")
print("")

i = 0

cansuc = 0
totalimp = 0

while i < len(df):

    suc = df["PRSUC"][i]

    cansuc = cansuc + 1

    while i < len(df) and df["PRSUC"][i] == suc:

        totalimp = totalimp + df["PRCANT"][i] * df["PRPRE"][i]

        i = i + 1

print("Cantidad de sucursales:", cansuc)
print("Total general $:", totalimp)