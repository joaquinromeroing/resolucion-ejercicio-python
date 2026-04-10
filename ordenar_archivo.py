import csv

def ordenar():
    with open('COMPRAS_desordenado.csv', mode='r', encoding='utf-8') as f:
        lector = csv.reader(f)
        cabecera = next(lector)
        datos = list(lector)

    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara Sucursal (col 0) y luego Producto (col 1)
            if (datos[j][0], datos[j][1]) > (datos[j + 1][0], datos[j + 1][1]):
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    with open('COMPRAS_ordenado_final.csv', mode='w', encoding='utf-8', newline='') as f_n:
        escritor = csv.writer(f_n)
        escritor.writerow(cabecera)
        escritor.writerows(datos)

if __name__ == "__main__":
    ordenar()
