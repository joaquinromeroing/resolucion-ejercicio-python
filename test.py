import pytest
from main import burbuja, busqueda_binaria

# Tests para el ordenamiento burbuja

def test_burbuja_desordenado():
    arreglo = [64, 34, 25, 12, 22, 11, 90]
    esperado = [11, 12, 22, 25, 34, 64, 90]
    assert burbuja(arreglo) == esperado

def test_burbuja_ya_ordenado():
    arreglo = [1, 2, 3, 4, 5]
    esperado = [1, 2, 3, 4, 5]
    assert burbuja(arreglo) == esperado

def test_burbuja_con_duplicados():
    arreglo = [5, 1, 4, 2, 8, 1, 5]
    esperado = [1, 1, 2, 4, 5, 5, 8]
    assert burbuja(arreglo) == esperado

def test_burbuja_vacio():
    arreglo = []
    esperado = []
    assert burbuja(arreglo) == esperado

# Tests para la busqueda binaria

def test_busqueda_binaria_encontrado_medio():
    arreglo_ordenado = [2, 3, 4, 10, 40]
    assert busqueda_binaria(arreglo_ordenado, 10) == True

def test_busqueda_binaria_encontrado_extremos():
    arreglo_ordenado = [1, 5, 8, 12, 15]
    assert busqueda_binaria(arreglo_ordenado, 1) == True
    assert busqueda_binaria(arreglo_ordenado, 15) == True

def test_busqueda_binaria_no_encontrado():
    arreglo_ordenado = [2, 4, 6, 8, 10]
    assert busqueda_binaria(arreglo_ordenado, 1) == False
    assert busqueda_binaria(arreglo_ordenado, 5) == False
    assert busqueda_binaria(arreglo_ordenado, 11) == False

def test_busqueda_binaria_vacio():
    arreglo_ordenado = []
    assert busqueda_binaria(arreglo_ordenado, 5) == False