import csv

def orderList(archive):
    archivo_for_open = open(archive, "r")

    reader = csv.reader(archivo_for_open)
    next(reader)  

    datos = list(reader)

    archivo_for_open.close()

    n = len(datos)

    for i in range(n):
        for j in range(0, n-i-1):
            # chequea condicion y hace intercambio si lo necesita
            if datos[j][0] > datos[j+1][0]:
                temp = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = temp

    #una ves que la lista datos esta ordenada lo escribe en el nuevo archivo
    archivo_out = open("compras_ordenado.csv", "w", newline="")
    writer = csv.writer(archivo_out)

    #escribo la primera linea de indices
    writer.writerow(["PRSUC","PRCOD","PRFEC","PRPROV","PRCANT","PRPRE"])

    #escribo los datos ordenados
    writer.writerows(datos)

    #cierro 
    archivo_out.close()
    
print("Ingrese el nombre del archivo a ordenar (con extension .csv):")

archivo_nombre = input()

print("El archivo esta ordenado? (s/n)")    
respuesta = input()

if respuesta.lower() == 'n':
    orderList(archivo_nombre)


archivo = open(archivo_nombre, "r")
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

