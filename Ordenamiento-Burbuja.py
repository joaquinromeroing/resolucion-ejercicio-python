import csv

def ordenar_burbuja(filas):
    n = len(filas)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if filas[j]["PRSUC"] > filas[j + 1]["PRSUC"]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
    
    return filas


# Leer archivo desordenado
archivo = open("COMPRAS_supermercado_desordenado_solo_sucursal.csv", encoding="utf-8")
lector = csv.DictReader(archivo)
filas = list(lector)
encabezados = lector.fieldnames
archivo.close()

# Ordenar con burbuja
filas = ordenar_burbuja(filas)

# Guardar archivo ordenado
archivo = open("COMPRAS_ordenado.csv", "w", newline="", encoding="utf-8")
escritor = csv.DictWriter(archivo, fieldnames=encabezados)
escritor.writeheader()
escritor.writerows(filas)
archivo.close()