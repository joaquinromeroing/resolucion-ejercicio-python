import csv

datos = []

with open('COMPRAS_supermercado_desordenado.csv', mode='r', encoding='utf-8') as archivo:
    lector_csv = csv.DictReader(archivo)

    for fila in lector_csv:
        fila['PRCANT'] = int(fila['PRCANT'])
        fila['PRPRE'] = float(fila['PRPRE'])
        datos.append(fila)

n = len(datos)

print(f"Ordenando {n} registros por sucursal... Por favor espera.")

for i in range(n):
    for j in range(0, n - i - 1):
        if datos[j]['PRSUC'] > datos[j+1]['PRSUC']:
            aux = datos[j]
            datos[j] = datos[j+1]
            datos[j+1] = aux

print("Ordenamiento finalizado.")

columnas = datos[0].keys()

with open('COMPRAS_supermercado_ordenado.csv', mode='w', encoding='utf-8', newline='') as archivo_salida:
    escritor = csv.DictWriter(archivo_salida, fieldnames=columnas)
    
    escritor.writeheader()
    escritor.writerows(datos)

print("Se ha creado el archivo 'COMPRAS_supermercado_ordenado.csv' con éxito.")