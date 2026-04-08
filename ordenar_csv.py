import pandas as pd

# 1. Leer el archivo desordenado
df = pd.read_csv('COMPRAS_supermercado_desordenado_solo_sucursal.csv')
datos = df.to_dict('records')

# 2. Función de Burbuja
def ordenar_por_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['PRSUC'] > lista[j+1]['PRSUC']:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# 3. Ordenar
datos_ordenados = ordenar_por_burbuja(datos)

# 4. GRABAR EL NUEVO ARCHIVO
df_ordenado = pd.DataFrame(datos_ordenados)
df_ordenado.to_csv('COMPRAS_temp_ordenado.csv', index=False)