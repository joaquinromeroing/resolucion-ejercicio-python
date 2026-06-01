from main import ordenar_burbuja, busqueda_binaria


def test_burbuja():
    numeros = [8, 3, 1, 5, 2]

    resultado = ordenar_burbuja(numeros)

    assert resultado == [1, 2, 3, 5, 8]


def test_burbuja_lista_vacia():
    numeros = []

    resultado = ordenar_burbuja(numeros)

    assert resultado == []


def test_busqueda_encontrado():
    numeros = [1, 2, 3, 5, 8]

    resultado = busqueda_binaria(numeros, 5)

    assert resultado is True


def test_busqueda_no_encontrado():
    numeros = [1, 2, 3, 5, 8]

    resultado = busqueda_binaria(numeros, 10)

    assert resultado is False