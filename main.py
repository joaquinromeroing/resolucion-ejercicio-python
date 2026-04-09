import csv

def bubble_sort(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (datos[j][0], datos[j][1]) > (datos[j + 1][0], datos[j + 1][1]):
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos

def ordenar_y_guardar_temporal(path_entrada):
    with open(path_entrada, "r", encoding="utf-8") as archivo:
        lector = list(csv.reader(archivo))

    encabezado = lector[0]
    datos = lector[1:]

    datos_ordenados = bubble_sort(datos)

    path_temporal = "archivo_temporal_ordenado.csv"
    with open(path_temporal, "w", newline="", encoding="utf-8") as archivo_temp:
        writer = csv.writer(archivo_temp)
        writer.writerow(encabezado)
        writer.writerows(datos_ordenados)

    return path_temporal

def procesar_archivo(path_csv):
    archivo = open(path_csv, "r", encoding="utf-8")
    lector = csv.reader(archivo)
    next(lector)

    registros = list(lector)
    n = len(registros)
    i = 0

    TOTALIMP = 0
    CANSUC = 0

    while i < n:
        sucursal_actual = registros[i][0]
        TOTSUC = 0
        CANSUC += 1

        primera_vez = True

        print(f"\nSUCURSAL: {sucursal_actual}")

        while i < n and registros[i][0] == sucursal_actual:
            producto_actual = registros[i][1]
            TOTUNI = 0
            TOTPES = 0

            while i < n and registros[i][0] == sucursal_actual and registros[i][1] == producto_actual:
                cantidad = int(registros[i][4])
                precio = float(registros[i][5])
                importe = cantidad * precio

                TOTUNI += cantidad
                TOTPES += importe

                i += 1

            print(f"Producto: {producto_actual} - Total unidades: {TOTUNI} - Total pesos: {TOTPES:.2f}")

            TOTSUC += TOTUNI
            TOTALIMP += TOTPES

            if primera_vez:
                MYPROD = producto_actual
                MYIMPOR = TOTPES
                MNPRO = producto_actual
                MNIMPOR = TOTPES
                primera_vez = False
            else:
                if TOTPES > MYIMPOR:
                    MYPROD = producto_actual
                    MYIMPOR = TOTPES

                if TOTPES < MNIMPOR:
                    MNPRO = producto_actual
                    MNIMPOR = TOTPES

        print(f"Total unidades sucursal: {TOTSUC}")
        print(f"Mayor compra en pesos: {MYPROD} - {MYIMPOR:.2f}")
        print(f"Menor compra en pesos: {MNPRO} - {MNIMPOR:.2f}")

    print("\nTOTALES GENERALES")
    print(f"Cantidad de sucursales: {CANSUC}")
    print(f"Importe total de todas las sucursales: {TOTALIMP:.2f}")

    archivo.close()

def menu():
    path_csv = input("Indique el path del csv: ")
    ordenado = input("El archivo esta ordenado? Y/N: ").strip().upper()

    if ordenado == "N":
        path_csv = ordenar_y_guardar_temporal(path_csv)
        print(f"Se genero el archivo temporal ordenado: {path_csv}")
        procesar_archivo(path_csv)
    elif ordenado == "Y":
        procesar_archivo(path_csv)
    else:
        print("Opcion invalida. Debe ingresar Y o N.")

if __name__ == "__main__":
    menu()