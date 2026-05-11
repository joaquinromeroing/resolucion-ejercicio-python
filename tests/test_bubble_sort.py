# tests/test_ordenar.py
import pytest
from src.bubble_sort import bubble_sort_sucursales

def test_bubble_sort_sucursales_orden_alfabetico():
    """Prueba que el ordenamiento alfabético sea correcto."""
    entrada = [
        "Zarate,Harina,100\n",
        "Abasto,Leche,50\n",
        "Rosario,Azucar,80\n"
    ]
    
    esperado = [
        "Abasto,Leche,50\n",
        "Rosario,Azucar,80\n",
        "Zarate,Harina,100\n"
    ]
    
    resultado = bubble_sort_sucursales(entrada)
    assert resultado == esperado

def test_bubble_sort_datos_repetidos():
    """Prueba que funcione correctamente con sucursales repetidas."""
    entrada = [
        "Rosario,ProductoA,10\n",
        "Abasto,ProductoB,20\n",
        "Rosario,ProductoC,30\n"
    ]
    
    # Abasto debería quedar primero, los de Rosario mantienen su orden relativo
    resultado = bubble_sort_sucursales(entrada)
    assert resultado[0].startswith("Abasto")
    assert resultado[1].startswith("Rosario")

def test_bubble_sort_lista_vacia():
    """Prueba el comportamiento con una lista sin datos."""
    assert bubble_sort_sucursales([]) == []

def test_bubble_sort_una_sola_fila():
    """Prueba con una sola fila."""
    entrada = ["Rosario,Harina,100\n"]
    assert bubble_sort_sucursales(entrada) == entrada