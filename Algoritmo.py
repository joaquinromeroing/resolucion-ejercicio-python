#!/bin/env python3
import csv
import os

def ordenar_burbuja(filas):
    n = len(filas)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            clave_actual = (filas[j][0], filas[j][1])
            clave_siguiente = (filas[j + 1][0], filas[j + 1][1])
            if clave_actual > clave_siguiente:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
    return filas

print("=== Sistema de procesamiento de compras ===")
print()

path_csv = input("1. Indique el path del CSV: ").strip()

if not os.path.exists(path_csv):
    print(f"Error: no se encontro el archivo '{path_csv}'")
    exit()

esta_ordenado = input("2. El archivo esta ordenado (Y/N): ").strip().upper()

if esta_ordenado == "N":
    print("Ordenando el archivo, por favor espere...")

    with open(path_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        encabezado = next(reader)
        filas = list(reader)

    filas = ordenar_burbuja(filas)

    path_csv = "temporal_ordenado.csv"
    with open(path_csv, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(encabezado)
        writer.writerows(filas)

    print(f"Archivo ordenado guardado como: {path_csv}")
    print()

elif esta_ordenado == "Y":
    print("El archivo ya esta ordenado, iniciando ejecucion...")
    print()

else:
    print("Opcion invalida. Debe ingresar Y o N.")
    exit()

with open(path_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    data = list(reader)
    i = 0

    total_units_product = 0
    total_price_product = 0
    total_units_branch = 0
    total_price_branch = 0
    max_price_product = 0
    min_price_product = 999999999
    total_price = 0
    total_branch = 0

    while i < len(data):
        row = data[i]

        current_branch = row[0]

        print("-"*30 + f"Sucursal: {current_branch}" + "-"*30 + "\n")

        while i < len(data) and current_branch == row[0]:

            current_product = row[1]

            while i < len(data) and current_product == row[1]:
                row = data[i]

                units_product = int(row[4])
                price_product = float(row[5])
                total_units_product += units_product
                total_price_product += price_product * units_product

                i += 1

            print(f"Cod. Prod.: {current_product}, Total Uni.: {total_units_product}, Total precio: {total_price_product:.2f}")

            if total_price_product > max_price_product:
                max_product = current_product
                max_price_product = total_price_product

            if total_price_product < min_price_product:
                min_product = current_product
                min_price_product = total_price_product

            total_units_branch += total_units_product
            total_price_branch += total_price_product
            total_units_product = 0
            total_price_product = 0

        print(f"\nTotal Uni. de la sucursal: {total_units_branch}")
        print(f"Producto mas comprado: {max_product}, Importe: {max_price_product:.2f}")
        print(f"Producto menos comprado: {min_product}, Importe: {min_price_product:.2f}\n")

        total_price += total_price_branch
        total_units_branch = 0
        total_price_branch = 0
        max_price_product = 0
        min_price_product = 999999999
        total_branch += 1

    print("-"*45)
    print(f"\nSucursales totales: {total_branch}, Compra total: {total_price:.2f}")
