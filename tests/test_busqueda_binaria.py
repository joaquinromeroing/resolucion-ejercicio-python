from busqueda_binaria import ordenar_burbuja, busqueda_binaria


def test_ordenar_burbuja_lista_desordenada():
    # Arrange
    Numeros = [5, 2, 9, 1, 7]

    # Act
    resultado = ordenar_burbuja(Numeros)

    # Assert
    assert resultado == [1, 2, 5, 7, 9]


def test_ordenar_burbuja_lista_ya_ordenada():
    # Arrange
    Numeros = [1, 2, 3, 4, 5]

    # Act
    resultado = ordenar_burbuja(Numeros)

    # Assert
    assert resultado == [1, 2, 3, 4, 5]


def test_ordenar_burbuja_con_numeros_repetidos():
    # Arrange
    Numeros = [4, 2, 4, 1, 2]

    # Act
    resultado = ordenar_burbuja(Numeros)

    # Assert
    assert resultado == [1, 2, 2, 4, 4]


def test_busqueda_binaria_numero_encontrado():
    # Arrange
    Numeros = [1, 3, 5, 7, 9]
    numero_buscado = 7

    # Act
    resultado = busqueda_binaria(Numeros, numero_buscado)

    # Assert
    assert resultado == True


def test_busqueda_binaria_numero_no_encontrado():
    # Arrange
    Numeros = [1, 3, 5, 7, 9]
    numero_buscado = 4

    # Act
    resultado = busqueda_binaria(Numeros, numero_buscado)

    # Assert
    assert resultado == False


def test_busqueda_binaria_lista_vacia():
    # Arrange
    Numeros = []
    numero_buscado = 10

    # Act
    resultado = busqueda_binaria(Numeros, numero_buscado)

    # Assert
    assert resultado == False


def test_busqueda_binaria_un_solo_elemento_encontrado():
    # Arrange
    Numeros = [8]
    numero_buscado = 8

    # Act
    resultado = busqueda_binaria(Numeros, numero_buscado)

    # Assert
    assert resultado == True
