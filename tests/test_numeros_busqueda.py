import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from numeros_busqueda import ordenar_burbuja, busqueda_binaria, es_numero_valido


def test_ordenar_burbuja_lista_desordenada():
    Numeros = [8, 3, 10, 1]
    resultado = ordenar_burbuja(Numeros)
    assert resultado == [1, 3, 8, 10]


def test_ordenar_burbuja_lista_ya_ordenada():
    Numeros = [1, 3, 8, 10]
    resultado = ordenar_burbuja(Numeros)
    assert resultado == [1, 3, 8, 10]


def test_busqueda_binaria_numero_encontrado():
    Numeros = [1, 3, 8, 10]
    resultado = busqueda_binaria(Numeros, 8)
    assert resultado == True


def test_busqueda_binaria_numero_no_encontrado():
    Numeros = [1, 3, 8, 10]
    resultado = busqueda_binaria(Numeros, 5)
    assert resultado == False


def test_es_numero_valido():
    assert es_numero_valido(1) == True
    assert es_numero_valido(100000) == True
    assert es_numero_valido(0) == True
    assert es_numero_valido(-1) == False
    assert es_numero_valido(100001) == False