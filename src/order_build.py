import csv
import os


def order_build():
    directorio_script = os.path.dirname(os.path.abspath(__file__))

    if os.path.basename(directorio_script) == 'src':
        directorio_base = os.path.dirname(directorio_script)
    else:
        directorio_base = directorio_script

    ruta_entrada = os.path.join(directorio_base, 'data', 'compras_desordenado.csv')
    ruta_salida = os.path.join(directorio_base, 'data', 'compras_ordenado.csv')
    # ----------------------------

    try:
        with open(ruta_entrada, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
    except FileNotFoundError:
        print(f"Error: No se encuentra el archivo en la ruta absoluta:\n{ruta_entrada}")
        print("Chequeá que la carpeta 'data' exista y el nombre del archivo sea idéntico.")
        return

    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j + 1] = data[j + 1], data[j]

    with open(ruta_salida, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    print(f"¡Éxito! Archivo leído, ordenado y guardado como '{ruta_salida}'")


if __name__ == "__main__":
    order_build()