import unittest
from main import burbuja, busqueda_binaria


class TestBurbuja(unittest.TestCase):

    def test_burbuja_lista_desordenada(self):
        numeros = [5, 3, 8, 1, 2]
        resultado = burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 3, 5, 8])

    def test_burbuja_lista_ordenada(self):
        numeros = [1, 2, 3, 4, 5]
        resultado = burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 3, 4, 5])

    def test_burbuja_con_repetidos(self):
        numeros = [4, 2, 4, 1, 2]
        resultado = burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 2, 4, 4])

    def test_burbuja_lista_vacia(self):
        numeros = []
        resultado = burbuja(numeros)
        self.assertEqual(resultado, [])


class TestBusquedaBinaria(unittest.TestCase):

    def test_busqueda_numero_encontrado(self):
        numeros = [1, 2, 3, 5, 8]
        resultado = busqueda_binaria(numeros, 5)
        self.assertTrue(resultado)

    def test_busqueda_numero_no_encontrado(self):
        numeros = [1, 2, 3, 5, 8]
        resultado = busqueda_binaria(numeros, 7)
        self.assertFalse(resultado)

    def test_busqueda_primer_elemento(self):
        numeros = [1, 2, 3, 5, 8]
        resultado = busqueda_binaria(numeros, 1)
        self.assertTrue(resultado)

    def test_busqueda_ultimo_elemento(self):
        numeros = [1, 2, 3, 5, 8]
        resultado = busqueda_binaria(numeros, 8)
        self.assertTrue(resultado)

    def test_busqueda_lista_vacia(self):
        numeros = []
        resultado = busqueda_binaria(numeros, 10)
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()