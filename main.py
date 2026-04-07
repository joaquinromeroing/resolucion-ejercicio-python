import csv
import os

# --- FUNCIÓN DE ORDENAMIENTO (MÉTODO BURBUJA) ---
def ordenar_por_sucursal(path_entrada, path_salida):
    datos = []

    try:
        with open(path_entrada, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                datos.append(fila)

        n = len(datos)
        print(f"Ordenando {n} registros...")
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if datos[j]['PRSUC'] > datos[j+1]['PRSUC']:
                    datos[j], datos[j+1] = datos[j+1], datos[j]

        columnas = datos[0].keys()
        with open(path_salida, mode='w', encoding='utf-8', newline='') as archivo_salida:
            escritor = csv.DictWriter(archivo_salida, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(datos)

    except Exception as e:
        print(f"Error durante el ordenamiento: {e}")

# --- FUNCIÓN DE PROCESAMIENTO (ESTADÍSTICAS) ---
def procesar_estadisticas(path_archivo):
    TOTALIMP = 0
    datos_supermercado = {}

    try:
        with open(path_archivo, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            
            for fila in lector_csv:
                sucursal = fila['PRSUC']
                producto = fila['PRCOD']
                cantidad = int(fila['PRCANT'])
                precio = float(fila['PRPRE'])
                
                importe_compra = cantidad * precio
                
                if sucursal not in datos_supermercado:
                    datos_supermercado[sucursal] = {}
                    
                if producto not in datos_supermercado[sucursal]:
                    datos_supermercado[sucursal][producto] = {'TOTUNI': 0, 'TOTPES': 0.0}
                    
                datos_supermercado[sucursal][producto]['TOTUNI'] += cantidad
                datos_supermercado[sucursal][producto]['TOTPES'] += importe_compra
                TOTALIMP += importe_compra

        print("\n" + "="*50)
        print(" ESTADÍSTICAS DEL SUPERMERCADO ".center(50, "="))
        print("="*50)

        for sucursal, productos in datos_supermercado.items():
            print(f"\n--- SUCURSAL: {sucursal} ---")
            TOTSUC = 0
            MYPROD = ""; MYIMPOR = -1.0
            MNPRO = ""; MNIMPOR = float('inf')
            
            print("A) Detalle por Producto:")
            for producto, valores in productos.items():
                TOTUNI = valores['TOTUNI']
                TOTPES = valores['TOTPES']
                print(f"   Producto: {producto} | Unidades: {TOTUNI} | Importe: ${TOTPES:.2f}")
                TOTSUC += TOTUNI
                if TOTPES > MYIMPOR:
                    MYIMPOR = TOTPES; MYPROD = producto
                if TOTPES < MNIMPOR:
                    MNIMPOR = TOTPES; MNPRO = producto

            print(f"\nB) Resumen de {sucursal}:")
            print(f"   - Total unidades (TOTSUC): {TOTSUC}")
            print(f"   - Mayor compra: {MYPROD} (${MYIMPOR:.2f})")
            print(f"   - Menor compra: {MNPRO} (${MNIMPOR:.2f})")
            print("-" * 50)

        print(f"\nC) TOTALES GENERALES")
        print(f"   - Total sucursales: {len(datos_supermercado)}")
        print(f"   - Compra total acumulada: ${TOTALIMP:.2f}")
        print("="*50 + "\n")
    except Exception as e:
        print(f"Error al procesar estadísticas: {e}")

# --- MENÚ PRINCIPAL ---
def menu():
    path_usuario = input("Indique el path del csv: ")
    
    if not os.path.exists(path_usuario):
        print("Error: El archivo especificado no existe.")
        return

    esta_ordenado = input("¿El archivo está ordenado? (Y/N): ").upper()

    if esta_ordenado == 'N':
        path_temp = "temp_ordenado_ejecucion.csv"
        
        ordenar_por_sucursal(path_usuario, path_temp)
        
        procesar_estadisticas(path_temp)
        
        if os.path.exists(path_temp):
            os.remove(path_temp)
            
    elif esta_ordenado == 'Y':
        procesar_estadisticas(path_usuario)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()