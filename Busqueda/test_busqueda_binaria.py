import unittest
from busqueda_binaria import bubble_sort, binary_search


class TestBubbleSort(unittest.TestCase):

    def test_lista_desordenada(self):
        self.assertEqual(bubble_sort([5, 3, 8, 1, 2]), [1, 2, 3, 5, 8])

    def test_lista_ya_ordenada(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_lista_orden_inverso(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_lista_un_elemento(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_lista_vacia(self):
        self.assertEqual(bubble_sort([]), [])

    def test_lista_con_duplicados(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_no_modifica_lista_ordenada(self):
        entrada = [10, 20, 30]
        resultado = bubble_sort(entrada)
        self.assertEqual(resultado, [10, 20, 30])


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 3, 5, 7, 9, 11, 13]

    def test_elemento_encontrado_medio(self):
        self.assertNotEqual(binary_search(self.arr, 7), -1)

    def test_elemento_encontrado_inicio(self):
        self.assertEqual(binary_search(self.arr, 1), 0)

    def test_elemento_encontrado_fin(self):
        self.assertEqual(binary_search(self.arr, 13), 6)

    def test_elemento_no_encontrado(self):
        self.assertEqual(binary_search(self.arr, 4), -1)

    def test_elemento_menor_que_minimo(self):
        self.assertEqual(binary_search(self.arr, 0), -1)

    def test_elemento_mayor_que_maximo(self):
        self.assertEqual(binary_search(self.arr, 100), -1)

    def test_lista_vacia(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_lista_un_elemento_encontrado(self):
        self.assertEqual(binary_search([42], 42), 0)

    def test_lista_un_elemento_no_encontrado(self):
        self.assertEqual(binary_search([42], 7), -1)

    def test_retorna_indice_correcto(self):
        self.assertEqual(binary_search(self.arr, 5), 2)


if __name__ == "__main__":
    unittest.main()
