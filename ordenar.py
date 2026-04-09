import os
import csv 

with open('compras_desordenado.csv','r') as file:
    lines = file.readlines()

Datos = []
Encabezado = ""

for l in lines:
    if "PRSUC" in l:
        Encabezado = l
    elif l.strip():
        Datos.append(l)

n = len(Datos)
for i in range(n):
    for j in range(0, n - i - 1):
        col_Actual = Datos[j].strip().split(',')
        col_siguiente = Datos[j+1].strip().split(',')
        
        if col_Actual[0] > col_siguiente[0]:
            temp = Datos[j]
            Datos[j] = Datos[j+1]
            Datos[j+1] = temp
        elif col_Actual[0] == col_siguiente[0]:
            if col_Actual[1] > col_siguiente[1]:
                temp = Datos[j]
                Datos[j] = Datos[j+1]
                Datos[j+1] = temp
            elif col_Actual[1] == col_siguiente[1]:
                if col_Actual[2] > col_siguiente[2]:
                    temp = Datos[j]
                    Datos[j] = Datos[j+1]
                    Datos[j+1] = temp

with open('compras_ordenado.csv','w') as order_file:
    order_file.write(Encabezado)
    for linea in Datos:
        order_file.write(linea)

print("Archivo Ordenado")


