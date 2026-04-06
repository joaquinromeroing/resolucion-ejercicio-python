archivo = open("COMPRAS_supermercado.csv", "r")
archivo.readline()
linea = archivo.readline()

TOTALIMP = 0
CANSUC = 0

while linea != "":
    datos = linea.strip().split(",")
    PRSUC = datos[0]
    sucursal_actual = PRSUC

    TOTSUC = 0 # total comprado en unidades
    max_importe = -1
    min_importe = 9999999999
    MYPROD = ""   #producto de mayor 
    MNPRO = ""# producto de mayor compra en peso

    while linea != "" and PRSUC == sucursal_actual:
        producto_actual = datos[1]
        TOTPES = 0
        TOTUNI = 0
        while linea != "" and PRSUC == sucursal_actual and datos[1] == producto_actual:
               PRCANT = int(datos[4])
               PRPRE = float(datos[5])

               importe = PRCANT * PRPRE
               
               TOTUNI=TOTUNI + PRCANT
               TOTSUC = TOTSUC + PRCANT
               TOTPES = TOTPES + importe # total comprado en peso
               TOTALIMP = TOTALIMP + importe #compra total de todas las sucu
               
               linea = archivo.readline()
            
               if linea != "":
                    datos = linea.strip().split(",")
                    PRSUC = datos[0]
        
        CANSUC = CANSUC + 1 #total de sucursales 

        if TOTPES > max_importe:
            max_importe = TOTPES
            MYPROD = producto_actual

        if TOTPES < min_importe:
            min_importe = TOTPES
            MNPRO = producto_actual
            
    
    print("Sucursal:", sucursal_actual,
        "Producto:", producto_actual,
        "TOTUNI:", TOTUNI,
        "TOTPES:", TOTPES)
    print("Sucursal:", sucursal_actual,
        "TOTSUC:", TOTSUC,
        "MYPROD:",MYPROD, 
        "MYIMPOR:", max_importe,
        "MNPRO:",MNPRO, 
        "MNIMPOR:", min_importe)
    print("El total de sucursales del supermercado son:", CANSUC," ", "y"," ","La compra total en pesos de todas las sucursales es:", "$", TOTALIMP)


archivo.close()
