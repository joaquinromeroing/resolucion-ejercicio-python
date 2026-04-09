import csv

# 1. FUNCIÓN DE BURBUJA (Desarrollada, sin usar .sort())
def funcion_burbuja(datos):
    n = len(datos)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Criterio: Sucursal (0) y Producto (1)
            if (datos[j][0], datos[j][1]) > (datos[j+1][0], datos[j+1][1]):
                datos[j], datos[j+1] = datos[j+1], datos[j]
                swapped = True
        if not swapped:
            break
    return datos

# 2. TU LÓGICA ORIGINAL DE WHILES (Encapsulada para que el menú la llame)
def ejecutar_analisis_original(path_archivo):
    print(f"\n--- Iniciando ejecución desde: {path_archivo} ---")
    archivo = open(path_archivo, 'r', encoding='utf-8')
    encabezado = archivo.readline()
    
    CANSUC = 0
    TOTALIMP = 0.0
    linea = archivo.readline()

    while linea != "":
        datos = linea.strip().split(',')
        sucursal_actual = datos[0]
        CANSUC += 1
        TOTSUC = 0
        MYIMPOR = 0.0
        MYPROD = ""
        MNIMPOR = 0.0
        MNPRO = ""
        primer_producto = True 
        
        print("\nSUCURSAL:", sucursal_actual)
        
        while linea != "" and datos[0] == sucursal_actual:
            producto_actual = datos[1]
            TOTUNI = 0
            TOTPES = 0.0
            
            while linea != "" and datos[0] == sucursal_actual and datos[1] == producto_actual:
                TOTUNI += int(datos[4])
                TOTPES += float(datos[4]) * float(datos[5])
                linea = archivo.readline()
                if linea != "": datos = linea.strip().split(',')
            
            print(f"Prod: {producto_actual} Unidades: {TOTUNI} Pesos: ${round(TOTPES, 2)}")
            TOTSUC += TOTUNI
            TOTALIMP += TOTPES

            if primer_producto:
                MYIMPOR = MNIMPOR = TOTPES
                MYPROD = MNPRO = producto_actual
                primer_producto = False 
            else:
                if TOTPES > MYIMPOR:
                    MYIMPOR = TOTPES
                    MYPROD = producto_actual
                if TOTPES < MNIMPOR:
                    MNIMPOR = TOTPES
                    MNPRO = producto_actual

        print(f"RESUMEN SUCURSAL {sucursal_actual}")
        print(f"Total unidades (TOTSUC): {TOTSUC}")
        print(f"Mayor compra: Prod. {MYPROD} con ${round(MYIMPOR, 2)}")
        print(f"Menor compra: Prod. {MNPRO} con ${round(MNIMPOR, 2)}")
    
    archivo.close()

# 3. FUNCIONALIDAD DE MENÚ (Requisito del paso 2)
def menu():
    path = input("Indique el path del csv: ")
    ordenado = input("El archivo esta ordenado (Y/N): ").upper()

    if ordenado == 'N':
        print("Ordenando archivo con Burbuja... (paciente, son 10.000 filas)")
        with open(path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            datos_lista = list(reader)
        
        datos_ordenados = funcion_burbuja(datos_lista)
        
        # Archivo temporal para la ejecución
        temp_path = "temp_archivo_ordenado.csv"
        with open(temp_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(datos_ordenados)
        
        ejecutar_analisis_original(temp_path)
    else:
        ejecutar_analisis_original(path)

if __name__ == "__main__":
    menu()