
# reviso el archivo

archivo = open('Tp1/COMPRAS_supermercado.csv', 'r', encoding='utf-8')

for i in range(6):
    linea = archivo.readline()
    print(linea.strip()) 

archivo.close()

# whiles anidados

archivo = open('Tp1/COMPRAS_supermercado.csv', 'r', encoding='utf-8')
encabezado = archivo.readline()
#Primeros acumuladores, de sucursales.
CANSUC = 0
TOTALIMP = 0.0

linea = archivo.readline()

while linea != "":
    datos = linea.strip().split(',')
    sucursal_actual = datos[0]
    #suma de sucursales
    CANSUC = CANSUC + 1
    #total unidades de sucursales
    TOTSUC = 0
    #acumuladores de sucursales, sobre prod e importe
    MYIMPOR = 0.0
    MYPROD = ""
    MNIMPOR = 0.0
    MNPRO = ""
    
    
    primer_producto = True 
    
    print("SUCURSAL:", sucursal_actual)
    
    while linea != "" and datos[0] == sucursal_actual:
        producto_actual = datos[1]
        
        TOTUNI = 0
        TOTPES = 0.0
        
        while linea != "" and datos[0] == sucursal_actual and datos[1] == producto_actual:
            cantidad = int(datos[4])
            precio = float(datos[5])
            importe = cantidad * precio
            #acumuladores de prod
            TOTUNI = TOTUNI + cantidad
            TOTPES = TOTPES + importe
            
            linea = archivo.readline()
            if linea != "":
                datos = linea.strip().split(',')
        
        print("Prod:", producto_actual, " Unidades:", TOTUNI, " Pesos: $", round(TOTPES, 2))
        #acumuladores finales
        TOTSUC = TOTSUC + TOTUNI
        TOTALIMP = TOTALIMP + TOTPES
        
        # aca arrancamos la comparacion de mayor/menor importe/producto

        #esto es solo para el primer producto, va a ocupar las primeras variables
        if primer_producto == True:
            
            MYIMPOR = TOTPES
            MNIMPOR = TOTPES
            MYPROD = producto_actual
            MNPRO = producto_actual
            
            #aca pasa a false y no va entrar ningun otro, queremos que se comparen con el producto establecido antes
            primer_producto = False 
        else:
            #a partir del segundo producto, comparamos normalmente
            if TOTPES > MYIMPOR:
                MYIMPOR = TOTPES
                MYPROD = producto_actual
                
            if TOTPES < MNIMPOR:
                MNIMPOR = TOTPES
                MNPRO = producto_actual

    print("RESUMEN SUCURSAL", sucursal_actual)
    print("Total unidades (TOTSUC):", TOTSUC)
    print("Mayor compra: Prod.", MYPROD, "con $", round(MYIMPOR, 2))
    print("Menor compra: Prod.", MNPRO, "con $", round(MNIMPOR, 2))


print("TOTALES GENERALES")
print("Total sucursales (CANSUC):", CANSUC)
print("Compra total pesos (TOTALIMP): $", round(TOTALIMP, 2))

archivo.close()