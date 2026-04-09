import csv
archivo = open("COMPRAS_desordenado.csv", "r")

reader = csv.reader(archivo)
next(reader)

datos = list(reader)
archivo.close()

n = len(datos)

for i in range(n):
    for j in range(0, n - i - 1):
        if datos[j][0] > datos[j + 1][0]:
            temp = datos[j]
            datos[j] = datos[j + 1]
            datos[j + 1] = temp

archivo_out = open("compras_ordenado.csv", "w", newline="")
writer = csv.writer(archivo_out)

writer.writerow(["PRSUC", "PRCOD", "PRFEC", "PRPROV", "PRCANT", "PRPRE"])

writer.writerows(datos)
archivo_out.close()

