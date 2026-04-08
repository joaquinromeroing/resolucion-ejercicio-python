import csv
import os

def algoritmo_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
         
            if lista[j][0] > lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def emitir_resultados(path_archivo):
    try:
        with open(path_archivo, 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            header = next(lector)
            datos = list(lector)
            
            if not datos:
                print("El archivo está vacío.")
                return

            sucursal_actual = datos[0][0]
            acum_unid = 0
            
            print(f"\n{'SUCURSAL':<10} | {'TOTAL UNIDADES'}")
            print("-" * 30)

            for fila in datos:
                suc = fila[0]
                cant = int(fila[4])
                
                if suc == sucursal_actual:
                    acum_unid += cant
                else:
                    print(f"{sucursal_actual:<10} | {acum_unid}")
                    sucursal_actual = suc
                    acum_unid = cant
            
          
            print(f"{sucursal_actual:<10} | {acum_unid}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{path_archivo}'")

def menu():
    print(f"--- SISTEMA DE COMPRAS ---")

    nombre_archivo = input("Ingresá el path del archivo CSV: ").strip()
    if not nombre_archivo:
        nombre_archivo = 'COMPRAS_supermercado_desordenado_solo_sucursal.csv'

    print(f"Archivo cargado: {nombre_archivo}")

   
    if not os.path.exists(nombre_archivo):
        print(f"ALERTA: El archivo '{nombre_archivo}' no está en la carpeta.")
        print("Asegurate de que el nombre sea exacto y no tenga doble .csv")
        return

    esta_ordenado = input("¿El archivo esta ordenado? (Y/N): ").upper()

    if esta_ordenado == 'N':
        print("Ordenando archivo con Burbuja... (esperá unos segundos)")
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            header = next(lector)
            filas = list(lector)
        
        filas_listas = algoritmo_burbuja(filas)
        

        path_temp = "temp_ordenado.csv"
        with open(path_temp, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(header)
            escritor.writerows(filas_listas)
        
        emitir_resultados(path_temp)
    else:
   
        emitir_resultados(nombre_archivo)

if __name__ == "__main__":
    menu()