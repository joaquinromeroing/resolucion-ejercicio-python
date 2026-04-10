import csv

def burbuja_ordenar(ruta_entrada, ruta_salida):
    with open(ruta_entrada, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        encabezados = next(reader)
        datos = list(reader)

    n = len(datos)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            tupla_j = (datos[j][0], datos[j][1], datos[j][2], datos[j][3])
            tupla_j_next = (datos[j+1][0], datos[j+1][1], datos[j+1][2], datos[j+1][3])
            
            if tupla_j > tupla_j_next:
                datos[j], datos[j+1] = datos[j+1], datos[j]

    with open(ruta_salida, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(encabezados)
        writer.writerows(datos)
    
    print(f"Archivo ordenado y guardado en: {ruta_salida}")
    return ruta_salida