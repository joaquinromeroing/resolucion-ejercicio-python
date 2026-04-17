import pandas as pd
import os

# --- FUNCIÓN DE ORDENAMIENTO (Burbuja) ---
def ordenar_por_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['PRSUC'] > lista[j+1]['PRSUC']:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# --- CONFIGURACIÓN PARA DOCKER ---
path_entrada = "/data/COMPRAS_supermercado.csv"
path_salida_csv = "/output/temp_archivo_ordenado.csv"
path_resultado_txt = "/output/resultado.txt"

print(f"Iniciando análisis sobre: {path_entrada}")

# Procesamiento inicial
df = pd.read_csv(path_entrada)
datos_dict = df.to_dict('records')
datos_ordenados = ordenar_por_burbuja(datos_dict)

# Guardamos el CSV ordenado en el volumen
pd.DataFrame(datos_ordenados).to_csv(path_salida_csv, index=False)

# --- PROCESAMIENTO CON REPORTE DETALLADO ---
datos = datos_ordenados
TOTALIMP = 0
CANSUC = 0
i = 0
total_registros = len(datos)

with open(path_resultado_txt, "w") as f_res:
    f_res.write("REPORTE DETALLADO DE VENTAS\n")
    f_res.write("=" * 60 + "\n\n")

    while i < total_registros:
        suc_actual = datos[i]['PRSUC']
        CANSUC += 1
        
        f_res.write(f"SUCURSAL: {suc_actual}\n")
        f_res.write("-" * 60 + "\n")
        
        TOTSUC = 0
        MYPROD = ""; MYIMPOR = -1000000.0
        MNPROD = ""; MNIMPOR = 1000000.0
        acumulado_sucursal_pesos = 0 
        
        while i < total_registros and datos[i]['PRSUC'] == suc_actual:
            prod_actual = datos[i]['PRCOD']
            TOTUNI = 0
            TOTPES = 0
            
            while i < total_registros and datos[i]['PRSUC'] == suc_actual and datos[i]['PRCOD'] == prod_actual:
                subtotal = datos[i]['PRCANT'] * datos[i]['PRPRE']
                TOTUNI += datos[i]['PRCANT']
                TOTPES += subtotal
                i += 1

            # AHORA SÍ: Guardamos el detalle de cada producto en el archivo TXT
            f_res.write(f" Producto: {prod_actual:10} | Unidades: {TOTUNI:5} | Ingresos: ${TOTPES:10.2f}\n")
            
            TOTSUC += TOTUNI
            acumulado_sucursal_pesos += TOTPES
            
            if TOTPES > MYIMPOR:
                MYIMPOR = TOTPES
                MYPROD = prod_actual
            if TOTPES < MNIMPOR:
                MNIMPOR = TOTPES
                MNPROD = prod_actual

        # Resumen de la sucursal
        f_res.write("\n RESULTADOS SUCURSAL:\n")
        f_res.write(f" >> Total unidades compradas: {TOTSUC}\n")
        f_res.write(f" >> Mayor compra (Producto):  {MYPROD} (${MYIMPOR:.2f})\n")
        f_res.write(f" >> Menor compra (Producto):  {MNPROD} (${MNIMPOR:.2f})\n")
        f_res.write("-" * 60 + "\n\n")
        
        TOTALIMP += acumulado_sucursal_pesos
        
    f_res.write("=" * 60 + "\n")
    f_res.write("ESTADÍSTICA TOTAL GENERAL\n")
    f_res.write(f"Total de sucursales: {CANSUC}\n")
    f_res.write(f"Compra total en pesos: ${TOTALIMP:.2f}\n")
    f_res.write("=" * 60 + "\n")

print(f"Análisis terminado. El reporte detallado está en {path_resultado_txt}")