from main import burbuja, busqueda_binaria


def test_burbuja():
    numeros = [5, 3, 8, 1, 2]
    resultado = burbuja(numeros)
    assert resultado == [1, 2, 3, 5, 8]


def test_busqueda_binaria_encontrado():
    numeros = [1, 2, 3, 5, 8]
    assert busqueda_binaria(numeros, 5) is True


def test_busqueda_binaria_no_encontrado():
    numeros = [1, 2, 3, 5, 8]
    assert busqueda_binaria(numeros, 7) is False