import unittest
from busqueda_binaria import ordenar_burbuja, busqueda_binaria


class TestOrdenarBurbuja(unittest.TestCase):

    def test_lista_desordenada(self):
        resultado = ordenar_burbuja([5, 2, 8, 1, 9])
        self.assertEqual(resultado, [1, 2, 5, 8, 9])

    def test_lista_ya_ordenada(self):
        resultado = ordenar_burbuja([1, 2, 3, 4, 5])
        self.assertEqual(resultado, [1, 2, 3, 4, 5])

    def test_lista_ordenada_inversa(self):
        resultado = ordenar_burbuja([9, 7, 5, 3, 1])
        self.assertEqual(resultado, [1, 3, 5, 7, 9])

    def test_lista_con_un_elemento(self):
        resultado = ordenar_burbuja([42])
        self.assertEqual(resultado, [42])

    def test_lista_vacia(self):
        resultado = ordenar_burbuja([])
        self.assertEqual(resultado, [])

    def test_lista_con_duplicados(self):
        resultado = ordenar_burbuja([3, 1, 3, 2, 1])
        self.assertEqual(resultado, [1, 1, 2, 3, 3])

    def test_no_modifica_lista_original(self):
        original = [3, 1, 2]
        ordenar_burbuja(original)
        self.assertEqual(original, [3, 1, 2])


class TestBusquedaBinaria(unittest.TestCase):

    def setUp(self):
        self.numeros = [1, 5, 10, 20, 35, 50, 75, 100]

    def test_numero_en_el_medio(self):
        self.assertTrue(busqueda_binaria(self.numeros, 20))

    def test_numero_al_inicio(self):
        self.assertTrue(busqueda_binaria(self.numeros, 1))

    def test_numero_al_final(self):
        self.assertTrue(busqueda_binaria(self.numeros, 100))

    def test_numero_no_existe(self):
        self.assertFalse(busqueda_binaria(self.numeros, 99))

    def test_lista_vacia(self):
        self.assertFalse(busqueda_binaria([], 5))

    def test_lista_con_un_elemento_encontrado(self):
        self.assertTrue(busqueda_binaria([7], 7))

    def test_lista_con_un_elemento_no_encontrado(self):
        self.assertFalse(busqueda_binaria([7], 3))

    def test_numero_fuera_de_rango_inferior(self):
        self.assertFalse(busqueda_binaria(self.numeros, 0))

    def test_numero_fuera_de_rango_superior(self):
        self.assertFalse(busqueda_binaria(self.numeros, 200))


if __name__ == "__main__":
    unittest.main()
