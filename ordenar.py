archivo = open("compras_supermercado_desordenado_solo_sucursal.csv", "r")
linea = archivo.readline().strip()

datos = []

while linea != "":
    data = linea.split(",")
    datos.append(data)
    linea = archivo.readline().strip()

archivo.close()

def Ordenar_productos(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][0] > lista[j + 1][0]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

Ordenar_productos(datos)

print("Datos ordenados por sucursal:")
for file in datos:
    print(file)

archivo_ordenado = open("compras_ordenado.csv", "w")

for file in datos:
    linea = ",".join(file)
    archivo_ordenado.write(linea + "\n")

archivo_ordenado.close()