import unittest

from main import burbuja, busqueda_binaria


class TestAlgoritmos(unittest.TestCase):

    def test_burbuja(self):

        datos = [5, 1, 4, 2]

        esperado = [1, 2, 4, 5]

        self.assertEqual(
            burbuja(datos),
            esperado
        )

    def test_busqueda_encontrado(self):

        datos = [1, 2, 3, 4, 5]

        self.assertTrue(
            busqueda_binaria(datos, 4)
        )

    def test_busqueda_no_encontrado(self):

        datos = [1, 2, 3, 4, 5]

        self.assertFalse(
            busqueda_binaria(datos, 8)
        )

    def test_burbuja_lista_vacia(self):

        datos = []

        esperado = []

        self.assertEqual(
            burbuja(datos),
            esperado
        )


if __name__ == "__main__":
    unittest.main()