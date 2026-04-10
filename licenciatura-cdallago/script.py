# -----------------------------------------
# ORDENAMIENTO BURBUJA + CORTE DE CONTROL
# -----------------------------------------

# nombre del archivo de entrada
archivo_entrada = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"

# nombre del archivo ordenado que se va a generar
archivo_salida = "compras_ordenadas.csv"


# -----------------------------------------
# 1) LEER ARCHIVO DESORDENADO
# -----------------------------------------

archivo = open(archivo_entrada, "r")

lineas = archivo.readlines()

archivo.close()

encabezado = lineas[0]

datos = []

for linea in lineas[1:]:
    fila = linea.strip().split(",")
    datos.append(fila)


# -----------------------------------------
# 2) ORDENAR CON BURBUJA
# -----------------------------------------

n = len(datos)

for i in range(n):
    for j in range(0, n - i - 1):

        # ordenar por sucursal (columna 0)
        if datos[j][0] > datos[j + 1][0]:

            aux = datos[j]
            datos[j] = datos[j + 1]
            datos[j + 1] = aux


# -----------------------------------------
# 3) GUARDAR ARCHIVO ORDENADO
# -----------------------------------------

archivo = open(archivo_salida, "w")

archivo.write(encabezado)

for fila in datos:
    linea = ",".join(fila)
    archivo.write(linea + "\n")

archivo.close()

print("Archivo ordenado generado:", archivo_salida)


# -----------------------------------------
# 4) CORTE DE CONTROL
# -----------------------------------------

archivo = open(archivo_salida, "r")

next(archivo)  # saltear encabezado

sucursal_actual = None
total_cantidad = 0

for linea in archivo:

    fila = linea.strip().split(",")

    sucursal = fila[0]
    cantidad = int(fila[4])

    if sucursal_actual is None:
        sucursal_actual = sucursal

    if sucursal != sucursal_actual:

        print("Sucursal:", sucursal_actual)
        print("Total cantidad:", total_cantidad)
        print("--------------------------")

        sucursal_actual = sucursal
        total_cantidad = 0

    total_cantidad += cantidad


# último grupo
print("Sucursal:", sucursal_actual)
print("Total cantidad:", total_cantidad)

archivo.close()