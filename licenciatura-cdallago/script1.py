import csv


def cargar_datos(nombre_archivo):
    archivo = open(nombre_archivo, mode='r', encoding='utf-8')
    datos = list(csv.DictReader(archivo))
    archivo.close()
    return datos


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

        print(f"PRODUCTO: {producto} | TOTUNI: {totuni} | TOTPES: ${totpes:,.2f}")

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
    datos = cargar_datos('COMPRAS_supermercado.csv')

    i = 0
    cantidad_sucursales = 0
    total_general = 0.0

    while i < len(datos):

        resumen, i = procesar_sucursal(datos, i)

        cantidad_sucursales += 1
        total_general += resumen["total_pesos"]

        print("\n" + "-" * 30)
        print(f"SUCURSAL: {resumen['sucursal']}")
        print(f"TOTAL UNIDADES: {resumen['total_unidades']}")
        print(
            f"MAYOR COMPRA: {resumen['mayor_producto']} "
            f"(${resumen['mayor_importe']:,.2f})"
        )
        print(
            f"MENOR COMPRA: {resumen['menor_producto']} "
            f"(${resumen['menor_importe']:,.2f})"
        )
        print("-" * 30)

    print("\n" + "=" * 40)
    print(f"TOTAL SUCURSALES: {cantidad_sucursales}")
    print(f"TOTAL GENERAL: ${total_general:,.2f}")
    print("=" * 40)


main()