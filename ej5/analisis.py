import pandas as pd
import os

df = pd.read_csv("datos.csv")
promedio = df["valor"].mean()

factor = float(os.getenv("FACTOR", 1))
resultado = promedio * factor

print("Resultado:", resultado)
