import csv
import os

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
    
def ordenar_burbuja(filas):
    """Implementación de burbuja para ordenar por Sucursal"""
    n = len(filas)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Ordenamos por sucursal, y si son iguales, por producto
            if filas[j][0] > filas[j + 1][0]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
            elif filas[j][0] == filas[j + 1][0] and filas[j][1] > filas[j + 1][1]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
    return filas

def procesar_datos(filas):
    """La lógica original de procesamiento de sucursales y productos"""
    i = 0
    n = len(filas)
    CANSUC = 0
    TOTALIMP = 0

    while i < n:
        sucursal_act = filas[i][0]
        print(f"\nRecorriendo sucursal : {sucursal_act}")
        MYPROD, MYIMPOR = "", 0
        MNPRO, MNIMPOR = "", float('inf')
        TOTSUC = 0
        
        while i < n and filas[i][0] == sucursal_act:
            producto_act = filas[i][1]
            TOTPES = 0
            TOTUNI = 0
            while i < n and filas[i][0] == sucursal_act and filas[i][1] == producto_act:
                TOTPES += int(filas[i][4]) * float(filas[i][5])
                TOTUNI += int(filas[i][4])
                i += 1
            
            if TOTPES > MYIMPOR:
                MYPROD = producto_act
                MYIMPOR = TOTPES
            if TOTPES < MNIMPOR:
                MNPRO = producto_act
                MNIMPOR = TOTPES

            print(f'Sucursal:{sucursal_act} - Producto:{producto_act} - Importe Total: ${TOTPES:.2f} - Total Unidades: {TOTUNI}')
            TOTSUC += TOTUNI
            TOTALIMP += TOTPES

        CANSUC += 1
        print(f"--- RESUMEN {sucursal_act} ---")
        print(f"Unidades Vendidas: {TOTSUC}")
        print(f"Mayor Producto: {MYPROD} (${MYIMPOR:.2f})")
        print(f"Menor Producto: {MNPRO} (${MNIMPOR:.2f})")
        print("----------------------------------------------")

    print(f"\nTOTAL DE SUCURSALES: {CANSUC}")
    print(f"TOTAL GENERAL DE TODAS LAS SUCURSALES: ${TOTALIMP:.2f}")


# --- INICIO DEL PROGRAMA (MENÚ) ---
path_archivo = input("Indique el path del csv: ")
esta_ordenado = input("¿El archivo esta ordenado? (Y/N): ").upper()

try:
    with open(path_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        cabecera = next(lector)
        filas = list(lector)

    if esta_ordenado == 'N':
        print("Ordenando archivo... por favor espere.")
        filas_ordenadas = ordenar_burbuja(filas)
        
        # Grabamos el archivo temporal
        path_temporal = "temp_ordenado.csv"
        with open(path_temporal, mode='w', newline='', encoding='utf-8') as archivo_salida:
            escritor = csv.writer(archivo_salida)
            escritor.writerow(cabecera)
            escritor.writerows(filas_ordenadas)
        
        print(f"Archivo ordenado guardado en: {path_temporal}")
        # Trabajamos con las filas ya ordenadas en memoria
        procesar_datos(filas_ordenadas)

        os.remove(path_temporal) 
        print(f"\nArchivo temporal {path_temporal} eliminado.")
    else:
        # Iniciar ejecución directamente
        procesar_datos(filas)

except FileNotFoundError:
    print("Error: No se encontró el archivo. Verifique el path.")

