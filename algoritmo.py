import csv

def ordenar_burbuja(registros):
    n = len(registros)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            actual = registros[j]
            siguiente = registros[j + 1]

            if (actual[0], actual[1]) > (siguiente[0], siguiente[1]):
                aux = registros[j]
                registros[j] = registros[j + 1]
                registros[j + 1] = aux

    return registros


def procesar_compras(nombre_archivo):
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        registros = list(lector)

    if not registros:
        print("El archivo está vacío.")
        return

    i = 0
    cansuc = 0
    totalimp = 0

    while i < len(registros):
        sucursal_actual = registros[i][0]
        print(f"\nSucursal: {sucursal_actual}")

        totsuc = 0
        totsucimp = 0
        myprod = None
        myimpor = 0
        mnprod = None
        mnimpor = float("inf")
        cansuc += 1

        while i < len(registros) and registros[i][0] == sucursal_actual:
            producto_actual = registros[i][1]

            totuni = 0
            totpes = 0

            while i < len(registros) and registros[i][0] == sucursal_actual and registros[i][1] == producto_actual:
                cantidad = int(registros[i][4])
                precio = float(registros[i][5])

                totuni += cantidad
                totpes += cantidad * precio

                i += 1

            print(f"Producto {producto_actual} - TOTUNI: {totuni} - TOTPES: ${totpes:.2f}")

            totsuc += totuni
            totsucimp += totpes

            if totpes > myimpor:
                myimpor = totpes
                myprod = producto_actual

            if totpes < mnimpor:
                mnimpor = totpes
                mnprod = producto_actual

        print(f"Total comprado en unidades: {totsuc}")
        print(f"Producto de mayor compra: {myprod} - Importe: ${myimpor:.2f}")
        print(f"Producto de menor compra: {mnprod} - Importe: ${mnimpor:.2f}")

        totalimp += totsucimp

    print(f"Total de sucursales del supermercado: {cansuc} - Importe total: ${totalimp:.2f}")


path = input("Indique el path del csv: ")
ordenado = input("El archivo está ordenado? (Y/N): ").strip().upper()

if ordenado == "N":
    with open(path, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector)
        registros = list(lector)

    if not registros:
        print("El archivo está vacío.")
    else:
        registros_ordenados = ordenar_burbuja(registros)
        archivo_ordenado = "archivo_ordenado_temporal.csv"

        with open(archivo_ordenado, "w", newline="", encoding="utf-8") as salida:
            escritor = csv.writer(salida)
            escritor.writerow(encabezado)
            escritor.writerows(registros_ordenados)

        print(f"\nSe generó el archivo ordenado: {archivo_ordenado}")
        print("Se procesará ese archivo.\n")

        procesar_compras(archivo_ordenado)

elif ordenado == "Y":
    procesar_compras(path)

else:
    print("Opción inválida. Debe ingresar Y o N.")