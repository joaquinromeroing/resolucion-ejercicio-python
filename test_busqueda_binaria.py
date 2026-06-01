import unittest

from busqueda_binaria import ordenar_burbuja, busqueda_binaria


class TestOrdenamientoBusqueda(unittest.TestCase):

    def test_ordenar_burbuja_lista_desordenada(self):
        numeros = [5, 1, 4, 2, 8]
        resultado = ordenar_burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 4, 5, 8])

    def test_ordenar_burbuja_lista_ya_ordenada(self):
        numeros = [1, 2, 3, 4, 5]
        resultado = ordenar_burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 3, 4, 5])

    def test_ordenar_burbuja_con_repetidos(self):
        numeros = [3, 1, 2, 3, 1]
        resultado = ordenar_burbuja(numeros)
        self.assertEqual(resultado, [1, 1, 2, 3, 3])

    def test_busqueda_binaria_numero_existente(self):
        numeros = [1, 2, 4, 5, 8]
        resultado = busqueda_binaria(numeros, 4)
        self.assertTrue(resultado)

    def test_busqueda_binaria_numero_no_existente(self):
        numeros = [1, 2, 4, 5, 8]
        resultado = busqueda_binaria(numeros, 7)
        self.assertFalse(resultado)

    def test_busqueda_binaria_lista_vacia(self):
        numeros = []
        resultado = busqueda_binaria(numeros, 10)
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()