import unittest
from busqueda_binaria import burbuja, busqueda_binaria


class TestBurbuja(unittest.TestCase):

    def test_ordenamiento_basico(self):
        self.assertEqual(burbuja([3, 1, 2]), [1, 2, 3])

    def test_ya_ordenado(self):
        self.assertEqual(burbuja([1, 2, 3]), [1, 2, 3])

    def test_orden_inverso(self):
        self.assertEqual(burbuja([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_un_elemento(self):
        self.assertEqual(burbuja([42]), [42])

    def test_elementos_repetidos(self):
        self.assertEqual(burbuja([3, 3, 1, 2]), [1, 2, 3, 3])


class TestBusquedaBinaria(unittest.TestCase):

    def test_numero_encontrado(self):
        self.assertNotEqual(busqueda_binaria([1, 2, 3, 4, 5], 3), -1)

    def test_numero_no_encontrado(self):
        self.assertEqual(busqueda_binaria([1, 2, 3, 4, 5], 99), -1)

    def test_primer_elemento(self):
        self.assertNotEqual(busqueda_binaria([1, 2, 3, 4, 5], 1), -1)

    def test_ultimo_elemento(self):
        self.assertNotEqual(busqueda_binaria([1, 2, 3, 4, 5], 5), -1)

    def test_arreglo_un_elemento_encontrado(self):
        self.assertNotEqual(busqueda_binaria([7], 7), -1)

    def test_arreglo_un_elemento_no_encontrado(self):
        self.assertEqual(busqueda_binaria([7], 99), -1)


if __name__ == "__main__":
    unittest.main()