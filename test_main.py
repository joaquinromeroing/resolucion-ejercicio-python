import pytest
# Importamos las constantes y funciones de tu main
from main import (
    calcular_subtotal, 
    ordenar_datos_burbuja, 
    procesar_ventas,
    COL_SUCURSAL,
    COL_PRODUCTO,
    COL_CANTIDAD,
    COL_PRECIO
)

# --- 1. TEST DE ARITMÉTICA (Función calcular_subtotal) ---
def test_calcular_subtotal():
    """Verifica que el cálculo de precio x cantidad sea exacto."""
    assert calcular_subtotal(5, 100) == 500.0
    assert calcular_subtotal(2.5, 10) == 25.0
    assert calcular_subtotal(0, 50) == 0.0

# --- 2. TEST DE ALGORITMO (Función ordenar_datos_burbuja) ---
def test_ordenar_datos_burbuja():
    """Verifica que el ordenamiento por sucursal funcione."""
    datos_sucios = [
        {COL_SUCURSAL: 5, COL_PRODUCTO: 'P1'},
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'P2'},
        {COL_SUCURSAL: 3, COL_PRODUCTO: 'P3'}
    ]
    resultado = ordenar_datos_burbuja(datos_sucios)
    
    # Comprobamos el orden ascendente
    assert resultado[0][COL_SUCURSAL] == 1
    assert resultado[1][COL_SUCURSAL] == 3
    assert resultado[2][COL_SUCURSAL] == 5

# --- 3. TEST DE LÓGICA DE NEGOCIO (Función procesar_ventas) ---
def test_procesar_ventas_totales():
    """Prueba el Corte de Control sin usar archivos reales."""
    datos_prueba = [
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'A', COL_CANTIDAD: 2, COL_PRECIO: 50},  # 100
        {COL_SUCURSAL: 1, COL_PRODUCTO: 'A', COL_CANTIDAD: 1, COL_PRECIO: 50},  # 50 -> Total Suc 1: 150
        {COL_SUCURSAL: 2, COL_PRODUCTO: 'B', COL_CANTIDAD: 1, COL_PRECIO: 200}  # 200 -> Total Suc 2: 200
    ]
    
    res = procesar_ventas(datos_prueba)
    
    # Validamos los puntos clave del ejercicio:
    assert res['total_general']['cansuc'] == 2 # Detectó 2 sucursales
    assert res['total_general']['totalimp'] == 350.0 # El total general es correcto
    assert len(res['sucursales'][0]['productos']) == 1 # Consolidó los dos registros de 'A' en uno solo

# --- 4. TEST DE ROBUSTEZ (Lista vacía) ---
def test_procesar_ventas_vacio():
    """Verifica que el sistema no falle si no hay datos."""
    res = procesar_ventas([])
    assert res['total_general']['totalimp'] == 0.0
    assert res['sucursales'] == []
