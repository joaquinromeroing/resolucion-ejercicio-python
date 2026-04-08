import csv

def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["PRSUC"] > lista[j + 1]["PRSUC"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def leer_registro(archivo):
    try:
        reg = next(archivo)
        reg["PRCANT"] = int(reg["PRCANT"])
        reg["PRPRE"] = float(reg["PRPRE"])
        return reg
    except StopIteration:
        return None

path = input("Ingrese el path del CSV: ")
ordenado = input("El archivo está ordenado? (Y/N): ")

if ordenado.upper() == "N":

    lista = []

    with open(path, newline="", encoding="utf-8") as f:
        archivo = csv.DictReader(f)

        for fila in archivo:
            fila["PRCANT"] = int(fila["PRCANT"])
            fila["PRPRE"] = float(fila["PRPRE"])
            lista.append(fila)

    lista = ordenar_burbuja(lista)

    temp_path = "temp_ordenado.csv"

    with open(temp_path, "w", newline="", encoding="utf-8") as f:
        campos = ["PRSUC", "PRCOD", "PRFEC", "PRPROV", "PRCANT", "PRPRE"]
        writer = csv.DictWriter(f, fieldnames=campos)

        writer.writeheader()
        for fila in lista:
            writer.writerow(fila)

    archivo_final = open(temp_path, newline="", encoding="utf-8")

else:
    archivo_final = open(path, newline="", encoding="utf-8")

archivo = csv.DictReader(archivo_final)

reg = leer_registro(archivo)

cantsucursales = 0
totalimporte = 0

while reg is not None:
    sucursal_actual = reg["PRSUC"]
    totsucursales = 0
    mayor_inicializado = False

    print(f"\nSUCURSAL: {sucursal_actual}")

    while reg is not None and reg["PRSUC"] == sucursal_actual:
        producto_actual = reg["PRCOD"]
        totunidades = 0
        totpesos = 0

        while reg is not None and reg["PRSUC"] == sucursal_actual and reg["PRCOD"] == producto_actual:
            importe = reg["PRCANT"] * reg["PRPRE"]

            totunidades += reg["PRCANT"]
            totpesos += importe

            reg = leer_registro(archivo)

        print(f"  PRODUCTO: {producto_actual} | TOTUNI: {totunidades} | TOTPES: ${totpesos:.2f}")

        totsucursales += totunidades
        totalimporte += totpesos

        if not mayor_inicializado:
            mayor_prod = producto_actual
            mayor_importe = totpesos
            menor_prod = producto_actual
            menor_importe = totpesos
            mayor_inicializado = True
        else:
            if totpesos > mayor_importe:
                mayor_prod = producto_actual
                mayor_importe = totpesos

            if totpesos < menor_importe:
                menor_prod = producto_actual
                menor_importe = totpesos

    print(f"TOTAL UNIDADES SUCURSAL: {totsucursales}")
    print(f"MAYOR COMPRA: {mayor_prod} -> ${mayor_importe:.2f}")
    print(f"MENOR COMPRA: {menor_prod} -> ${menor_importe:.2f}")

    cantsucursales += 1

print("\n--- TOTALES GENERALES ---")
print(f"CANTIDAD DE SUCURSALES: {cantsucursales}")
print(f"TOTAL EN PESOS: ${totalimporte:.2f}")