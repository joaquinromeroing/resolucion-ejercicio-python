import csv
import os

ARCHIVO_SALIDA   = "datos_ordenados.csv"
COLUMNA_1        = "PRSUC"   # clave primaria
COLUMNA_2        = "PRCOD"   # clave secundaria
ORDEN_ASCENDENTE = True


def bubble_sort(arr, key_fn):
    """Bubble Sort sobre una lista de filas usando key_fn como comparador."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if key_fn(arr[j]) > key_fn(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def clave_doble(fila):
    """Ordena primero por PRSUC y luego por PRCOD."""
    return (fila[COLUMNA_1], fila[COLUMNA_2])


def leer_csv(ruta):
    with open(ruta, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        filas = list(reader)
        encabezados = reader.fieldnames
    return filas, encabezados


def escribir_csv(ruta, filas, encabezados):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=encabezados)
        writer.writeheader()
        writer.writerows(filas)


def main():
    print("=" * 50)
    print("   ORDENADOR DE CSV - BUBBLE SORT")
    print("=" * 50)

    # Pedir path del CSV
    ruta = input("\nIndique el path del CSV: ").strip()
    if not os.path.exists(ruta):
        print(f"Error: no se encontró el archivo '{ruta}'.")
        return

    # Preguntar si ya está ordenado
    resp = input("¿El archivo ya está ordenado? (Y/N): ").strip().upper()

    if resp == "Y":
        print("El archivo ya está ordenado, no se realizan cambios.")
        return

    elif resp == "N":
        print(f"\nLeyendo '{ruta}'...")
        filas, encabezados = leer_csv(ruta)
        print(f"   {len(filas)} filas encontradas.")

        for col in [COLUMNA_1, COLUMNA_2]:
            if col not in encabezados:
                print(f"Error: La columna '{col}' no existe.")
                print(f"Columnas disponibles: {encabezados}")
                return

        print(f"Ordenando por '{COLUMNA_1}' y '{COLUMNA_2}' con Bubble Sort...")
        bubble_sort(filas, clave_doble)

        if not ORDEN_ASCENDENTE:
            filas.reverse()

        escribir_csv(ARCHIVO_SALIDA, filas, encabezados)
        print(f"Archivo guardado como '{ARCHIVO_SALIDA}'.")
        print(f"Primera fila → {COLUMNA_1}: {filas[0][COLUMNA_1]}  {COLUMNA_2}: {filas[0][COLUMNA_2]}")
        print(f"Última  fila → {COLUMNA_1}: {filas[-1][COLUMNA_1]}  {COLUMNA_2}: {filas[-1][COLUMNA_2]}")

    else:
        print("Opción inválida. Ingresá Y o N.")


if __name__ == "__main__":
    main()