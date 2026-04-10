# resolucion_unificada.py

def procesar_compras(path_archivo):
    print(f"{'='*60}")
    print(f"PROCESANDO INFORME DE COMPRAS: {path_archivo}")
    print(f"{'='*60}\n")

    try:
        with open(path_archivo, mode='r', encoding='utf-8') as file:
            next(file)  # Saltar encabezado
            line = file.readline()
            
            if not line:
                print("El archivo está vacío.")
                return
            
            data = line.strip().split(",")
            
            # --- Inicialización General (Punto 3) ---
            cansuc = 0
            totalimp_general = 0

            # Bucle Principal: Recorre todo el archivo
            while data:
                # --- Inicialización por SUCURSAL (Punto 2) ---
                prsuc_actual = data[0]
                totsuc_unidades = 0
                total_suc_pesos = 0
                
                myprod, myimpor = None, -1
                mnprod, mnimpor = None, float('inf')
                
                cansuc += 1
                
                print(f"DETALLE SUCURSAL: {prsuc_actual}")
                print(f"{'ID Prod':<10} | {'Unidades':<10} | {'Subtotal ($)':<15}")
                print("-" * 40)

                # Corte de Control: Nivel Sucursal
                while data and data[0] == prsuc_actual:
                    # --- Inicialización por PRODUCTO (Punto 1) ---
                    prcod_actual = data[1]
                    totuni_producto = 0
                    totpes_producto = 0

                    # Corte de Control: Nivel Producto
                    while data and data[0] == prsuc_actual and data[1] == prcod_actual:
                        # Extraer datos de la fila
                        cant = int(data[4])
                        precio = float(data[5])
                        
                        # Acumular datos del Producto
                        totuni_producto += cant
                        totpes_producto += (cant * precio)
                        
                        # Leer siguiente línea
                        line = file.readline()
                        if not line:
                            data = None
                        else:
                            data = line.strip().split(",")

                    # Al terminar un Producto:
                    # 1. Informar (Punto 1)
                    print(f"{prcod_actual:<10} | {totuni_producto:<10} | {round(totpes_producto, 2):<15}")
                    
                    # 2. Acumular para la Sucursal (Punto 2)
                    totsuc_unidades += totuni_producto
                    total_suc_pesos += totpes_producto
                    
                    # 3. Evaluar Mayor y Menor compra (Punto 2)
                    if totpes_producto > myimpor:
                        myimpor = totpes_producto
                        myprod = prcod_actual
                    
                    if totpes_producto < mnimpor:
                        mnimpor = totpes_producto
                        mnprod = prcod_actual

                # Al terminar una Sucursal:
                # 1. Informar totales de sucursal (Punto 2)
                print("-" * 40)
                print(f"TOTAL {prsuc_actual}: {totsuc_unidades} unidades.")
                print(f"MAYOR COMPRA: {myprod} (${round(myimpor, 2)})")
                print(f"MENOR COMPRA: {mnprod} (${round(mnimpor, 2)})")
                print(f"SUBTOTAL SUCURSAL: ${round(total_suc_pesos, 2)}\n")
                
                # 2. Acumular para el Total General (Punto 3)
                totalimp_general += total_suc_pesos

            # --- Informe Final (Punto 3) ---
            print(f"{'='*60}")
            print(f"RESUMEN GENERAL")
            print(f"Cantidad de sucursales procesadas: {cansuc}")
            print(f"IMPORTE TOTAL DE COMPRAS: ${round(totalimp_general, 2)}")
            print(f"{'='*60}")

    except FileNotFoundError:
        print("Error: No se encontró el archivo COMPRAS_supermercado.csv")

if __name__ == "__main__":
    # Asegúrate de que el path sea el correcto según tu estructura de carpetas
    path = "./data/COMPRAS_supermercado.csv"
    procesar_compras(path)