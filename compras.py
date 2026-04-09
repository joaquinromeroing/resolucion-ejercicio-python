import os
import csv 

def ordenar_datos(path_entrada):
    with open(path_entrada, 'r') as file:
        lines = file.readlines()
    
    Datos = []
    Encabezado = ""
    for l in lines:
        if "PRSUC" in l:
            Encabezado = l
        elif l.strip():
            Datos.append(l)

    n = len(Datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            col_Actual = Datos[j].strip().split(',')
            col_siguiente = Datos[j+1].strip().split(',')
            if col_Actual[0] > col_siguiente[0]:
                Datos[j], Datos[j+1] = Datos[j+1], Datos[j]
            elif col_Actual[0] == col_siguiente[0]:
                if col_Actual[1] > col_siguiente[1]:
                    Datos[j], Datos[j+1] = Datos[j+1], Datos[j]
                elif col_Actual[1] == col_siguiente[1]:
                    if col_Actual[2] > col_siguiente[2]:
                        Datos[j], Datos[j+1] = Datos[j+1], Datos[j]
    
    archivo_temporal = "temp_ordenado.csv"
    with open(archivo_temporal, 'w') as out:
        out.write(Encabezado)
        for linea in Datos:
            out.write(linea)
    return archivo_temporal

path_usuario = input("Indique el path del csv: ")
esta_ordenado = input("¿El archivo esta ordenado? (Y/N): ").upper()

if esta_ordenado == "N":
    print("Ordenando archivo...")
    archivo_final = ordenar_datos(path_usuario)
else:
    archivo_final = path_usuario

with open(archivo_final, 'r') as f:
    lines = f.readlines()[1:]  

n = len(lines)
i = 0
TOTALIMP = 0
CANSUC = 0

while i < n:
    datos = lines[i].strip().split(',')
    suc_actual = datos[0]
    CANSUC += 1
    
    TOTSUC_UNI = 0
    TOTSUC_PESOS = 0
    MYPROD = ""
    MYIMPOR = -1
    MNPROD = ""
    MNIPOR = float('inf')

    while i < n and lines[i].strip().split(',')[0] == suc_actual:
        datos = lines[i].strip().split(',') 
        prod_actual = datos[1]
        TOTUNI = 0
        TOTPES = 0

        while i < n and lines[i].strip().split(',')[0] == suc_actual and lines[i].strip().split(',')[1] == prod_actual:
            linea_split = lines[i].strip().split(',')
            cant = int(linea_split[4])
            precio = float(linea_split[5])
            TOTUNI += cant
            TOTPES += (cant * precio)
            i += 1
        
        print(f"Sucursal: {suc_actual} | Producto: {prod_actual} | Cantidad: {TOTUNI} | Total: ${TOTPES:.2f}")
        
        TOTSUC_UNI += TOTUNI
        TOTSUC_PESOS += TOTPES

        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = prod_actual
        if TOTPES < MNIPOR:
            MNIPOR = TOTPES
            MNPROD = prod_actual

    
    print("-" * 50)
    print(f"INFORME SUCURSAL {suc_actual}:")
    print(f"Total Unidades Vendidas: {TOTSUC_UNI}")
    print(f"Producto Mayor Compra: {MYPROD} (${MYIMPOR:.2f})")
    print(f"Producto Menor Compra: {MNPROD} (${MNIPOR:.2f})")
    print("-" * 50)
    TOTALIMP += TOTSUC_PESOS

print("=" * 50)
print("ESTADISTICA GENERAL DEL SUPERMERCADO")
print(f"Total de Sucursales procesadas: {CANSUC}")
print(f"Importe Total General: ${TOTALIMP:.2f}")
print("=" * 50)