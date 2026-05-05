import csv
import os

# --- AGREGÁ ESTA FUNCIÓN AQUÍ ---
def validar_monto_positivo(monto):
    """Retorna True si el monto es mayor a cero."""
    try:
        return float(monto) > 0
    except (ValueError, TypeError):
        return False

def funcion_burbuja(datos):
    """Ordena por PRSUC (0) y PRCOD (1)[cite: 1, 2]."""
    n = len(datos)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (datos[j][0], datos[j][1]) > (datos[j+1][0], datos[j+1][1]):
                datos[j], datos[j+1] = datos[j+1], datos[j]
                swapped = True
        if not swapped: break
    return datos

def calcular_subtotal(cantidad, precio):
    """Multiplica PRCANT por PRPRE."""
    return round(float(cantidad) * float(precio), 2)

def procesar_corte_control(lista_datos):
    """Lógica de 3 whiles anidados basada en PRSUC y PRCOD[cite: 1]."""
    resultados = {}
    i, n = 0, len(lista_datos)
    
    while i < n:
        sucursal_actual = lista_datos[i][0]
        tot_suc_pesos = 0.0
        max_monto, max_prod = -1.0, ""
        
        while i < n and lista_datos[i][0] == sucursal_actual:
            producto_actual = lista_datos[i][1]
            tot_prod_pesos = 0.0
            
            while i < n and lista_datos[i][0] == sucursal_actual and lista_datos[i][1] == producto_actual:
                subtotal = calcular_subtotal(lista_datos[i][4], lista_datos[i][5])
                tot_prod_pesos += subtotal
                i += 1
            
            if tot_prod_pesos > max_monto:
                max_monto, max_prod = tot_prod_pesos, producto_actual
            tot_suc_pesos += tot_prod_pesos
            
        resultados[sucursal_actual] = {"total": round(tot_suc_pesos, 2), "max_p": max_prod}
    return resultados

if __name__ == "__main__":
    archivo = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
    if os.path.exists(archivo):
        with open(archivo, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            datos = list(reader)
        
        opcion = input("¿El archivo ya está ordenado? (S/N): ").upper()
        if opcion == 'N':
            datos = funcion_burbuja(datos)
            
        res = procesar_corte_control(datos)
        for suc, info in res.items():
            print(f"Sucursal: {suc} | Total: ${info['total']} | Líder: {info['max_p']}")