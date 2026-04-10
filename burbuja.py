import csv

def ordenar_burbuja(nombre_archivo):
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector)
        registros = list(lector)

    n = len(registros)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            actual = registros[j]
            siguiente = registros[j + 1]

            if (actual[0], actual[1]) > (siguiente[0], siguiente[1]):
                aux = registros[j]
                registros[j] = registros[j + 1]
                registros[j + 1] = aux

    with open("COMPRAS_ordenado.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)
        escritor.writerows(registros)

    print("Archivo ordenado generado: COMPRAS_ordenado.csv")

ordenar_burbuja("COMPRAS_supermercado_desordenado_solo_sucursal.csv")