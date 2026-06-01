import unittest
from busqueda import validate_input, dicotomic_search, bubble_sort


class TestValidateInput(unittest.TestCase):
    def test_numero_valido(self):
        self.assertEqual(validate_input("50"), 50)

    def test_limite_inferior(self):
        self.assertEqual(validate_input("1"), 1)

    def test_limite_superior(self):
        self.assertEqual(validate_input("100000"), 100000)

    def test_fuera_de_rango_superior(self):
        self.assertIsNone(validate_input("100001"))

    def test_fuera_de_rango_inferior(self):
        self.assertIsNone(validate_input("0"))

    def test_texto(self):
        self.assertIsNone(validate_input("abc"))

    def test_string_vacio(self):
        self.assertIsNone(validate_input(""))

    def test_numero_negativo(self):
        self.assertIsNone(validate_input("-5"))


class TestDicotomicSearch(unittest.TestCase):
    def test_encontrado_al_medio(self):
        self.assertEqual(dicotomic_search([1, 3, 5, 7, 9], 5), 2)

    def test_encontrado_al_inicio(self):
        self.assertEqual(dicotomic_search([1, 3, 5, 7, 9], 1), 0)

    def test_encontrado_al_final(self):
        self.assertEqual(dicotomic_search([1, 3, 5, 7, 9], 9), 4)

    def test_no_encontrado(self):
        self.assertEqual(dicotomic_search([1, 3, 5, 7, 9], 4), -1)

    def test_arreglo_vacio(self):
        self.assertEqual(dicotomic_search([], 5), -1)

    def test_un_elemento_encontrado(self):
        self.assertEqual(dicotomic_search([7], 7), 0)

    def test_un_elemento_no_encontrado(self):
        self.assertEqual(dicotomic_search([7], 3), -1)


class TestBubbleSort(unittest.TestCase):
    def test_ordenar_desordenado(self):
        arr = [3, 1, 2]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_ya_ordenado(self):
        arr = [1, 2, 3]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_orden_inverso(self):
        arr = [5, 4, 3, 2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_un_elemento(self):
        arr = [42]
        bubble_sort(arr)
        self.assertEqual(arr, [42])

    def test_arreglo_vacio(self):
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

    def test_duplicados(self):
        arr = [3, 1, 2, 1, 3]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
