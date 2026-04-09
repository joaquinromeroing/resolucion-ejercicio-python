import csv

def bubble_sort(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (datos[j][0], datos[j][1]) > (datos[j+1][0], datos[j+1][1]):
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos

entrada = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
salida = "COMPRAS_supermercado_ordenado_generado.csv"

with open(entrada, "r", encoding="utf-8") as f:
    lector = list(csv.reader(f))

encabezado = lector[0]
datos = lector[1:]

datos_ordenados = bubble_sort(datos)

with open(salida, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(encabezado)
    writer.writerows(datos_ordenados)

print("Archivo ordenado generado correctamente ✔️")