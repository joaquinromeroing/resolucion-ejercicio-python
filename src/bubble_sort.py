def bubble_sort_sucursales(filas_datos):
    """
    Lógica pura de ordenamiento (Algoritmo de Burbuja).
    Recibe una lista de strings y devuelve una lista ordenada por la primera columna.
    """
    n = len(filas_datos)
    # Copiamos la lista para no alterar la original
    datos = list(filas_datos)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Extraemos solo la primera columna (Sucursal)
            # Manejamos posibles líneas vacías o mal formateadas
            try:
                sucursal_actual = datos[j].split(',')[0].strip()
                sucursal_siguiente = datos[j + 1].split(',')[0].strip()

                if sucursal_actual > sucursal_siguiente:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
            except IndexError:
                continue
    return datos

def ordenar_archivo(path_entrada, path_salida):
    print(f"Leyendo archivo: {path_entrada}...")
    
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
    cuerpo = lineas[1:]

    print("Ordenando datos por sucursal...")
    datos_ordenados = bubble_sort_sucursales(cuerpo)

    # Guardar el resultado
    with open(path_salida, 'w', encoding='utf-8') as f_salida:
        f_salida.write(encabezado)
        for linea in datos_ordenados:
            if not linea.endswith('\n'):
                linea += '\n'
            f_salida.write(linea)
            
    print(f"¡Hecho! Archivo generado en: {path_salida}")

if __name__ == "__main__":
    # Ajustamos rutas relativas
    archivo_in = './data/COMPRAS_supermercado_desordenado_solo_sucursal.csv'
    archivo_out = './data/COMPRAS_supermercado_ordenado.csv'
    ordenar_archivo(archivo_in, archivo_out)