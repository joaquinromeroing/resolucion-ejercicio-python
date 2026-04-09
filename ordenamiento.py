import pandas as pd

ARCHIVO_ENTRADA = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
ARCHIVO_SALIDA  = "COMPRAS_supermercado_ordenado.csv"

# PASO 1: Leer el CSV con pandas
df = pd.read_csv(ARCHIVO_ENTRADA)
filas = df.to_dict(orient='records')  # Convierte el DataFrame a lista de diccionarios

# PASO 2: Ordenar con Bubble Sort
def clave_orden(fila):
    return (fila['PRSUC'], fila['PRCOD'], fila['PRFEC'])

n = len(filas)
print(f"Ordenando {n} registros con Bubble Sort...")    

for i in range(n - 1):
    for j in range(n - 1 - i):
        if clave_orden(filas[j]) > clave_orden(filas[j + 1]):
            filas[j], filas[j + 1] = filas[j + 1], filas[j]
    if i % 500 == 0:
        print(f"  Pasada {i + 1} de {n - 1}...")

print("Ordenamiento completado.")

# PASO 3: Convertir la lista ordenada a DataFrame y guardar
df_ordenado = pd.DataFrame(filas)
df_ordenado.to_csv(ARCHIVO_SALIDA, index=False)

print(f"Archivo ordenado guardado como: {ARCHIVO_SALIDA}")
