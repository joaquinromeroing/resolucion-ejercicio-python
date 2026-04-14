import os

CANSUC   = 0
TOTALIMP = 0.0

script_dir = os.path.dirname(os.path.abspath(__file__))
archivo = open(os.path.join(script_dir, "datos_ordenados.csv"), "r")
salida  = open(os.path.join(script_dir, "salida.txt"), "w")
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

        texto = (f"  Sucursal: {sucursal_actual} | Producto: {producto_actual} | "
                 f"Unidades: {TOTUNI} | Importe: ${TOTPES:.2f}")
        print(texto)
        salida.write(texto + "\n")

        TOTSUC += TOTPES

        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD  = producto_actual

        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD  = producto_actual

    TOTALIMP += TOTSUC
    texto1 = f"\nSucursal: {sucursal_actual} — Total importe: ${TOTSUC:.2f}"
    texto2 = f"  Mayor importe: {MYPROD} — ${MYIMPOR:.2f}"
    texto3 = f"  Menor importe: {MNPROD} — ${MNIMPOR:.2f}"
    texto4 = "─" * 50
    print(texto1)
    print(texto2)
    print(texto3)
    print(texto4)
    salida.write(texto1 + "\n")
    salida.write(texto2 + "\n")
    salida.write(texto3 + "\n")
    salida.write(texto4 + "\n")

archivo.close()

texto5 = f"\nTotal de sucursales procesadas : {CANSUC}"
texto6 = f"Importe total general          : ${TOTALIMP:.2f}"
print(texto5)
print(texto6)
salida.write(texto5 + "\n")
salida.write(texto6 + "\n")
salida.close()