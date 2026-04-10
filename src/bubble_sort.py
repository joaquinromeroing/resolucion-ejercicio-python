# paso1_ordenar.py

def ordenar_archivo(path_entrada, path_salida):
    print(f"Leyendo archivo: {path_entrada}...")
    
    # 1. Leer el archivo de forma manual
    try:
        with open(path_entrada, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {path_entrada}")
        return

    if not lineas:
        print("El archivo está vacío.")
        return

    encabezado = lineas[0]
    datos = lineas[1:] # El resto son las filas con datos

    # 2. Algoritmo de Burbuja (Solo por Sucursal)
    n = len(datos)
    print("Ordenando por sucursal...")
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Extraemos solo la primera columna (Sucursal) de las filas actuales
            sucursal_actual = datos[j].split(',')[0]
            sucursal_siguiente = datos[j + 1].split(',')[0]

            # Si la sucursal actual es "mayor" alfabéticamente, intercambiamos
            if sucursal_actual > sucursal_siguiente:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    # 3. Guardar el resultado
    with open(path_salida, 'w', encoding='utf-8') as f_salida:
        f_salida.write(encabezado)
        for linea in datos:
            # Nos aseguramos de mantener el formato de saltos de línea
            if not linea.endswith('\n'):
                linea += '\n'
            f_salida.write(linea)
            
    print(f"¡Hecho! Archivo ordenado generado en: {path_salida}")

# Ejecución
if __name__ == "__main__":
    # Asegúrate de que las carpetas existan o ajusta los nombres aquí
    archivo_in = './data/COMPRAS_supermercado_desordenado_solo_sucursal.csv'
    archivo_out = './data/COMPRAS_supermercado_ordenado.csv'
    
    ordenar_archivo(archivo_in, archivo_out)