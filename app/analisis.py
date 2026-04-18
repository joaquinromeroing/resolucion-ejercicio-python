import pandas as pd

df = pd.read_csv("data/datos.csv")
resultado = df["valor"].mean()

with open("output/resultado.txt", "w") as f:
        f.write(f"Promedio: {resultado}")

print("Análisis terminado")
