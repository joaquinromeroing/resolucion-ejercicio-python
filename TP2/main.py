import csv
from bubble_sort import bubble_sort

# -------- ORDENAMIENTO --------

with open("TP2/COMPRAS_supermercado_desordenado_solo_sucursal.csv") as f:
    reader = list(csv.reader(f))
    header = reader[0]
    data = reader[1:]

data = bubble_sort(data)

with open("TP2/ordenado.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("Archivo ordenado generado.\n")

# -------- CORTE DE CONTROL --------

archivo = open('TP2/ordenado.csv', 'r', encoding='utf-8')
encabezado = archivo.readline()

CANSUC = 0
TOTALIMP = 0.0

linea = archivo.readline()

while linea != "":
    datos = linea.strip().split(',')
    sucursal_actual = datos[0]

    CANSUC += 1
    TOTSUC = 0

    MYIMPOR = 0.0
    MYPROD = ""
    MNIMPOR = 0.0
    MNPRO = ""

    primer_producto = True

    print("SUCURSAL:", sucursal_actual)

    while linea != "" and datos[0] == sucursal_actual:
        producto_actual = datos[1]

        TOTUNI = 0
        TOTPES = 0.0

        while linea != "" and datos[0] == sucursal_actual and datos[1] == producto_actual:
            cantidad = int(datos[4])
            precio = float(datos[5])
            importe = cantidad * precio

            TOTUNI += cantidad
            TOTPES += importe

            linea = archivo.readline()
            if linea != "":
                datos = linea.strip().split(',')

        print("Prod:", producto_actual, " Unidades:", TOTUNI, " Pesos: $", round(TOTPES, 2))

        TOTSUC += TOTUNI
        TOTALIMP += TOTPES

        if primer_producto:
            MYIMPOR = TOTPES
            MNIMPOR = TOTPES
            MYPROD = producto_actual
            MNPRO = producto_actual
            primer_producto = False
        else:
            if TOTPES > MYIMPOR:
                MYIMPOR = TOTPES
                MYPROD = producto_actual

            if TOTPES < MNIMPOR:
                MNIMPOR = TOTPES
                MNPRO = producto_actual

    print("RESUMEN SUCURSAL", sucursal_actual)
    print("Total unidades:", TOTSUC)
    print("Mayor compra:", MYPROD, MYIMPOR)
    print("Menor compra:", MNPRO, MNIMPOR)
    print("-------------")

print("TOTALES GENERALES")
print("Total sucursales:", CANSUC)
print("Total importes:", round(TOTALIMP, 2))

archivo.close()