import unittest
from busqueda_binaria import burbuja, busqueda_binaria


class TestBurbuja(unittest.TestCase):

    def test_lista_desordenada(self):
        """Ordena correctamente una lista con valores aleatorios."""
        self.assertEqual(burbuja([5, 3, 8, 1, 9, 2]), [1, 2, 3, 5, 8, 9])

    def test_lista_ya_ordenada(self):
        """No altera una lista que ya está ordenada."""
        self.assertEqual(burbuja([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_lista_orden_inverso(self):
        """Ordena correctamente una lista en orden descendente."""
        self.assertEqual(burbuja([9, 7, 5, 3, 1]), [1, 3, 5, 7, 9])

    def test_lista_un_elemento(self):
        """Una lista de un solo elemento no cambia."""
        self.assertEqual(burbuja([42]), [42])

    def test_lista_vacia(self):
        """Una lista vacía devuelve otra lista vacía."""
        self.assertEqual(burbuja([]), [])

    def test_lista_con_duplicados(self):
        """Ordena correctamente cuando hay valores repetidos."""
        self.assertEqual(burbuja([4, 2, 4, 1, 2]), [1, 2, 2, 4, 4])

    def test_no_modifica_original(self):
        """La función no debe mutar la lista original."""
        original = [3, 1, 2]
        _ = burbuja(original)
        self.assertEqual(original, [3, 1, 2])

    def test_valores_en_rango_permitido(self):
        """Ordena valores dentro del rango 1–100000."""
        datos = [100000, 1, 50000, 25000]
        self.assertEqual(burbuja(datos), [1, 25000, 50000, 100000])

class TestBusquedaBinaria(unittest.TestCase):

    def setUp(self):
        """Arreglo ordenado reutilizado en varios tests."""
        self.arr = [1, 3, 5, 7, 9, 11, 15, 20]

    def test_elemento_encontrado_inicio(self):
        """Encuentra el primer elemento del arreglo."""
        self.assertEqual(busqueda_binaria(self.arr, 1), 0)

    def test_elemento_encontrado_fin(self):
        """Encuentra el último elemento del arreglo."""
        self.assertEqual(busqueda_binaria(self.arr, 20), 7)

    def test_elemento_encontrado_medio(self):
        """Encuentra un elemento en el medio del arreglo."""
        indice = busqueda_binaria(self.arr, 9)
        self.assertEqual(self.arr[indice], 9)

    def test_elemento_no_encontrado(self):
        """Retorna -1 para un valor que no existe."""
        self.assertEqual(busqueda_binaria(self.arr, 6), -1)

    def test_elemento_no_encontrado_menor_al_minimo(self):
        """Retorna -1 si el objetivo es menor que todos los elementos."""
        self.assertEqual(busqueda_binaria(self.arr, 0), -1)

    def test_elemento_no_encontrado_mayor_al_maximo(self):
        """Retorna -1 si el objetivo es mayor que todos los elementos."""
        self.assertEqual(busqueda_binaria(self.arr, 999), -1)

    def test_lista_vacia(self):
        """Retorna -1 en una lista vacía."""
        self.assertEqual(busqueda_binaria([], 5), -1)

    def test_lista_un_elemento_encontrado(self):
        """Encuentra el único elemento de la lista."""
        self.assertEqual(busqueda_binaria([7], 7), 0)

    def test_lista_un_elemento_no_encontrado(self):
        """Retorna -1 cuando el único elemento no coincide."""
        self.assertEqual(busqueda_binaria([7], 3), -1)

    def test_elemento_encontrado_retorna_indice_correcto(self):
        """El índice retornado apunta al valor correcto en el arreglo."""
        objetivo = 11
        indice = busqueda_binaria(self.arr, objetivo)
        self.assertNotEqual(indice, -1)
        self.assertEqual(self.arr[indice], objetivo)

    def test_con_duplicados_retorna_un_indice_valido(self):
        """Con duplicados, retorna algún índice válido del elemento."""
        arr_dup = [1, 2, 2, 2, 3]
        indice = busqueda_binaria(arr_dup, 2)
        self.assertNotEqual(indice, -1)
        self.assertEqual(arr_dup[indice], 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)