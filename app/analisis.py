import pandas as pd

df = pd.read_csv("/data/COMPRAS_supermercado.csv") 

resultado = df["PRPRE"].mean()

with open("/output/resultado.txt", "w") as f:
    f.write(f"El promedio de las compras (PRPRE) es: {resultado}")

print("Análisis terminado con éxito.")