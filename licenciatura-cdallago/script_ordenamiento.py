def leer_archivo(nombre_archivo):

    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    encabezado = lineas[0]

    datos = []

    for linea in lineas[1:]:
        fila = linea.strip().split(",")
        datos.append(fila)

    return encabezado, datos


def ordenar_por_sucursal(datos):

    n = len(datos)

    for i in range(n):

        for j in range(0, n - i - 1):

            if datos[j][0] > datos[j + 1][0]:

                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux

    return datos


def guardar_archivo(nombre_archivo, encabezado, datos):

    with open(nombre_archivo, "w") as archivo:

        archivo.write(encabezado)

        for fila in datos:
            linea = ",".join(fila)
            archivo.write(linea + "\n")


def calcular_totales_por_sucursal(datos):

    resultados = {}

    for fila in datos:

        sucursal = fila[0]
        cantidad = int(fila[4])

        if sucursal not in resultados:
            resultados[sucursal] = 0

        resultados[sucursal] += cantidad

    return resultados


def mostrar_resultados(resultados):

    for sucursal, total in resultados.items():

        print("Sucursal:", sucursal)
        print("Total cantidad:", total)
        print("--------------------------")


def main():

    archivo_entrada = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
    archivo_salida = "compras_ordenadas.csv"

    encabezado, datos = leer_archivo(archivo_entrada)

    datos_ordenados = ordenar_por_sucursal(datos)

    guardar_archivo(
        archivo_salida,
        encabezado,
        datos_ordenados
    )

    print("Archivo ordenado generado:", archivo_salida)

    resultados = calcular_totales_por_sucursal(datos_ordenados)

    mostrar_resultados(resultados)


if __name__ == "__main__":
    main()