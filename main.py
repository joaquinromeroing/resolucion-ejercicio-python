import csv
import os

# 1. Manejo de Archivos

def construir_ruta(directorio, nombre_archivo):
    """Concatena un directorio y un nombre de archivo de forma segura."""
    return os.path.join(directorio, nombre_archivo)

def leer_csv(ruta_archivo):
    """Lee el CSV y devuelve los encabezados y los datos puros."""
    with open(ruta_archivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        encabezados = next(reader)
        datos = list(reader)
    return encabezados, datos

def escribir_csv(ruta_salida, encabezados, datos):
    """Escribe los datos en un nuevo archivo CSV."""
    with open(ruta_salida, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(encabezados)
        writer.writerows(datos)

# 2. Ordenar y Procesar

def ordenar_datos_burbuja(datos):
    """Recibe una lista de datos y la devuelve ordenada. No toca archivos."""
    datos_ordenados = datos.copy()
    n = len(datos_ordenados)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            tupla_j = tuple(datos_ordenados[j][:4])
            tupla_j_next = tuple(datos_ordenados[j+1][:4])
            
            if tupla_j > tupla_j_next:
                datos_ordenados[j], datos_ordenados[j+1] = datos_ordenados[j+1], datos_ordenados[j]
                
    return datos_ordenados

def procesar_corte_de_control(datos):
    """
    Realiza los cálculos del corte de control y devuelve un diccionario 
    con los resultados estructurados. No usa print().
    """
    resultados = {
        "sucursales": [],
        "cantidad_sucursales": 0,
        "total_general": 0.0
    }
    
    i = 0
    n = len(datos)

    while i < n:
        suc_actual = datos[i][0]
        resultados["cantidad_sucursales"] += 1
        
        datos_sucursal = {
            "nombre": suc_actual,
            "productos": [],
            "total_unidades_sucursal": 0,
            "mayor_producto": "",
            "mayor_importe": -1.0,
            "menor_producto": "",
            "menor_importe": float('inf')
        }
        
        totpes_sucursal = 0.0

        while i < n and datos[i][0] == suc_actual:
            prod_actual = datos[i][1]
            tot_uni = 0
            tot_pes = 0.0

            while i < n and datos[i][0] == suc_actual and datos[i][1] == prod_actual:
                cant = int(datos[i][4])
                pre = float(datos[i][5])
                imp = cant * pre

                tot_uni += cant
                tot_pes += imp
                i += 1
            
            datos_sucursal["productos"].append({
                "nombre": prod_actual,
                "unidades": tot_uni,
                "total_pesos": tot_pes
            })

            datos_sucursal["total_unidades_sucursal"] += tot_uni
            totpes_sucursal += tot_pes

            # Evaluamos mayores y menores
            if tot_pes > datos_sucursal["mayor_importe"]:
                datos_sucursal["mayor_importe"] = tot_pes
                datos_sucursal["mayor_producto"] = prod_actual
            
            if tot_pes < datos_sucursal["menor_importe"]:
                datos_sucursal["menor_importe"] = tot_pes
                datos_sucursal["menor_producto"] = prod_actual

        resultados["total_general"] += totpes_sucursal
        resultados["sucursales"].append(datos_sucursal)
        
    return resultados

# 3. Salida

def imprimir_reporte_corte(resultados):
    """Recibe el diccionario de resultados y lo imprime por pantalla."""
    for suc in resultados["sucursales"]:
        print(f"\nSUCURSAL: {suc['nombre']}")
        print("a) TOTALES POR PRODUCTO")
        
        for prod in suc["productos"]:
            print(f"  Producto: {prod['nombre']} - Unidades: {prod['unidades']} - Total: ${prod['total_pesos']:.2f}")
            
        print("b) TOTAL POR SUCURSAL")
        print(f"  Total Unidades: {suc['total_unidades_sucursal']}")
        if suc["mayor_producto"]:
            print(f"  Mayor compra: {suc['mayor_producto']} (${suc['mayor_importe']:.2f})")
            print(f"  Menor compra: {suc['menor_producto']} (${suc['menor_importe']:.2f})")

    print("\nc) TOTALES GENERALES")
    print(f"Cantidad de sucursales: {resultados['cantidad_sucursales']}")
    print(f"Compra total general: ${resultados['total_general']:.2f}")

# 4. Menu principal

def menu():
    directorio = input("Indique la ruta de la carpeta (ej. ./): ")
    nombre_archivo = input("Indique el nombre del archivo CSV: ")
    
    path = construir_ruta(directorio, nombre_archivo)
    
    if not os.path.exists(path):
        print("Error: El archivo no existe en la ruta especificada.")
        return

    esta_ordenado = input("El archivo esta ordenado: Y/N: ").upper()

    if esta_ordenado == 'N':
        ruta_salida = construir_ruta(directorio, "COMPRAS_supermercado_ordenado.csv")
        print("Ordenando el archivo...")
        
        # 1. Leer
        encabezados, datos = leer_csv(path)
        # 2. Ordenar
        datos_ordenados = ordenar_datos_burbuja(datos)
        # 3. Guardar
        escribir_csv(ruta_salida, encabezados, datos_ordenados)
        print(f"Archivo ordenado y guardado en: {ruta_salida}")
        
        # 4. Procesar y Mostrar
        resultados = procesar_corte_de_control(datos_ordenados)
        imprimir_reporte_corte(resultados)
        
    else:
        # 1. Leer
        _, datos = leer_csv(path)
        # 2. Procesar y Mostrar
        resultados = procesar_corte_de_control(datos)
        imprimir_reporte_corte(resultados)

if __name__ == "__main__":
    menu()