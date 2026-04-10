# sales_report_processor.py
import os

def ordenar_por_burbuja(path_entrada):
    """
    Algoritmo de burbuja desarrollado manualmente para ordenar por sucursal.
    Genera un archivo temporal para no sobreescribir el original.
    """
    path_temporal = "./data/COMPRAS_supermercado_desordenado_solo_sucursal.csv"
    print(f"Ordenando archivo mediante algoritmo de burbuja...")

    with open(path_entrada, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    if len(lineas) <= 1:
        return path_entrada

    encabezado = lineas[0]
    datos = lineas[1:]
    n = len(datos)

    # Algoritmo de Burbuja (Paso 2 - Sin usar .sort())
    for i in range(n):
        for j in range(0, n - i - 1):
            sucursal_actual = datos[j].split(',')[0]
            sucursal_siguiente = datos[j + 1].split(',')[0]

            if sucursal_actual > sucursal_siguiente:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    with open(path_temporal, 'w', encoding='utf-8') as f_out:
        f_out.write(encabezado)
        f_out.writelines(datos)
    
    return path_temporal

def procesar_corte_de_control(path_archivo):
    """
    Ejecuta la lógica de Corte de Control (Paso 1 unificado).
    """
    print(f"\n{'='*60}")
    print(f"INICIANDO PROCESAMIENTO: {path_archivo}")
    print(f"{'='*60}\n")

    try:
        with open(path_archivo, mode='r', encoding='utf-8') as file:
            next(file)  # Saltar encabezado
            line = file.readline()
            if not line: return
            
            data = line.strip().split(",")
            cansuc = 0
            totalimp_general = 0

            while data:
                prsuc_actual = data[0]
                totsuc_unidades = 0
                total_suc_pesos = 0
                myprod, myimpor = None, -1
                mnprod, mnimpor = None, float('inf')
                cansuc += 1
                
                print(f"SUCURSAL: {prsuc_actual}")
                print(f"{'-'*40}")

                while data and data[0] == prsuc_actual:
                    prcod_actual = data[1]
                    totuni_producto = 0
                    totpes_producto = 0

                    while data and data[0] == prsuc_actual and data[1] == prcod_actual:
                        cant = int(data[4])
                        precio = float(data[5])
                        totuni_producto += cant
                        totpes_producto += (cant * precio)
                        
                        line = file.readline()
                        data = line.strip().split(",") if line else None

                    # Punto 1: Informe por producto
                    print(f"Prod: {prcod_actual} | Unidades: {totuni_producto} | Total: ${round(totpes_producto, 2)}")
                    
                    total_suc_pesos += totpes_producto
                    totsuc_unidades += totuni_producto
                    
                    if totpes_producto > myimpor:
                        myimpor, myprod = totpes_producto, prcod_actual
                    if totpes_producto < mnimpor:
                        mnimpor, mnprod = totpes_producto, prcod_actual

                # Punto 2: Informe por sucursal
                print(f"\n>>> TOTAL {prsuc_actual}: {totsuc_unidades} unidades.")
                print(f">>> MAYOR COMPRA: {myprod} (${round(myimpor, 2)})")
                print(f">>> MENOR COMPRA: {mnprod} (${round(mnimpor, 2)})\n")
                totalimp_general += total_suc_pesos

            # Punto 3: Informe total
            print(f"{'='*60}")
            print(f"CANTIDAD TOTAL SUCURSALES: {cansuc}")
            print(f"IMPORTE TOTAL GENERAL: ${round(totalimp_general, 2)}")
            print(f"{'='*60}")

    except FileNotFoundError:
        print("Error: El archivo no existe.")

def menu():
    """
    Funcionalidad de menú (Paso 2).
    """
    print("--- SISTEMA DE GESTIÓN DE COMPRAS ---")
    path_csv = input("Indique el path del csv: ")
    
    if not os.path.exists(path_csv):
        print("El path indicado no es válido.")
        return

    esta_ordenado = input("El archivo esta ordenado (Y/N): ").upper()

    if esta_ordenado == "N":
        # Si no está ordenado, aplicamos burbuja y usamos el temporal
        path_a_procesar = ordenar_por_burbuja(path_csv)
    else:
        # Si está ordenado, procesamos el original directamente
        path_a_procesar = path_csv

    procesar_corte_de_control(path_a_procesar)

    # Limpieza: borrar archivo temporal si se creó
    if esta_ordenado == "N" and os.path.exists("temp_ordenado.csv"):
        os.remove("temp_ordenado.csv")

if __name__ == "__main__":
    menu()