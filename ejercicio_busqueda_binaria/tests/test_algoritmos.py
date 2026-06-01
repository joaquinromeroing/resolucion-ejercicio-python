import unittest

from ejercicio_busqueda_binaria.algoritmos import ordenar_burbuja, busqueda_binaria


class TestAlgoritmos(unittest.TestCase):

    def test_ordenar_burbuja_lista_desordenada(self):
        numeros = [5, 2, 9, 1, 3]
        resultado = ordenar_burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 3, 5, 9])

    def test_ordenar_burbuja_lista_ordenada(self):
        numeros = [1, 2, 3, 4, 5]
        resultado = ordenar_burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 3, 4, 5])

    def test_ordenar_burbuja_con_repetidos(self):
        numeros = [4, 2, 4, 1, 2]
        resultado = ordenar_burbuja(numeros)
        self.assertEqual(resultado, [1, 2, 2, 4, 4])

    def test_busqueda_binaria_numero_encontrado(self):
        numeros = [1, 2, 3, 5, 9]
        resultado = busqueda_binaria(numeros, 5)
        self.assertTrue(resultado)

    def test_busqueda_binaria_numero_no_encontrado(self):
        numeros = [1, 2, 3, 5, 9]
        resultado = busqueda_binaria(numeros, 7)
        self.assertFalse(resultado)

    def test_busqueda_binaria_lista_vacia(self):
        numeros = []
        resultado = busqueda_binaria(numeros, 10)
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()