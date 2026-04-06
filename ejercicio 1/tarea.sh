#!/bin/python3

CANSUC = 0
TOTALIMP = 0

archivo = open("compras.csv", "r")
archivo.readline()

linea = archivo.readline()

while linea:
    campo = linea.strip().split(",")
    sucursal_actual = campo[0]

    TOTSUC = 0
    MYPROD = ""
    MYIMPOR = 0
    MNPROD = ""
    MNIMPOR = float("inf")

    CANSUC += 1
    
    while linea and campo[0] == sucursal_actual:
        producto_actual = campo[1]

        TOTUNI = 0
        TOTPES = 0 

        while linea and campo[0] == sucursal_actual and campo[1] == producto_actual:
            cantidad = int(campo[4])
            precio  = float(campo[5])

            TOTUNI += cantidad
            TOTPES += cantidad * precio

            linea = archivo.readline()
            if linea:
                campo = linea.strip().split(",")
        print(f"Sucursal: {sucursal_actual} - Productos: {producto_actual}- Unidades: {TOTUNI} - Pesos {TOTPES:.2f}")
        
        TOTSUC += TOTPES

        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = producto_actual

        if TOTPES < MNIMPOR: 
            MNIMPOR = TOTPES
            MNPROD = producto_actual

    TOTALIMP += TOTSUC
    print(f"Sucursal: {sucursal_actual} - Total unidades sucursal: {TOTSUC:.2f}")
    print(f"  Mayor compra: {MYPROD} - ${MYIMPOR:.2f}")                                                                                                                 
    print(f"  Menor compra: {MNPROD} - ${MNIMPOR:.2f}")                                                                                                                 
    print("---") 

archivo.close()                                                                                                                                                      
                                                                                                                                                                          
print(f"Total de sucursales: {CANSUC}")                                                                                                                              
print(f"Compra total en pesos: {TOTALIMP:.2f}")   

