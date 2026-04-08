import csv

def ordenar_burbuja(filas):
    n = len(filas)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if filas[j]["PRSUC"] > filas[j + 1]["PRSUC"]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
    
    return filas


# MENU
path = input("Indique el path del csv: ")
ordenado = input("El archivo esta ordenado? (Y/N): ").upper()


# LEER CSV
archivo = open(path, encoding="utf-8")
lector = csv.DictReader(archivo)
filas = list(lector)
encabezados = lector.fieldnames
archivo.close()


# SI NO ESTA ORDENADO
if ordenado == "N":
    print("Ordenando archivo...")
    
    filas = ordenar_burbuja(filas)
    
    archivo_temp = "archivo_ordenado_temp.csv"
    
    archivo = open(archivo_temp, "w", newline="", encoding="utf-8")
    escritor = csv.DictWriter(archivo, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(filas)
    archivo.close()
    
    path = archivo_temp


# LEER ARCHIVO (ya ordenado)
archivo = open(path, encoding="utf-8")
lector = csv.DictReader(archivo)
filas = list(lector)
archivo.close()


# CORTE DE CONTROL
n = len(filas)
i = 0
CANSUC = 0
TOTALIMP = 0

while i < n:
    suc_actual = filas[i]["PRSUC"]
    TOTSUC = 0
    IMP_SUC = 0
    MYPROD = ""
    MYIMPOR = -1
    MNPROD = ""
    MNIMPOR = 999999999

    while i < n and filas[i]["PRSUC"] == suc_actual:
        prod_actual = filas[i]["PRCOD"]

        TOTUNI = 0
        TOTPES = 0

        while (i < n and filas[i]["PRSUC"] == suc_actual and filas[i]["PRCOD"] == prod_actual):
            cantidad = int(filas[i]["PRCANT"])
            precio = float(filas[i]["PRPRE"])

            TOTUNI += cantidad
            TOTPES += cantidad * precio

            i += 1

        print(f"Producto {prod_actual}")
        print(f"Total unidades: {TOTUNI}")
        print(f"Total pesos: ${TOTPES:.2f}")

        TOTSUC += TOTUNI
        IMP_SUC += TOTPES

        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = prod_actual

        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD = prod_actual

    print(f"\nSucursal {suc_actual}")
    print(f"Total unidades: {TOTSUC}")
    print(f"Mayor compra: {MYPROD} ${MYIMPOR:.2f}")
    print(f"Menor compra: {MNPROD} ${MNIMPOR:.2f}")

    CANSUC += 1
    TOTALIMP += IMP_SUC


print("\nTotales generales")
print(f"Sucursales: {CANSUC}")
print(f"Total: ${TOTALIMP:.2f}")