import pytest
from app.algorithms import ordenamiento_burbuja, busqueda_binaria


# --- Ordenamiento Burbuja ---

def test_burbuja_lista_desordenada():
    assert ordenamiento_burbuja([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_burbuja_lista_ya_ordenada():
    assert ordenamiento_burbuja([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_burbuja_orden_inverso():
    assert ordenamiento_burbuja([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_burbuja_un_elemento():
    assert ordenamiento_burbuja([42]) == [42]

def test_burbuja_lista_vacia():
    assert ordenamiento_burbuja([]) == []

def test_burbuja_duplicados():
    assert ordenamiento_burbuja([3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3]

def test_burbuja_dos_elementos_invertidos():
    assert ordenamiento_burbuja([9, 1]) == [1, 9]


# --- Busqueda Binaria ---

def test_binaria_elemento_en_el_medio():
    assert busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15], 7) != -1

def test_binaria_primer_elemento():
    assert busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15], 1) == 0

def test_binaria_ultimo_elemento():
    arreglo = [1, 3, 5, 7, 9, 11, 13, 15]
    assert busqueda_binaria(arreglo, 15) == len(arreglo) - 1

def test_binaria_elemento_no_encontrado():
    assert busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15], 6) == -1

def test_binaria_lista_vacia():
    assert busqueda_binaria([], 5) == -1

def test_binaria_un_elemento_encontrado():
    assert busqueda_binaria([42], 42) == 0

def test_binaria_un_elemento_no_encontrado():
    assert busqueda_binaria([42], 99) == -1

def test_binaria_menor_al_minimo():
    assert busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15], 0) == -1

def test_binaria_mayor_al_maximo():
    assert busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15], 100) == -1

def test_binaria_indice_correcto():
    assert busqueda_binaria([2, 4, 6, 8, 10], 6) == 2
