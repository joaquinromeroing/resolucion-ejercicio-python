import csv
import os

def bubbleSearch(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][0] > lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenar_csv(path_entrada, path_salida):
    with open(path_entrada, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        datos = list(reader)

    datos_ordenados = bubbleSearch(datos)

    with open(path_salida, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(datos_ordenados)

    return path_salida


def corte_control(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)

        sucursal_actual = None
        total = 0

        print("\n--- Totales por sucursal ---")

        for fila in reader:
            sucursal = fila[0]
            cantidad = int(fila[4])

            if sucursal_actual != sucursal:
                if sucursal_actual is not None:
                    print(f"Sucursal {sucursal_actual}: {total}")

                sucursal_actual = sucursal
                total = 0

            total += cantidad

        if sucursal_actual is not None:
            print(f"Sucursal {sucursal_actual}: {total}")


def main():
    path = input("Indique el path del csv: ")
    ordenado = input("¿El archivo está ordenado? (Y/N): ").upper()

    if not os.path.exists(path):
        print("El archivo no existe")
        return

    if ordenado == "N":
        path = ordenar_csv(path, "archivo_temp_ordenado.csv")
        print("Archivo ordenado generado")

    corte_control(path)


if __name__ == "__main__":
    main()