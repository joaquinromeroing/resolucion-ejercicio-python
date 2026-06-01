from programa import ordenar_burbuja, busqueda_binaria

# ==========================================
# TEST UNITARIOS: ORDENAMIENTO BURBUJA
# ==========================================

def test_ordenar_burbuja_desordenado():
    # Arrange
    datos = [64, 34, 25, 12, 22, 11, 90]
    # Act
    resultado = ordenar_burbuja(datos)
    # Assert
    assert resultado == [11, 12, 22, 25, 34, 64, 90]

def test_ordenar_burbuja_ya_ordenado():
    datos = [1, 2, 3, 4, 5]
    resultado = ordenar_burbuja(datos)
    assert resultado == [1, 2, 3, 4, 5]

def test_ordenar_burbuja_vacio():
    datos = []
    resultado = ordenar_burbuja(datos)
    assert resultado == []


# ==========================================
# TEST UNITARIOS: BÚSQUEDA BINARIA
# ==========================================

def test_busqueda_binaria_elemento_presente():
    # Arrange (La lista DEBE estar ordenada para la búsqueda binaria)
    lista_ordenada = [11, 12, 22, 25, 34, 64, 90]
    objetivo = 25
    # Act
    encontrado = busqueda_binaria(lista_ordenada, objetivo)
    # Assert
    assert encontrado is True

def test_busqueda_binaria_elemento_ausente():
    lista_ordenada = [11, 12, 22, 25, 34, 64, 90]
    objetivo = 99
    resultado = busqueda_binaria(lista_ordenada, objetivo)
    assert resultado is False

def test_busqueda_binaria_lista_vacia():
    lista_ordenada = []
    objetivo = 10
    resultado = busqueda_binaria(lista_ordenada, objetivo)
    assert resultado is False