import csv

def burbuja_paso1():
    archivo_entrada = 'COMPRAS_supermercado_desordenado_solo_sucursal.csv'
    archivo_salida = 'COMPRAS_nuevo_ordenado_paso1.csv'
    
    print(f"Leyendo {archivo_entrada}...")
    with open(archivo_entrada, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        datos = list(reader)

    n = len(datos)
    print(f"Ordenando {n} registros por Burbuja. Esto puede demorar un poquito...")
    
    # Algoritmo de Burbuja Manual
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Comparamos por Sucursal (col 0) y Producto (col 1)
            if (datos[j][0], datos[j][1]) > (datos[j+1][0], datos[j+1][1]):
                datos[j], datos[j+1] = datos[j+1], datos[j]
                swapped = True
        if not swapped:
            break
    
    print(f"Grabando resultado en {archivo_salida}...")
    with open(archivo_salida, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(datos)
    print("¡Paso 1 completado con éxito!")

if __name__ == "__main__":
    burbuja_paso1()