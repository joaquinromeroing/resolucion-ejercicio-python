from main import binary_search, bubble_sort


def test_bubble_sort_ordena_ascendente():
    numeros = [5, 3, 8, 1, 2]

    assert bubble_sort(numeros) == [1, 2, 3, 5, 8]


def test_bubble_sort_no_modifica_la_lista_original():
    numeros = [4, 2, 7]

    resultado = bubble_sort(numeros)

    assert numeros == [4, 2, 7]
    assert resultado == [2, 4, 7]


def test_binary_search_encuentra_elemento_existente():
    numeros = [1, 2, 3, 5, 8]

    assert binary_search(numeros, 5) is True


def test_binary_search_no_encuentra_elemento_inexistente():
    numeros = [1, 2, 3, 5, 8]

    assert binary_search(numeros, 4) is False
