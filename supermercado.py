import pandas as pd
import csv



# FUNCIONES GENERALES


def calcular_importe(cantidad, precio):
    return cantidad * precio



# ORDENAMIENTO BURBUJA


def leer_csv(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lector = csv.reader(archivo)

    encabezado = next(lector)

    filas = []
    for fila in lector:
        filas.append(fila)

    archivo.close()

    return encabezado, filas


def debe_intercambiar(f1, f2):
    if f1[0] > f2[0]:
        return True

    elif f1[0] == f2[0]:
        if f1[1] > f2[1]:
            return True

        elif f1[1] == f2[1]:
            if f1[2] > f2[2]:
                return True

            elif f1[2] == f2[2]:
                if f1[3] > f2[3]:
                    return True

                elif f1[3] == f2[3]:
                    if int(f1[4]) > int(f2[4]):
                        return True

                    elif int(f1[4]) == int(f2[4]):
                        if float(f1[5]) > float(f2[5]):
                            return True

    return False


def ordenar_burbuja(filas):
    n = len(filas)

    for i in range(n - 1):
        for j in range(n - 1):
            if debe_intercambiar(filas[j], filas[j + 1]):
                aux = filas[j]
                filas[j] = filas[j + 1]
                filas[j + 1] = aux

    return filas


def guardar_csv(nombre_archivo, encabezado, filas):
    archivo = open(nombre_archivo, "w", newline="")
    escritor = csv.writer(archivo)

    escritor.writerow(encabezado)

    for fila in filas:
        escritor.writerow(fila)

    archivo.close()


def ordenar_archivo():
    encabezado, filas = leer_csv("COMPRAS_supermercado_desordenado_solo_sucursal.csv")
    filas_ordenadas = ordenar_burbuja(filas)
    guardar_csv("COMPRAS_supermercado_ordenado.csv", encabezado, filas_ordenadas)

    print("archivo ordenado.")



#  ANALISIS


def leer_compras(nombre_archivo):
    return pd.read_csv(nombre_archivo)


def mostrar_totales_por_producto(df):
    i = 0

    while i < len(df):
        suc = df["PRSUC"][i]
        prod = df["PRCOD"][i]

        totuni = 0
        totpes = 0

        while i < len(df) and df["PRSUC"][i] == suc and df["PRCOD"][i] == prod:
            totuni += df["PRCANT"][i]
            totpes += calcular_importe(df["PRCANT"][i], df["PRPRE"][i])
            i += 1

        print("Sucursal:", suc, "| Producto:", prod, "| Unidades:", totuni, "| Total $:", totpes)
        print("")


def mostrar_totales_por_sucursal(df):
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
                totuni += df["PRCANT"][i]
                totpes += calcular_importe(df["PRCANT"][i], df["PRPRE"][i])
                i += 1

            totsuc += totuni

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


def mostrar_totales_generales(df):
    i = 0
    cansuc = 0
    totalimp = 0

    while i < len(df):
        suc = df["PRSUC"][i]
        cansuc += 1

        while i < len(df) and df["PRSUC"][i] == suc:
            totalimp += calcular_importe(df["PRCANT"][i], df["PRPRE"][i])
            i += 1

    print("Cantidad de sucursales:", cansuc)
    print("Total general $:", totalimp)



# MAIN

def main():
    ordenar_archivo()

    df = leer_compras("COMPRAS_supermercado_ordenado.csv")

    mostrar_totales_por_producto(df)
    mostrar_totales_por_sucursal(df)
    mostrar_totales_generales(df)


if __name__ == "__main__":
    main()