import pandas as pd

df = pd.read_csv('COMPRAS_supermercado_desordenado_solo_sucursal.csv')
datos = df.to_dict('records')

# 1. FUNCIÓN DE ORDENAMIENTO (Burbuja)
def ordenar_por_burbuja(lista_desordenada):
    n = len(lista_desordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparamos por sucursal (PRSUC)
            if lista_desordenada[j]['PRSUC'] > lista_desordenada[j+1]['PRSUC']:
                # Intercambio
                lista_desordenada[j], lista_desordenada[j+1] = lista_desordenada[j+1], lista_desordenada[j]
    return lista_desordenada

# --- PROCESAMIENTO ---
datos_ordenados = ordenar_por_burbuja(datos)

# --- CORTE DE CONTROL (Punto C - Total) ---
TOTALIMP = 0
CANSUC = 0
i = 0
total_registros = len(datos_ordenados)

while i < total_registros:
    # Sucursal actual
    suc_actual = datos_ordenados[i]['PRSUC']
    CANSUC += 1
    
    # Punto B (Por sucursal)
    TOTSUC = 0
    MYPROD = ""; MYIMPOR = -1000000.0
    MNPROD = ""; MNIMPOR = 1000000.0
    acumulado_sucursal_pesos = 0 
    
    while i < total_registros and datos_ordenados[i]['PRSUC'] == suc_actual:
        # Producto actual 
        prod_actual = datos_ordenados[i]['PRCOD']
        
        # Punto A (Por producto)
        TOTUNI = 0
        TOTPES = 0
        
        while i < total_registros and datos_ordenados[i]['PRSUC'] == suc_actual and datos_ordenados[i]['PRCOD'] == prod_actual:
            
            subtotal = datos_ordenados[i]['PRCANT'] * datos_ordenados[i]['PRPRE']
            
            TOTUNI = TOTUNI + datos_ordenados[i]['PRCANT']
            TOTPES = TOTPES + subtotal
            i += 1

        # FIN CORTE PRODUCTO (Punto A)    
        print(f" Producto: {prod_actual} | Unidades vendidas: {TOTUNI} | Ingresos: ${TOTPES:.2f}")
        
        TOTSUC += TOTUNI
        acumulado_sucursal_pesos += TOTPES
        
        # Lógica de Mayor y Menor
        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = prod_actual
            
        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD = prod_actual

    # FIN CORTE SUCURSAL (Punto B)
    print("\n" + "." * 60)
    print(f" SUCURSAL {suc_actual}:")
    print(f" - Total unidades (TOTSUC): {TOTSUC}")
    print(f" - Mayor compra (MYPROD):   {MYPROD} con ${MYIMPOR:.2f}")
    print(f" - Menor compra (MNPROD):   {MNPROD} con ${MNIMPOR:.2f}")
    print("." * 60)
    
    TOTALIMP += acumulado_sucursal_pesos
    
# FIN CORTE TOTAL (Punto C)
print(f"\nTotal de sucursales: {CANSUC}")
print(f"Compra total general: ${TOTALIMP:.2f}")