import pandas as pd

df = pd.read_csv('COMPRAS_supermercado.csv')
datos = df.values.tolist()

n_filas = len(datos)
i = 0

tot_gral_pesos = 0
cant_suc = 0

productos = []
unidades = []
pesos = []

resultados_suc = []

while i < n_filas:
    suc_actual = datos[i][0]
    tot_uni_suc = 0
    mayor_imp = None
    menor_imp = None
    prod_mayor = ""
    prod_menor = ""
    cant_suc += 1

    while i < n_filas and datos[i][0] == suc_actual:
        prod_actual = datos[i][1]
        tot_pesos_prod = 0

        while i < n_filas and datos[i][0] == suc_actual and datos[i][1] == prod_actual:
            cant = datos[i][4]
            precio = datos[i][5]
            importe = cant * precio

            tot_pesos_prod += importe
            tot_uni_suc += cant
            tot_gral_pesos += importe
            
            if prod_actual not in productos:
                productos.append(prod_actual)
                unidades.append(0)
                pesos.append(0)
            
            pos = productos.index(prod_actual)
            unidades[pos] += cant
            pesos[pos] += importe

            i += 1

        if mayor_imp is None or tot_pesos_prod > mayor_imp:
            mayor_imp = tot_pesos_prod
            prod_mayor = prod_actual
            
        if menor_imp is None or tot_pesos_prod < menor_imp:
            menor_imp = tot_pesos_prod
            prod_menor = prod_actual

    texto_suc = f"SUCURSAL {suc_actual} - Total unidades: {tot_uni_suc}\n  Mayor compra: {prod_mayor} (${mayor_imp}) - Menor compra: {prod_menor} (${menor_imp})\n"
    resultados_suc.append(texto_suc)

print("a) TOTALES POR PRODUCTO")
j = 0
while j < len(productos):
    print(f"Producto {productos[j]}: {unidades[j]} unidades - ${pesos[j]}")
    j += 1

print("\nb) TOTALES POR SUCURSAL")
k = 0
while k < len(resultados_suc):
    print(resultados_suc[k], end="")
    k += 1

print("\nc) TOTALES GENERALES")
print(f"Cantidad de sucursales: {cant_suc}")
print(f"Compra total general: ${tot_gral_pesos}")