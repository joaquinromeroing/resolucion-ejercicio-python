import csv

archivo = open("COMPRAS_supermercado_desordenado_solo_sucursal.csv", "r")

reader = csv.reader(archivo)
next(reader)  # leer segunda linea xq la primera no tiene datos.

#guarda los datos en una nueva lista
datos = list(reader)

#cierro archivo pq al tener los datos guardados en la nueva lista ya no lo necesito
archivo.close()

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
