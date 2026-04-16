import pandas as pd

try:
    df = pd.read_csv("/data/datos.csv")
    resultado = df["valor"].mean()

    with open("/output/resultado.txt", "w") as f:
        f.write(f"Promedio: {resultado}")
    
    print(f"Análisis terminado. El promedio es: {resultado}")
except Exception as e:
    print(f"Error: {e}")