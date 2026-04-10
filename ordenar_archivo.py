import csv
def ordenar():
    with open('COMPRAS_desordenado.csv', mode='r', encoding='utf-8') as f:
        lector = csv.reader(f)
        cabecera = next(lector)
        datos = list(lector)
    datos.sort(key=lambda x: (x[0], x[1]))
    with open('COMPRAS_ordenado_final.csv', mode='w', encoding='utf-8', newline='') as f_n:
        escritor = csv.writer(f_n)
        escritor.writerow(cabecera)
        escritor.writerows(datos)
if __name__ == "__main__":
    ordenar()
