import csv

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
        mnimpor = 10000000
        cansuc += 1

        while i < len(registros) and registros[i][0] == sucursal_actual:
            producto_actual = registros[i][1]

            totuni = 0
            totpes = 0

            while i < len(registros) and registros[i][0] == sucursal_actual and registros[i][1] == producto_actual:
                cantidad = int(registros[i][4])
                precio = float(registros[i][5])

                totuni += (cantidad)
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
procesar_compras("COMPRAS_supermercado.csv")