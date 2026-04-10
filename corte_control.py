import csv

archivo = "COMPRAS_supermercado.csv"


def moneda(x):
    return f"${x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def corte_control(nombre_archivo):
    por_producto = {}
    tot_unidades_sucursal = {}
    pesos_por_sucursal_producto = {}
    total_imp = 0

    with open(nombre_archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        for fila in lector:
            sucursal = fila["PRSUC"]
            producto = fila["PRCOD"]
            cantidad = int(fila["PRCANT"])
            precio = float(fila["PRPRE"])
            importe = cantidad * precio

            clave = (sucursal, producto)

            if clave not in por_producto:
                por_producto[clave] = [0, 0]

            por_producto[clave][0] += cantidad
            por_producto[clave][1] += importe

            if sucursal not in tot_unidades_sucursal:
                tot_unidades_sucursal[sucursal] = 0

            tot_unidades_sucursal[sucursal] += cantidad

            if sucursal not in pesos_por_sucursal_producto:
                pesos_por_sucursal_producto[sucursal] = {}

            if producto not in pesos_por_sucursal_producto[sucursal]:
                pesos_por_sucursal_producto[sucursal][producto] = 0

            pesos_por_sucursal_producto[sucursal][producto] += importe

            total_imp += importe

    ancho_sucursal = max(len("Sucursal"), max(len(str(s)) for s in tot_unidades_sucursal))
    ancho_producto = max(len("Producto"), max(len(str(clave[1])) for clave in por_producto))

    print()
    print("=" * 90)
    print("A) POR PRODUCTO".center(90))
    print("=" * 90)
    print(
        f'{"Sucursal":<{ancho_sucursal}}   '
        f'{"Producto":<{ancho_producto}}   '
        f'{"TOTUNI":>10}   '
        f'{"TOTPES":>16}'
    )
    print("-" * 90)

    for clave in sorted(por_producto):
        sucursal, producto = clave
        totuni = por_producto[clave][0]
        totpes = por_producto[clave][1]

        print(
            f'{sucursal:<{ancho_sucursal}}   '
            f'{producto:<{ancho_producto}}   '
            f'{totuni:>10}   '
            f'{moneda(totpes):>16}'
        )

    print()
    print("=" * 90)
    print("B) POR SUCURSAL".center(90))
    print("=" * 90)

    for sucursal in sorted(tot_unidades_sucursal):
        productos = pesos_por_sucursal_producto[sucursal]

        mayor_producto = None
        mayor_importe = None
        menor_producto = None
        menor_importe = None

        for producto in productos:
            importe = productos[producto]

            if mayor_importe is None or importe > mayor_importe:
                mayor_importe = importe
                mayor_producto = producto

            if menor_importe is None or importe < menor_importe:
                menor_importe = importe
                menor_producto = producto

        print("-" * 90)
        print(f"Sucursal:           {sucursal}")
        print(f"Total unidades:     {tot_unidades_sucursal[sucursal]}")
        print(f"Producto mayor:     {mayor_producto}")
        print(f"Importe mayor:      {moneda(mayor_importe)}")
        print(f"Producto menor:     {menor_producto}")
        print(f"Importe menor:      {moneda(menor_importe)}")

    print()
    print("=" * 90)
    print("C) TOTAL GENERAL".center(90))
    print("=" * 90)
    print(f"Cantidad sucursales: {len(tot_unidades_sucursal)}")
    print(f"Importe total:       {moneda(total_imp)}")
    print("=" * 90)
    print()


if __name__ == "__main__":
    corte_control(archivo)