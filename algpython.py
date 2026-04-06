import csv

archivo = open("compras_ordenado.csv", "r")
reader = csv.reader(archivo)

# leer segunda linea xq la primera no tiene datos.
next(reader)
fila = next(reader, None)

#total de sucursales
CANSUC = 0
#gasto total de todas las sucursales
TOTALIMP = 0

while fila is not None:
    #sucursal actual
    PRSUC = fila[0]

    #sumo 1 al total de sucursales
    CANSUC += 1

    print(f"\nSucursal: {PRSUC}")

    #total comprado en unidades
    TOTSUC = 0

    #producto mayor importe
    MYIMPOR = -1
    #producto menor importe
    MNIMPOR = float('inf')
    #producto mayor compra
    MYPROD = ""
    #Producto menor compra
    MNPROD = ""

    while fila is not None and fila[0] == PRSUC:
        #producto actual
        PRCOD = fila[1]

        #total comprado en unidades
        TOTUNI = 0
        #total comprado en pesos
        TOTPES = 0

        while fila is not None and fila[0] == PRSUC and fila[1] == PRCOD:

            #cantidad de producto
            PRCANT = int(fila[4])
            #precio del producto
            PRPRE = float(fila[5])
            
            #acumulo totales
            TOTUNI += PRCANT
            TOTPES += PRCANT * PRPRE

            fila = next(reader, None)

        print(f" Producto: {PRCOD} | Unidades: {TOTUNI} | Importe: {TOTPES}")

        TOTSUC += TOTPES

        #mayor compra
        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = PRCOD

        #Menor compra
        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD = PRCOD

    print(f"Total sucursal: {TOTSUC}")
    print(f"Mayor compra: {MYPROD} - {MYIMPOR}")
    print(f"Menor compra: {MNPROD} - {MNIMPOR}")

    TOTALIMP += TOTSUC

archivo.close()

print("\n=== TOTALES GENERALES ===")
print(f"Cantidad de sucursales: {CANSUC}")
print(f"Importe total: {TOTALIMP}")

