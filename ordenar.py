import csv

archivo = open("COMPRAS_supermercado_desordenado_solo_sucursal.csv", "r")
lector = csv.reader(archivo)

encabezado = next(lector)

filas = []
for fila in lector:
    filas.append(fila)

archivo.close()

# ORDENAMIENTO BURBUJA
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


# GUARDAR ARCHIVO ORDENADO
archivo = open("COMPRAS_supermercado_ordenado.csv", "w", newline="")
escritor = csv.writer(archivo)

escritor.writerow(encabezado)

for fila in filas:
    escritor.writerow(fila)

archivo.close()

print("archivo ordenado.")