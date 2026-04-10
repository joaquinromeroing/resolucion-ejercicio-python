import csv
import os
import tempfile

ARCHIVO_POR_DEFECTO = "COMPRAS_supermercado.csv"
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CAMPOS_ORDEN = ("PRSUC", "PRCOD", "PRFEC", "PRPROV")


def moneda(x):
    return f"${x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def resolver_path(nombre_archivo):
    nombre_archivo = nombre_archivo.strip()

    if not nombre_archivo:
        nombre_archivo = ARCHIVO_POR_DEFECTO

    if os.path.isabs(nombre_archivo):
        return nombre_archivo

    return os.path.join(DIRECTORIO_BASE, nombre_archivo)


def leer_csv(nombre_archivo):
    with open(nombre_archivo, newline="", encoding="utf-8-sig") as f:
        lector = csv.reader(f)
        encabezado = next(lector)
        filas = [fila for fila in lector]

    return encabezado, filas


def clave_ordenacion(fila, indices):
    return tuple(fila[indice] for indice in indices)


def ordenar_burbuja(filas, indices):
    n = len(filas)

    for pasada in range(n - 1):
        hubo_cambio = False

        for i in range(n - 1 - pasada):
            if clave_ordenacion(filas[i], indices) > clave_ordenacion(filas[i + 1], indices):
                filas[i], filas[i + 1] = filas[i + 1], filas[i]
                hubo_cambio = True

        if not hubo_cambio:
            break

    return filas


def grabar_csv(nombre_archivo, encabezado, filas):
    with open(nombre_archivo, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f)
        escritor.writerow(encabezado)
        escritor.writerows(filas)


def generar_archivo_temporal_ordenado(nombre_archivo):
    encabezado, filas = leer_csv(nombre_archivo)
    indices = [encabezado.index(campo) for campo in CAMPOS_ORDEN]
    filas_ordenadas = ordenar_burbuja(filas, indices)

    archivo_temporal = tempfile.NamedTemporaryFile(
        mode="w",
        delete=False,
        newline="",
        suffix=".csv",
        prefix="compras_ordenadas_",
        dir=os.path.dirname(nombre_archivo) or DIRECTORIO_BASE,
        encoding="utf-8-sig",
    )
    ruta_temporal = archivo_temporal.name
    archivo_temporal.close()

    grabar_csv(ruta_temporal, encabezado, filas_ordenadas)
    return ruta_temporal


def solicitar_path_csv():
    while True:
        nombre_archivo = input(f"Indique el path del csv [{ARCHIVO_POR_DEFECTO}]: ")
        ruta = resolver_path(nombre_archivo)

        if os.path.isfile(ruta):
            return ruta

        print("No se encontro el archivo indicado. Intente nuevamente.")


def solicitar_si_esta_ordenado():
    while True:
        respuesta = input("El archivo esta ordenado (Y/N): ").strip().upper()

        if respuesta in {"Y", "N"}:
            return respuesta == "Y"

        print("Ingrese Y para si o N para no.")


def preparar_archivo(nombre_archivo, esta_ordenado):
    if esta_ordenado:
        return nombre_archivo, None

    ruta_temporal = generar_archivo_temporal_ordenado(nombre_archivo)
    print()
    print(f"Se genero un archivo temporal ordenado: {ruta_temporal}")
    print()
    return ruta_temporal, ruta_temporal


def corte_control(nombre_archivo):
    por_producto = {}
    tot_unidades_sucursal = {}
    pesos_por_sucursal_producto = {}
    total_imp = 0

    with open(nombre_archivo, newline="", encoding="utf-8-sig") as f:
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

    if not por_producto:
        print()
        print("El archivo no contiene registros para procesar.")
        print()
        return

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


def main():
    nombre_archivo = solicitar_path_csv()
    esta_ordenado = solicitar_si_esta_ordenado()
    archivo_a_procesar, archivo_temporal = preparar_archivo(nombre_archivo, esta_ordenado)

    try:
        corte_control(archivo_a_procesar)
    finally:
        if archivo_temporal and os.path.exists(archivo_temporal):
            os.remove(archivo_temporal)
            print(f"Se elimino el archivo temporal: {archivo_temporal}")


if __name__ == "__main__":
    main()
