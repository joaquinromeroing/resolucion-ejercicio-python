import pandas as pd
import os
from typing import List, Dict, Any

# --- CONSTANTES ---
COL_SUCURSAL = 'PRSUC'
COL_PRODUCTO = 'PRCOD'
COL_CANTIDAD = 'PRCANT'
COL_PRECIO = 'PRPRE'

# --- 1. CAPA DE DATOS (Data Access) ---
def leer_csv(path: str) -> List[Dict[str, Any]]:
    """Lee el CSV y maneja errores de archivo."""
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo {path} no existe.")
        return pd.read_csv(path).to_dict('records')
    except Exception as e:
        print(f"Error crítico de lectura: {e}")
        return []

# --- 2. CAPA DE ALGORITMOS (Sorting) ---
def ordenar_datos_burbuja(datos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Algoritmo de ordenamiento por sucursal."""
    lista = datos.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][COL_SUCURSAL] > lista[j+1][COL_SUCURSAL]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# --- 3. CAPA DE LÓGICA (Business Logic) ---
def calcular_subtotal(cantidad: float, precio: float) -> float:
    """Función aritmética simple (Ideal para Test Unitario)."""
    return cantidad * precio

def procesar_ventas(datos: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Procesa el Corte de Control y devuelve una estructura de datos.
    NO CONTIENE PRINTS. Esto la hace 100% testeable.
    """
    resultados = {
        'sucursales': [],
        'total_general': {'cansuc': 0, 'totalimp': 0.0}
    }
    
    i = 0
    total_registros = len(datos)
    
    while i < total_registros:
        suc_actual = datos[i][COL_SUCURSAL]
        info_sucursal = {
            'id': suc_actual,
            'productos': [],
            'totsuc': 0,
            'max_prod': {'prod': '', 'valor': -1.0},
            'min_prod': {'prod': '', 'valor': float('inf')}
        }
        
        acum_suc_pesos = 0
        
        while i < total_registros and datos[i][COL_SUCURSAL] == suc_actual:
            prod_actual = datos[i][COL_PRODUCTO]
            tot_uni = 0
            tot_pesos = 0
            
            while i < total_registros and datos[i][COL_SUCURSAL] == suc_actual and datos[i][COL_PRODUCTO] == prod_actual:
                sub = calcular_subtotal(datos[i][COL_CANTIDAD], datos[i][COL_PRECIO])
                tot_uni += datos[i][COL_CANTIDAD]
                tot_pesos += sub
                i += 1
            
            # Guardamos info de producto
            info_sucursal['productos'].append({
                'id': prod_actual, 'unidades': tot_uni, 'pesos': tot_pesos
            })
            
            # Lógica de máximos/mínimos
            if tot_pesos > info_sucursal['max_prod']['valor']:
                info_sucursal['max_prod'] = {'prod': prod_actual, 'valor': tot_pesos}
            if tot_pesos < info_sucursal['min_prod']['valor']:
                info_sucursal['min_prod'] = {'prod': prod_actual, 'valor': tot_pesos}
                
            info_sucursal['totsuc'] += tot_uni
            acum_suc_pesos += tot_pesos

        resultados['sucursales'].append(info_sucursal)
        resultados['total_general']['totalimp'] += acum_suc_pesos
        resultados['total_general']['cansuc'] += 1

    return resultados

# --- 4. CAPA DE PRESENTACIÓN (UI) ---
def presentar_resultados(res: Dict[str, Any]):
    """Única función con permiso para usar print."""
    for suc in res['sucursales']:
        for p in suc['productos']:
            print(f" Producto: {p['id']} | Unidades: {p['unidades']} | Ingresos: ${p['pesos']:.2f}")
        
        print("\n" + "." * 60)
        print(f" SUCURSAL {suc['id']}:")
        print(f" - Total unidades (TOTSUC): {suc['totsuc']}")
        print(f" - Mayor compra: {suc['max_prod']['prod']} (${suc['max_prod']['valor']:.2f})")
        print(f" - Menor compra: {suc['min_prod']['prod']} (${suc['min_prod']['valor']:.2f})")
        print("." * 60)

    tg = res['total_general']
    print(f"\nESTADÍSTICA TOTAL: Sucursales: {tg['cansuc']} | Total: ${tg['totalimp']:.2f}")

# --- MAIN ---
def main():
    path = input("Path del CSV: ")
    datos = leer_csv(path)
    if not datos: return

    if input("¿Ordenar? (Y/N): ").upper() == 'Y':
        datos = ordenar_datos_burbuja(datos)

    # El "Cerebro" procesa todo y devuelve datos puros
    resultados = procesar_ventas(datos)
    
    # La "Voz" muestra los datos
    presentar_resultados(resultados)

if __name__ == "__main__":
    main()
