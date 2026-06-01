import unittest

from algoritmos import burbuja, busqueda_binaria


class TestBurbuja(unittest.TestCase):

    def test_ordena_lista_desordenada(self):
        self.assertEqual(burbuja([5, 2, 8, 1, 9, 3]), [1, 2, 3, 5, 8, 9])

    def test_lista_ya_ordenada(self):
        self.assertEqual(burbuja([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_lista_orden_inverso(self):
        self.assertEqual(burbuja([9, 7, 5, 3, 1]), [1, 3, 5, 7, 9])

    def test_lista_vacia(self):
        self.assertEqual(burbuja([]), [])

    def test_un_solo_elemento(self):
        self.assertEqual(burbuja([42]), [42])

    def test_con_duplicados(self):
        self.assertEqual(burbuja([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_no_muta_la_lista_original(self):
        original = [4, 2, 1, 3]
        burbuja(original)
        self.assertEqual(original, [4, 2, 1, 3])

    def test_limites_del_rango(self):
        self.assertEqual(burbuja([100000, 1, 50000]), [1, 50000, 100000])


class TestBusquedaBinaria(unittest.TestCase):

    def test_encuentra_elemento_existente(self):
        self.assertTrue(busqueda_binaria([1, 3, 5, 7, 9], 5))

    def test_encuentra_primer_elemento(self):
        self.assertTrue(busqueda_binaria([1, 3, 5, 7, 9], 1))

    def test_encuentra_ultimo_elemento(self):
        self.assertTrue(busqueda_binaria([1, 3, 5, 7, 9], 9))

    def test_no_encuentra_elemento_inexistente(self):
        self.assertFalse(busqueda_binaria([1, 3, 5, 7, 9], 4))

    def test_no_encuentra_menor_al_minimo(self):
        self.assertFalse(busqueda_binaria([10, 20, 30], 5))

    def test_no_encuentra_mayor_al_maximo(self):
        self.assertFalse(busqueda_binaria([10, 20, 30], 100))

    def test_lista_vacia(self):
        self.assertFalse(busqueda_binaria([], 7))

    def test_un_solo_elemento_encontrado(self):
        self.assertTrue(busqueda_binaria([42], 42))

    def test_un_solo_elemento_no_encontrado(self):
        self.assertFalse(busqueda_binaria([42], 41))

    def test_con_duplicados_encuentra(self):
        self.assertTrue(busqueda_binaria([1, 2, 2, 2, 3], 2))


class TestIntegracion(unittest.TestCase):

    def test_ordenar_y_buscar_existente(self):
        Numeros = burbuja([45, 2, 100000, 1, 78, 33])
        self.assertTrue(busqueda_binaria(Numeros, 78))

    def test_ordenar_y_buscar_inexistente(self):
        Numeros = burbuja([45, 2, 100000, 1, 78, 33])
        self.assertFalse(busqueda_binaria(Numeros, 99))


if __name__ == "__main__":
    unittest.main()
