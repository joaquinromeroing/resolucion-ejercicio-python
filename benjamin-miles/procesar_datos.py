import pandas as pd

def bubble_sort(data, col_index):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][col_index] > data[j + 1][col_index]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# MENU DE USUARIO
path = input("Indique el path del csv: ")
ordenado = input("El archivo está ordenado? (Y/N): ").upper()

while ordenado not in ["Y", "N"]:
    ordenado = input("Opción inválida. Ingrese Y o N: ").upper()


# LECTURA
df = pd.read_csv(path, sep=";")


# ORDENAMIENTO
if ordenado == "N":

    data = df.values.tolist()
    columnas = df.columns

    col_index = df.columns.get_loc("PRSUC")

    data_ordenada = bubble_sort(data, col_index)

    df = pd.DataFrame(data_ordenada, columns=columnas)

    df.to_csv("archivo_temporal_ordenado.csv", index=False, sep=";")

    print("Archivo temporal ordenado generado. Se continúa la ejecución con ese archivo.")


# CALCULO IMPORTE
df["PRIMPORTE"] = df["PRCANT"] * df["PRPRE"]


# CORTE DE CONTROL
i = 0
n = len(df)

resultados = []
total_general = 0

while i < n:

    sucursal = df.loc[i, "PRSUC"]
    total_sucursal = 0

    while i < n and df.loc[i, "PRSUC"] == sucursal:
        total_sucursal += df.loc[i, "PRIMPORTE"]
        i += 1

    resultados.append([sucursal, total_sucursal])
    total_general += total_sucursal


# RESULTADOS
df_resultados = pd.DataFrame(resultados, columns=["Sucursal", "Total Comprado"])

print("\nResultados por sucursal:")
print(df_resultados.to_string(index=False))

print("\nTotal general:", round(total_general, 2))