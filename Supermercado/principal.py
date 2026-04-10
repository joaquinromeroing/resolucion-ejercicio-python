import os
import csv

def algoritmo_burbuja(registros):
    n = len(registros)
    for i in range(n):
        for j in range(0, n - i - 1):
            if registros[j]['PRSUC'] > registros[j + 1]['PRSUC']:
                registros[j], registros[j + 1] = registros[j + 1], registros[j]
    return registros


def process(ruta_del_archivo):
    with open(ruta_del_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        registros = list(lector)

    print("\nProcesando los datos...")

    i = 0
    CANSUC = 0
    TOTALIMP = 0

    while i < len(registros):
        suc_actual = registros[i]['PRSUC']

        TOTSUC = 0
        MYPROD = None
        MYIMPOR = 0
        MNPROD = None
        MNIMPOR = 1000000000

        print("=" * 55)
        print(f"  SUCURSAL: {suc_actual}")
        print("-" * 55)

        while i < len(registros) and registros[i]['PRSUC'] == suc_actual:

            prod_actual = registros[i]['PRCOD']

            TOTUNI = 0
            TOTPES = 0.0

            while i < len(registros) and registros[i]['PRSUC'] == suc_actual and registros[i]['PRCOD'] == prod_actual:
                fila = registros[i]

                TOTUNI += int(fila['PRCANT'])
                TOTPES += int(fila['PRCANT']) * float(fila['PRPRE'])
                i += 1

            TOTSUC += TOTUNI
            TOTALIMP += TOTPES
            print(f"  > {prod_actual:<10} | Unidades: {TOTUNI:>8} | Pesos: ${TOTPES:>12.2f}")

            if TOTPES > MYIMPOR:
                MYIMPOR = TOTPES
                MYPROD = prod_actual

            if TOTPES < MNIMPOR:
                MNIMPOR = TOTPES
                MNPROD = prod_actual

        print("-" * 55)
        print(f"  Total unidades compradas: {TOTSUC:>8}")
        print(f"  El producto mayor vendido fue: {MYPROD}, ingresando: ${MYIMPOR:>12.2f}")
        print(f"  El producto menor vendido fue: {MNPROD}, ingresando: ${MNIMPOR:>12.2f}")
        print("=" * 55)
        print()

        CANSUC += 1

    print("*" * 55)
    print(f"  TOTAL SUCURSALES: {CANSUC}")
    print(f"  INGRESOS TOTALES:    ${TOTALIMP:>12.2f}")
    print("*" * 55)


def menu():
    ruta_csv = input("Indique el path del csv (ej: COMPRAS_supermercado.csv): ").strip()

    if not os.path.exists(ruta_csv):
        print("El archivo no existe.")
        return

    estado = input("¿El archivo esta ordenado? (Y/N): ").strip().upper()

    if estado == 'N':
        print("Generando archivo temporal, aguarde un instante...")
        with open(ruta_csv, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            nombres_columnas = lector.fieldnames
            registros = list(lector)

        registros_ordenados = algoritmo_burbuja(registros)

        ruta_temp = "temp_ordenado.csv"
        with open(ruta_temp, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=nombres_columnas)
            writer.writeheader()
            writer.writerows(registros_ordenados)

        print("Archivo temporal generado. Pasando a tu código original...")
        process(ruta_temp)

    elif estado == 'Y':
        print("Iniciando la ejecución directamente...")
        process(ruta_csv)
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    menu()