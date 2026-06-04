import unittest
from eje import ordenar_burbuja, busqueda_binaria

class TestAlgoritmos(unittest.TestCase):

    def test_burbuja_desordenada(self):
        self.assertEqual(ordenar_burbuja([5, 3, 8, 1]), [1, 3, 5, 8])

    def test_burbuja_ordenada(self):
        self.assertEqual(ordenar_burbuja([10, 20]), [10, 20])

    def test_burbuja_vacia(self):
        self.assertEqual(ordenar_burbuja([]), [])

    def test_binaria_encuentra(self):
        self.assertTrue(busqueda_binaria([1, 4, 7, 9], 7))

    def test_binaria_no_encuentra(self):
        self.assertFalse(busqueda_binaria([1, 4, 7, 9], 10))

    def test_binaria_lista_vacia(self):
        self.assertFalse(busqueda_binaria([], 5))

if __name__ == '__main__':
    unittest.main()