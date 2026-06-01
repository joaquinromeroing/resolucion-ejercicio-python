import unittest
from busqued import burbuja, busqueda_binaria

class TestBurbuja(unittest.TestCase):

    def test_ordena_lista(self):

        lista = [5, 2, 8, 1]

        resultado = burbuja(lista)

        self.assertEqual(resultado, [1, 2, 5, 8])


class TestBusquedaBinaria(unittest.TestCase):

    def test_numero_encontrado(self):

        lista = [1, 2, 3, 4, 5]

        self.assertTrue(
            busqueda_binaria(lista, 3)
        )


    def test_numero_no_encontrado(self):

        lista = [1, 2, 3, 4, 5]

        self.assertFalse(
            busqueda_binaria(lista, 10)
        )


if __name__ == "__main__":
    unittest.main()


def test_lista_vacia(self):
    self.assertEqual(burbuja([]), [])


def test_un_elemento(self):
    self.assertEqual(burbuja([7]), [7])