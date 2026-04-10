def ordenar_archivo_si_es_necesario(path, ordenado):

    if ordenado.upper() == "N":
        print("Ordenando archivo...")

        archivo = open(path, "r")
        encabezado = archivo.readline()
        datos = []

        for linea in archivo:
            datos.append(linea.strip().split(","))

        archivo.close()

        # ORDENAMIENTO BURBUJA POR SUCURSAL
        n = len(datos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if datos[j][0] > datos[j + 1][0]:
                    aux = datos[j]
                    datos[j] = datos[j + 1]
                    datos[j + 1] = aux

        nuevo_path = "archivo_ordenado_temp.csv"
        archivo = open(nuevo_path, "w")
        archivo.write(encabezado)

        for fila in datos:
            archivo.write(",".join(fila) + "\n")

        archivo.close()

        return nuevo_path

    else:
        return path

path = input("Ingrese el path del archivo CSV: ")
ordenado = input("El archivo está ordenado? (Y/N): ")

path_final = ordenar_archivo_si_es_necesario(path, ordenado)



archivo = open(path_final, "r")
archivo.readline()
linea = archivo.readline()

TOTALIMP = 0
CANSUC = 0

while linea != "":
    datos = linea.strip().split(",")
    PRSUC = datos[0]
    sucursal_actual = PRSUC

    TOTSUC = 0
    max_importe = -1
    min_importe = 9999999999
    MYPROD = ""
    MNPRO = ""

    while linea != "" and PRSUC == sucursal_actual:
        producto_actual = datos[1]
        TOTPES = 0
        TOTUNI = 0

        while linea != "" and PRSUC == sucursal_actual and datos[1] == producto_actual:
            PRCANT = int(datos[4])
            PRPRE = float(datos[5])

            importe = PRCANT * PRPRE

            TOTUNI = TOTUNI + PRCANT
            TOTSUC = TOTSUC + PRCANT
            TOTPES = TOTPES + importe
            TOTALIMP = TOTALIMP + importe

            linea = archivo.readline()

            if linea != "":
                datos = linea.strip().split(",")
                PRSUC = datos[0]

        
        if TOTPES > max_importe:
            max_importe = TOTPES
            MYPROD = producto_actual

        if TOTPES < min_importe:
            min_importe = TOTPES
            MNPRO = producto_actual

    CANSUC = CANSUC + 1  

    print("Sucursal:", sucursal_actual,
          "Producto:", producto_actual,
          "TOTUNI:", TOTUNI,
          "TOTPES:", TOTPES)

    print("Sucursal:", sucursal_actual,
          "TOTSUC:", TOTSUC,
          "MYPROD:", MYPROD,
          "MYIMPOR:", max_importe,
          "MNPRO:", MNPRO,
          "MNIMPOR:", min_importe)

print("El total de sucursales del supermercado son:", CANSUC,
      "y la compra total en pesos es: $", TOTALIMP)

archivo.close()
