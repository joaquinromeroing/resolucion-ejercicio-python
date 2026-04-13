import pandas as pd
# Lee desde la ruta interna del contenedor
df = pd.read_csv("/data/datos.csv")
resultado = df["valor"].mean()
# Escribe en la ruta del volumen
with open("/output/resultado.txt", "w") as f:
    f.write(f"Promedio: {resultado}")
print("Análisis terminado")
