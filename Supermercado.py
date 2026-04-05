# Punto C (Total)
TOTALIMP = 0
CANSUC = 0
i = 0
total_registros = len(datos)

while i < total_registros:
    # Sucursal actual
    suc_actual = datos[i]['PRSUC']
    CANSUC += 1
    
    # Punto B (Por sucursal)
    TOTSUC = 0
    MYPROD = ""
    MYIMPOR = -1000000.0
    MNPROD = ""
    MNIMPOR = 1000000.0
    acumulado_sucursal_pesos = 0 # Auxiliar para el punto C
    
    while i < total_registros and datos[i]['PRSUC'] == suc_actual:
        # Producto actual 
        prod_actual = datos[i]['PRCOD']
        
        # Punto A (Por producto)
        TOTUNI = 0
        TOTPES = 0
        
        while i < total_registros and datos[i]['PRSUC'] == suc_actual and datos[i]['PRCOD'] == prod_actual:
            
            subtotal = datos[i]['PRCANT'] * datos[i]['PRPRE']
            
            TOTUNI = TOTUNI + datos[i]['PRCANT']
            TOTPES = TOTPES + subtotal
            i += 1

        # FIN CORTE PRODUCTO (Punto A)    
        print(f" Producto: {prod_actual} | Unidades vendidas: {TOTUNI} | Ingresos generados: ${TOTPES:.2f}")
        
        # Sumamos el total de unidades vendidas del producto al total de unidades vendidas de la sucursal
        TOTSUC += TOTUNI
        acumulado_sucursal_pesos += TOTPES
        
        # Mayor y menor compra por producto en pesos
        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = prod_actual
            
        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD = prod_actual

    # FIN CORTE SUCURSAL (Punto B)
    print("\n" + "." * 60)
    print(f" SUCURSAL {suc_actual}:")
    print(f" - Total unidades compradas (TOTSUC): {TOTSUC}")
    print(f" - Mayor compra (MYPROD):   {MYPROD} con ${MYIMPOR:.2f}")
    print(f" - Menor compra (MNPRO):    {MNPROD} con ${MNIMPOR:.2f}")
    print("." * 60)
    
    # TOTAL GENERAL (Punto C)
    TOTALIMP = TOTALIMP + acumulado_sucursal_pesos
    
# FIN CORTE TOTAL (Punto C)
print("\n" + "."*60)
print("ESTADÍSTICA TOTAL GENERAL")
print("."*60)
print(f"Total de sucursales (CANSUC): {CANSUC}")
print(f"Compra total en pesos (TOTALIMP): ${TOTALIMP:.2f}")
print("."*60)