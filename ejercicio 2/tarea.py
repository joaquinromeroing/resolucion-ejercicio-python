CANSUC   = 0
TOTALIMP = 0.0

archivo = open("/home/kali/Desktop/Austral/resolucion-ejercicio-python/ejercicio 2/datos_ordenados.csv", "r")
archivo.readline()          # saltear encabezado
linea = archivo.readline()

while linea:
    campo          = linea.strip().split(",")
    sucursal_actual = campo[0]

    TOTSUC   = 0.0
    MYPROD   = ""
    MYIMPOR  = 0.0
    MNPROD   = ""
    MNIMPOR  = float("inf")
    CANSUC  += 1

    while linea and campo[0] == sucursal_actual:
        producto_actual = campo[1]
        TOTUNI = 0
        TOTPES = 0.0

        while linea and campo[0] == sucursal_actual and campo[1] == producto_actual:
            cantidad = int(campo[4])
            precio   = float(campo[5])
            TOTUNI  += cantidad
            TOTPES  += cantidad * precio

            linea = archivo.readline()
            if linea:
                campo = linea.strip().split(",")

        print(f"  Sucursal: {sucursal_actual} | Producto: {producto_actual} | "
              f"Unidades: {TOTUNI} | Importe: ${TOTPES:.2f}")

        TOTSUC += TOTPES

        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD  = producto_actual

        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD  = producto_actual

    TOTALIMP += TOTSUC
    print(f"\nSucursal: {sucursal_actual} — Total importe: ${TOTSUC:.2f}")
    print(f"  Mayor importe: {MYPROD} — ${MYIMPOR:.2f}")
    print(f"  Menor importe: {MNPROD} — ${MNIMPOR:.2f}")
    print("─" * 50)

archivo.close()

print(f"\nTotal de sucursales procesadas : {CANSUC}")
print(f"Importe total general          : ${TOTALIMP:.2f}")