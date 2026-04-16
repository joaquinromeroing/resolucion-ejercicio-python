import csv
import sys


def bubble_sort(filas, columna):
    n = len(filas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if filas[j][columna] > filas[j + 1][columna]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
    return filas


def procesar_csv(archivo_entrada):
    with open(archivo_entrada, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        encabezados = lector.fieldnames
        filas = list(lector)

    filas_ordenadas = bubble_sort(filas, encabezados[0])

    nombre_salida = "ordenado.csv"
    with open(nombre_salida, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(filas_ordenadas)

    print(f"Archivo ordenado guardado como {nombre_salida}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ordenar_burbuja.py <archivo.csv>")
        sys.exit(1)

    procesar_csv(sys.argv[1])
