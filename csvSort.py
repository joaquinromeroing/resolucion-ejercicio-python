import pandas as pd

df = pd.read_csv("COMPRAS_supermercado_desordenado_solo_sucursal.csv")
columns = df.columns
df.dropna()

columns = ["PRSUC", "PRCOD", "PRFEC"]

rows = df.to_dict(orient="records")

lenght = len(rows)
for i in range(lenght):
    for j in range(0, lenght - i - 1):
        swap = False
        for col in columns:
            if rows[j][col] > rows[j + 1][col]:
                swap = True
                break
            elif rows[j][col] < rows[j + 1][col]:
                break
        if swap:
            rows[j], rows[j + 1] = rows[j + 1], rows[j]

sortedDf = pd.DataFrame(rows)
sortedDf.to_csv("COMPRAS_supermercado_ordenado.csv", index=False)