import csv

# Abrimos el archivo
with open('COMPRAS_supermercado.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)  # Saltamos el encabezado si existe
    # Convertimos a lista para poder navegar por índices con while
    filas = list(lector)
    
i = 0
n = len(filas)

CANSUC = 0 #Cantidad sucursales
TOTALIMP = 0 #Total Importe de todas las sucursales

#Recorremos mientras haya filas restantes
while i < n:
    sucursal_act = filas[i][0]
    print(f"Recorriendo sucursal : {sucursal_act}")
    MYPROD, MYIMPOR = "",0
    MNPRO,MNIMPOR = "",float('inf')
    TOTSUC = 0
    while i<n and filas[i][0] == sucursal_act:
        #Segumos en la misma sucursal
        producto_act = filas[i][1]
        TOTPES = 0
        TOTUNI = 0
        while i<n and filas[i][0] == sucursal_act and filas[i][1] == producto_act:
            #Seguimos en el mismo producto
            TOTPES += int(filas[i][4]) * float(filas[i][5]) #Acumulamos el importe comprado
            TOTUNI += int(filas[i][4]) #Acumulamos la cantidad comprada
            i += 1
        #Cambio de producto
        #Chequeamos que el producto anterior era el mas caro o mas barato de la sucursal
        if TOTPES > MYIMPOR:
            MYPROD = producto_act
            MYIMPOR = TOTPES

        if TOTPES < MNIMPOR:
            MNPRO = producto_act
            MNIMPOR = TOTPES

        print(f'Sucursal:{sucursal_act}-Producto:{producto_act}-Importe Total: ${TOTPES}-Total Unidades: {TOTUNI}')

        TOTSUC += TOTUNI  #Acumulamos las unidades compradas del producto a la sucrusal
        TOTALIMP += TOTPES #Acumulamos el importe total del producto al acumulador global
    #Reporte fin de sucursal
    CANSUC += 1
    print(f"--- RESUMEN {sucursal_act} ---")
    print(f"Unidades Vendidas: {TOTSUC}")
    print(f"Mayor Producto: {MYPROD} (${MYIMPOR:.2f})")
    print(f"Menor Producto: {MNPRO} (${MNIMPOR:.2f})")
    print("----------------------------------------------")

print(f"\nTOTAL DE SUCURSALES: {CANSUC}")
print(f"TOTAL GENERAL DE TODAS LAS SUCURSALES: ${TOTALIMP:.2f}")
    

