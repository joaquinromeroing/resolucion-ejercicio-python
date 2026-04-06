# =========================================================
#             EJERCICIO SUPERMERCADO DESORDENADO
# =========================================================

import pandas as pd

df = pd.read_csv("COMPRAS_supermercado_desordenado_solo_sucursal.csv")

# Pasarlo a lista de listas para poder aplicar burbuja
registros = df.values.tolist()
columnas = df.columns.tolist()

n = len(registros)

for i in range(n - 1):
    intercambio = False

    for j in range(n - 1 - i):
        suc_actual = int(str(registros[j][0]).replace("SUC", ""))
        suc_siguiente = int(str(registros[j + 1][0]).replace("SUC", ""))

        if suc_actual > suc_siguiente:
            aux = registros[j]
            registros[j] = registros[j + 1]
            registros[j + 1] = aux
            intercambio = True

    if not intercambio:
        break

# Volver a DataFrame
df_ordenado = pd.DataFrame(registros, columns=columnas)

# Guardar archivo nuevo ordenado
df_ordenado.to_csv("COMPRAS_supermercado_ordenado_solo_sucursal.csv", index=False)

print("Archivo ordenado generado correctamente")