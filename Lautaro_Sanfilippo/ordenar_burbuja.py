import csv

archivo_entrada = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
archivo_salida = "COMPRAS_supermercado.csv"


def leer_csv(nombre):
    with open(nombre, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        encabezado = next(lector)
        filas = [fila for fila in lector]
    return encabezado, filas


def ordenar_burbuja(filas, indice):
    n = len(filas)

    for pasada in range(n - 1):
        hubo_cambio = False

        for i in range(n - 1 - pasada):
            if filas[i][indice] > filas[i + 1][indice]:
                filas[i], filas[i + 1] = filas[i + 1], filas[i]
                hubo_cambio = True

        if not hubo_cambio:
            break

    return filas


def grabar_csv(nombre, encabezado, filas):
    with open(nombre, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(encabezado)
        escritor.writerows(filas)


def main():
    encabezado, filas = leer_csv(archivo_entrada)
    indice_sucursal = encabezado.index("PRSUC")
    filas_ordenadas = ordenar_burbuja(filas, indice_sucursal)
    grabar_csv(archivo_salida, encabezado, filas_ordenadas)

    print()
    print("=" * 70)
    print("ARCHIVO ORDENADO GENERADO CORRECTAMENTE".center(70))
    print("=" * 70)
    print(f"Entrada : {archivo_entrada}")
    print(f"Salida  : {archivo_salida}")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()