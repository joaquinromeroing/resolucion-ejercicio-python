import pandas as pd
import csv


def ordenar_csv(path_entrada, path_salida):
    archivo = open(path_entrada, "r")
    lector = csv.reader(archivo)

    encabezado = next(lector)

    filas = []
    for fila in lector:
        filas.append(fila)

    archivo.close()

    n = len(filas)

    for i in range(n - 1):
        for j in range(n - 1):

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

    archivo = open(path_salida, "w", newline="")
    escritor = csv.writer(archivo)

    escritor.writerow(encabezado)

    for fila in filas:
        escritor.writerow(fila)

    archivo.close()


path = input("Indique el path del csv: ")
ordenado = input("El archivo esta ordenado? (Y/N): ")

if ordenado == "N":
    path_temporal = "archivo_temporal_ordenado.csv"
    ordenar_csv(path, path_temporal)
    path = path_temporal

df = pd.read_csv(path)

# por prod
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

    print("Sucursal:", suc, "| Producto:", prod, "| Unidades:", totuni, "| Total $:", totpes)
    print("")


# por suc
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


# totales
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