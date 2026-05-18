import csv

def leer_archivo(nombre_archivo):

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    encabezado = lineas[0]
    datos = [linea.strip().split(",") for linea in lineas[1:]]

    return encabezado, datos


def ordenar_por_sucursal(datos):

    n = len(datos)

    for i in range(n):
        for j in range(0, n - i - 1):

            if datos[j][0] > datos[j + 1][0]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    return datos


def guardar_archivo(nombre_archivo, encabezado, datos):

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:

        archivo.write(encabezado)

        for fila in datos:
            archivo.write(",".join(fila) + "\n")


def calcular_totales_producto(datos, inicio, sucursal, producto):

    totuni = 0
    totpes = 0.0
    i = inicio

    while (
        i < len(datos)
        and datos[i]['PRSUC'] == sucursal
        and datos[i]['PRCOD'] == producto
    ):

        cantidad = int(datos[i]['PRCANT'])
        precio = float(datos[i]['PRPRE'])

        totuni += cantidad
        totpes += cantidad * precio

        i += 1

    return totuni, totpes, i


def actualizar_mayor_compra(producto, total_pesos, mayor_producto, mayor_importe):

    if total_pesos > mayor_importe:
        return producto, total_pesos

    return mayor_producto, mayor_importe


def actualizar_menor_compra(producto, total_pesos, menor_producto, menor_importe):

    if total_pesos < menor_importe:
        return producto, total_pesos

    return menor_producto, menor_importe


def procesar_sucursal(datos, inicio):

    sucursal = datos[inicio]['PRSUC']

    total_unidades = 0
    total_pesos_sucursal = 0.0

    mayor_producto = ""
    mayor_importe = -1

    menor_producto = ""
    menor_importe = float('inf')

    i = inicio

    while i < len(datos) and datos[i]['PRSUC'] == sucursal:

        producto = datos[i]['PRCOD']

        totuni, totpes, i = calcular_totales_producto(
            datos,
            i,
            sucursal,
            producto
        )

        total_unidades += totuni
        total_pesos_sucursal += totpes

        mayor_producto, mayor_importe = actualizar_mayor_compra(
            producto,
            totpes,
            mayor_producto,
            mayor_importe
        )

        menor_producto, menor_importe = actualizar_menor_compra(
            producto,
            totpes,
            menor_producto,
            menor_importe
        )

    resumen = {
        "sucursal": sucursal,
        "total_unidades": total_unidades,
        "total_pesos": total_pesos_sucursal,
        "mayor_producto": mayor_producto,
        "mayor_importe": mayor_importe,
        "menor_producto": menor_producto,
        "menor_importe": menor_importe
    }

    return resumen, i



def main():

    archivo_entrada = "COMPRAS_supermercado.csv"
    archivo_ordenado = "compras_ordenadas.csv"

    # FASE 1 ORDENAR
    encabezado, datos = leer_archivo(archivo_entrada)

    datos_ordenados = ordenar_por_sucursal(datos)

    guardar_archivo(archivo_ordenado, encabezado, datos_ordenados)

    # FASE 2 PROCESAR
    with open(archivo_ordenado, mode='r', encoding='utf-8') as archivo:
        datos_dict = list(csv.DictReader(archivo))

    i = 0
    total_general = 0.0

    while i < len(datos_dict):

        resumen, i = procesar_sucursal(datos_dict, i)

        total_general += resumen["total_pesos"]

        print("Sucursal:", resumen["sucursal"])
        print("Total unidades:", resumen["total_unidades"])
        print("Mayor compra:", resumen["mayor_producto"], resumen["mayor_importe"])
        print("Menor compra:", resumen["menor_producto"], resumen["menor_importe"])
        print("---------------------------")

    print("TOTAL GENERAL:", total_general)


if __name__ == "__main__":
    main()