import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from algorithms import bubble_sort, binary_search


# ── Ordenamiento Burbuja ──────────────────────────────────────────────────────

def test_bubble_sort_caso_general():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]

def test_bubble_sort_lista_ya_ordenada():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_bubble_sort_lista_vacia():
    assert bubble_sort([]) == []

def test_bubble_sort_un_elemento():
    assert bubble_sort([42]) == [42]

def test_bubble_sort_con_duplicados():
    assert bubble_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

def test_bubble_sort_no_modifica_original():
    original = [3, 1, 2]
    bubble_sort(original)
    assert original == [3, 1, 2]


# ── Búsqueda Binaria ──────────────────────────────────────────────────────────

def test_binary_search_encontrado():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2

def test_binary_search_no_encontrado():
    assert binary_search([1, 2, 3, 4, 5], 99) == -1

def test_binary_search_lista_vacia():
    assert binary_search([], 1) == -1

def test_binary_search_un_elemento_encontrado():
    assert binary_search([7], 7) == 0

def test_binary_search_un_elemento_no_encontrado():
    assert binary_search([7], 5) == -1

def test_binary_search_con_duplicados():
    assert binary_search([1, 2, 2, 2, 3], 2) != -1
