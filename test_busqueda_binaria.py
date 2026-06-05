import pytest
from busqueda_binaria import BusquedaBinaria


@pytest.fixture
def app():
    return BusquedaBinaria()


class TestOrdenarBurbuja:

    def test_lista_desordenada(self, app):
        assert app.ordenar_burbuja([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

    def test_lista_ya_ordenada(self, app):
        assert app.ordenar_burbuja([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_lista_inversa(self, app):
        assert app.ordenar_burbuja([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_lista_un_elemento(self, app):
        assert app.ordenar_burbuja([42]) == [42]

    def test_lista_vacia(self, app):
        assert app.ordenar_burbuja([]) == []

    def test_lista_con_duplicados(self, app):
        assert app.ordenar_burbuja([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

    def test_no_modifica_original(self, app):
        original = [3, 1, 2]
        app.ordenar_burbuja(original)
        assert original == [3, 1, 2]


class TestBusquedaBinaria:

    def test_numero_existe_inicio(self, app):
        assert app.busqueda_binaria([1, 2, 3, 4, 5], 1) != -1

    def test_numero_existe_fin(self, app):
        assert app.busqueda_binaria([1, 2, 3, 4, 5], 5) != -1

    def test_numero_existe_medio(self, app):
        assert app.busqueda_binaria([1, 2, 3, 4, 5], 3) == 2

    def test_numero_no_existe(self, app):
        assert app.busqueda_binaria([1, 2, 3, 4, 5], 99) == -1

    def test_lista_vacia(self, app):
        assert app.busqueda_binaria([], 5) == -1

    def test_lista_un_elemento_encontrado(self, app):
        assert app.busqueda_binaria([7], 7) == 0

    def test_lista_un_elemento_no_encontrado(self, app):
        assert app.busqueda_binaria([7], 1) == -1

    def test_numero_menor_que_minimo(self, app):
        assert app.busqueda_binaria([10, 20, 30], 5) == -1

    def test_numero_mayor_que_maximo(self, app):
        assert app.busqueda_binaria([10, 20, 30], 50) == -1

    def test_retorna_indice_correcto(self, app):
        assert app.busqueda_binaria([2, 4, 6, 8, 10], 6) == 2
