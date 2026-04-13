import csv

def bubble_sort(datos):
    n = len(datos)

    for i in range(n):
        for j in range(0, n-i-1):

            if datos[j] > datos[j+1]:
                temp = datos[j]
                datos[j] = datos[j+1]
                datos[j+1] = temp

    return datos


def leer_csv(path):

    with open(path, newline='') as f:
        reader = csv.reader(f)
        datos = list(reader)

    return datos


def guardar_csv(path, datos):

    with open(path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(datos)


def menu():

    path = input("Indique el path del csv: ")

    ordenado = input("El archivo esta ordenado? (Y/N): ")

    datos = leer_csv(path)

    if ordenado.upper() == "N":

        print("Ordenando archivo con algoritmo de burbuja...")

        datos = bubble_sort(datos)

        archivo_temp = "archivo_temporal_ordenado.csv"

        guardar_csv(archivo_temp, datos)

        print("Archivo ordenado guardado en:", archivo_temp)

    else:

        print("Archivo ya ordenado. Iniciando ejecución...")


menu()