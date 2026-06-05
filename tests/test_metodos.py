import unittest
import sys
import os

# Esto asegura que Python pueda encontrar la carpeta 'src' desde la carpeta 'tests'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.metodos import ordenamiento_burbuja, busqueda_binaria


class TestMetodos(unittest.TestCase):

    # ----------------------------------------------------
    # PRUEBAS PARA EL ORDENAMIENTO BURBUJA
    # ----------------------------------------------------
    
    def test_ordenamiento_burbuja_desordenado(self):
        """Prueba que un arreglo completamente desordenado se ordene correctamente."""
        lista = [5, 3, 8, 1, 2]
        ordenamiento_burbuja(lista)
        self.assertEqual(lista, [1, 2, 3, 5, 8])

    def test_ordenamiento_burbuja_ya_ordenado(self):
        """Prueba que un arreglo que ya está ordenado mantenga su orden."""
        lista = [10, 20, 30, 40]
        ordenamiento_burbuja(lista)
        self.assertEqual(lista, [10, 20, 30, 40])

    def test_ordenamiento_burbuja_vacio(self):
        """Prueba que el algoritmo no falle si el arreglo está vacío."""
        lista = []
        ordenamiento_burbuja(lista)
        self.assertEqual(lista, [])


    # ----------------------------------------------------
    # PRUEBAS PARA LA BÚSQUEDA BINARIA
    # ----------------------------------------------------
    
    def test_busqueda_binaria_elemento_existente(self):
        """Prueba que encuentre un número que sí está en el arreglo."""
        lista_ordenada = [1, 5, 8, 12, 20, 50]
        # Buscamos el 12, debería retornar True
        resultado = busqueda_binaria(lista_ordenada, 12)
        self.assertTrue(resultado)

    def test_busqueda_binaria_elemento_inexistente(self):
        """Prueba que devuelva False si el número no está en el arreglo."""
        lista_ordenada = [1, 5, 8, 12, 20, 50]
        # Buscamos el 7 (no está), debería retornar False
        resultado = busqueda_binaria(lista_ordenada, 7)
        self.assertFalse(resultado)

    def test_busqueda_binaria_limites(self):
        """Prueba la búsqueda en los extremos (primer y último elemento)."""
        lista_ordenada = [1, 5, 8, 12, 20, 50]
        # Primer elemento
        self.assertTrue(busqueda_binaria(lista_ordenada, 1))
        # Último elemento
        self.assertTrue(busqueda_binaria(lista_ordenada, 50))


if __name__ == '__main__':
    unittest.main()
