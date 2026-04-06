def ordenar_archivo(origen, destino):
    archivo = open(origen, "r")
    lineas = archivo.readlines()
    archivo.close()


    cabecera = lineas[0]
    lineas = lineas[1:]


    datos = [linea.strip().split(",") for linea in lineas if linea.strip() != ""]

    n = len(datos)


    for i in range(n):
        for j in range(0, n - i - 1):
            a = datos[j]
            b = datos[j + 1]

            if (a[0] > b[0] or
               (a[0] == b[0] and a[1] > b[1]) or
               (a[0] == b[0] and a[1] == b[1] and a[2] > b[2]) or
               (a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] > b[3])):
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    archivo = open(destino, "w")
    archivo.write(cabecera)

    for fila in datos:
        archivo.write(",".join(fila) + "\n")

    archivo.close()


def procesar_archivo(nombre):
    archivo = open(nombre, "r")

    archivo.readline()  # 🔹 saltear cabecera
    linea = archivo.readline()

    CANSUC = 0
    TOTALIMP = 0

    while linea != "":
        datos = linea.strip().split(",")

        if len(datos) < 6:
            linea = archivo.readline()
            continue

        sucursal = datos[0]
        producto = datos[1]
        cantidad = int(datos[4])
        precio = float(datos[5])

        sucursal_actual = sucursal

        TOTSUC = 0
        total_sucursal_pesos = 0

        MYPROD = ""
        MYIMPOR = 0

        MNPROD = ""
        MNIMPOR = 0
        primer_producto = True

        print("\nSucursal:", sucursal_actual)


        while linea != "" and sucursal == sucursal_actual:

            producto_actual = producto

            TOTUNI = 0
            TOTPES = 0

            
            while linea != "" and sucursal == sucursal_actual and producto == producto_actual:

                importe = cantidad * precio

                TOTUNI += cantidad
                TOTPES += importe

                linea = archivo.readline()

                if linea != "":
                    datos = linea.strip().split(",")

                    if len(datos) < 6:
                        linea = archivo.readline()
                        continue

                    sucursal = datos[0]
                    producto = datos[1]
                    cantidad = int(datos[4])
                    precio = float(datos[5])

            print("Producto:", producto_actual, "Unidades:", TOTUNI, "Importe:", TOTPES)

            TOTSUC += TOTUNI
            total_sucursal_pesos += TOTPES

            if primer_producto:
                MYIMPOR = TOTPES
                MYPROD = producto_actual

                MNIMPOR = TOTPES
                MNPROD = producto_actual

                primer_producto = False
            else:
                if TOTPES > MYIMPOR:
                    MYIMPOR = TOTPES
                    MYPROD = producto_actual

                if TOTPES < MNIMPOR:
                    MNIMPOR = TOTPES
                    MNPROD = producto_actual

        print("Total unidades sucursal:", TOTSUC)
        print("Producto mayor compra:", MYPROD, MYIMPOR)
        print("Producto menor compra:", MNPROD, MNIMPOR)

        CANSUC += 1
        TOTALIMP += total_sucursal_pesos

    archivo.close()


    print("\n===== TOTALES GENERALES =====")
    print("Cantidad de sucursales:", CANSUC)
    print("Importe total:", TOTALIMP)


ordenar_archivo("COMPRAS_desordenado.csv", "COMPRAS_ordenado.csv")
procesar_archivo("COMPRAS_ordenado.csv")