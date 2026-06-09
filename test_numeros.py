import unittest
from numeros import burbuja, busqueda_binaria


class TestBurbuja(unittest.TestCase):

    def test_lista_desordenada(self):
        self.assertEqual(burbuja([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_lista_ya_ordenada(self):
        self.assertEqual(burbuja([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_lista_orden_inverso(self):
        self.assertEqual(burbuja([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_un_elemento(self):
        self.assertEqual(burbuja([42]), [42])

    def test_elementos_repetidos(self):
        self.assertEqual(burbuja([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])

    def test_lista_vacia(self):
        self.assertEqual(burbuja([]), [])

    def test_modifica_lista_original(self):
        arr = [3, 1, 2]
        resultado = burbuja(arr)
        self.assertEqual(arr, [1, 2, 3])
        self.assertIs(resultado, arr)


class TestBusquedaBinaria(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 3, 5, 7, 9, 11, 13, 15]

    def test_numero_presente_inicio(self):
        self.assertEqual(busqueda_binaria(self.arr, 1), 0)

    def test_numero_presente_fin(self):
        self.assertEqual(busqueda_binaria(self.arr, 15), 7)

    def test_numero_presente_medio(self):
        indice = busqueda_binaria(self.arr, 7)
        self.assertNotEqual(indice, -1)
        self.assertEqual(self.arr[indice], 7)

    def test_numero_ausente(self):
        self.assertEqual(busqueda_binaria(self.arr, 6), -1)

    def test_numero_menor_al_minimo(self):
        self.assertEqual(busqueda_binaria(self.arr, 0), -1)

    def test_numero_mayor_al_maximo(self):
        self.assertEqual(busqueda_binaria(self.arr, 100), -1)

    def test_lista_vacia(self):
        self.assertEqual(busqueda_binaria([], 5), -1)

    def test_lista_un_elemento_encontrado(self):
        self.assertEqual(busqueda_binaria([42], 42), 0)

    def test_lista_un_elemento_no_encontrado(self):
        self.assertEqual(busqueda_binaria([42], 7), -1)

    def test_retorna_indice_correcto(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(busqueda_binaria(arr, 30), 2)
        self.assertEqual(busqueda_binaria(arr, 10), 0)
        self.assertEqual(busqueda_binaria(arr, 50), 4)


if __name__ == "__main__":
    unittest.main()
