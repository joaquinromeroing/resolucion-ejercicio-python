def leer_csv(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    encabezado = archivo.readline()
    datos = []

    for linea in archivo:
        fila = linea.strip().split(",")
        datos.append(fila)

    archivo.close()
    return encabezado, datos



def burbuja(datos):
    n = len(datos)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Ordenamos por SUCURSAL (posición 0)
            if datos[j][0] > datos[j + 1][0]:
                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux

    return datos


def guardar_csv(nombre_archivo, encabezado, datos):
    archivo = open(nombre_archivo, "w")
    archivo.write(encabezado)

    for fila in datos:
        linea = ",".join(fila)
        archivo.write(linea + "\n")

    archivo.close()



entrada = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
salida = "COMPRAS_supermercado_ordenado.csv"

encabezado, datos = leer_csv(entrada)
datos_ordenados = burbuja(datos)
guardar_csv(salida, encabezado, datos_ordenados)

print("Archivo ordenado generado correctamente.")
