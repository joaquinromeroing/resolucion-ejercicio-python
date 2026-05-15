import csv

# ================================
# FUNCIONES AUXILIARES (AGREGADO)
# ================================

# cálculo de importe
def calcular_importe(cantidad, precio):
    return cantidad * precio

# cálculo de totales por producto
def calcular_totales_producto(filas_producto):
    TOTUNI = 0
    TOTPES = 0
    for fila in filas_producto:
        PRCANT = int(fila[4])
        PRPRE = float(fila[5])
        TOTUNI += PRCANT
        TOTPES += calcular_importe(PRCANT, PRPRE)  # MODIFICADO: antes era PRCANT * PRPRE directo
    return TOTUNI, TOTPES

# lógica de máximo
def actualizar_maximo(importe, maximo_actual, producto, producto_actual):
    if importe > maximo_actual:
        return importe, producto
    return maximo_actual, producto_actual

# lógica de mínimo
def actualizar_minimo(importe, minimo_actual, producto, producto_actual):
    if importe < minimo_actual:
        return importe, producto
    return minimo_actual, producto_actual


# ================================
# CODIGO DEL ARCHIVO ejbubble.py
# ================================
def ordenar_csv(path_entrada, path_salida):
    archivo = open(path_entrada, "r")
    reader = csv.reader(archivo)
    next(reader)

    datos = list(reader)
    archivo.close()

    n = len(datos)

    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j][0] > datos[j + 1][0]:
                temp = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = temp

    archivo_out = open(path_salida, "w", newline="")
    writer = csv.writer(archivo_out)
    writer.writerow(["PRSUC", "PRCOD", "PRFEC", "PRPROV", "PRCANT", "PRPRE"])
    writer.writerows(datos)
    archivo_out.close()


# ================================
# ALGORITMO PRINCIPAL
# ================================
def procesar_csv(path_archivo):
    archivo = open(path_archivo, "r")
    reader = csv.reader(archivo)

    next(reader)
    fila = next(reader, None)

    CANSUC = 0
    TOTALIMP = 0

    while fila is not None:
        PRSUC = fila[0]
        CANSUC += 1

        print(f"\nSucursal: {PRSUC}")

        TOTSUC = 0
        MYIMPOR = -1
        MNIMPOR = float("inf")
        MYPROD = ""
        MNPROD = ""

        while fila is not None and fila[0] == PRSUC:
            PRCOD = fila[1]
            filas_producto = []  # AGREGADO: lista para acumular filas del producto

            while fila is not None and fila[0] == PRSUC and fila[1] == PRCOD:
                filas_producto.append(fila)  # AGREGADO: acumulamos la fila
                fila = next(reader, None)
                # ELIMINADO: PRCANT = int(fila[4])
                # ELIMINADO: PRPRE = float(fila[5])
                # ELIMINADO: TOTUNI += PRCANT
                # ELIMINADO: TOTPES += PRCANT * PRPRE

            TOTUNI, TOTPES = calcular_totales_producto(filas_producto)  # MODIFICADO: antes el cálculo estaba inline

            print(f"Producto: {PRCOD} | Unidades: {TOTUNI} | Importe: {TOTPES}")

            TOTSUC += TOTUNI
            TOTALIMP += TOTPES

            # MODIFICADO: antes eran dos if inline, ahora se llaman las funciones
            MYIMPOR, MYPROD = actualizar_maximo(TOTPES, MYIMPOR, PRCOD, MYPROD)
            MNIMPOR, MNPROD = actualizar_minimo(TOTPES, MNIMPOR, PRCOD, MNPROD)
            # ELIMINADO: if TOTPES > MYIMPOR: MYIMPOR = TOTPES / MYPROD = PRCOD
            # ELIMINADO: if TOTPES < MNIMPOR: MNIMPOR = TOTPES / MNPROD = PRCOD

        print(f"Total sucursal: {TOTSUC}")
        print(f"Mayor compra: {MYPROD} - {MYIMPOR}")
        print(f"Menor compra: {MNPROD} - {MNIMPOR}")

    archivo.close()

    print("\n=== TOTALES GENERALES ===")
    print(f"Cantidad de sucursales: {CANSUC}")
    print(f"Importe total: {TOTALIMP}")


# ================================
# ================================
if __name__ == "__main__":
    path_csv = input("Indique el path del csv: ")
    ordenado = input("El archivo esta ordenado? Y/N: ").upper()

    if ordenado == "N":
        archivo_temporal = "compras_ordenado.csv"
        ordenar_csv(path_csv, archivo_temporal)
        procesar_csv(archivo_temporal)
    else:
        procesar_csv(path_csv)