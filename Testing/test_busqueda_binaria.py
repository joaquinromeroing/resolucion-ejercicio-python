import unittest
from busqueda_binaria import AlgoritmosOrdenamiento, AlgoritmosBusqueda


class TestBurbuja(unittest.TestCase):
    """Unit Tests para el ordenamiento Burbuja"""
    
    def setUp(self):
        self.ordenador = AlgoritmosOrdenamiento()
    
    def test_burbuja_numeros_desordenados(self):
        """Prueba burbuja con números desordenados"""
        entrada = [64, 34, 25, 12, 22, 11, 90]
        esperado = [11, 12, 22, 25, 34, 64, 90]
        resultado = self.ordenador.burbuja(entrada)
        self.assertEqual(resultado, esperado)
    
    def test_burbuja_numeros_ya_ordenados(self):
        """Prueba burbuja con números ya ordenados"""
        entrada = [1, 2, 3, 4, 5]
        esperado = [1, 2, 3, 4, 5]
        resultado = self.ordenador.burbuja(entrada)
        self.assertEqual(resultado, esperado)
    
    def test_burbuja_numeros_inversos(self):
        """Prueba burbuja con números en orden inverso"""
        entrada = [5, 4, 3, 2, 1]
        esperado = [1, 2, 3, 4, 5]
        resultado = self.ordenador.burbuja(entrada)
        self.assertEqual(resultado, esperado)
    
    def test_burbuja_un_elemento(self):
        """Prueba burbuja con un solo elemento"""
        entrada = [42]
        esperado = [42]
        resultado = self.ordenador.burbuja(entrada)
        self.assertEqual(resultado, esperado)
    
    def test_burbuja_dos_elementos(self):
        """Prueba burbuja con dos elementos"""
        entrada = [2, 1]
        esperado = [1, 2]
        resultado = self.ordenador.burbuja(entrada)
        self.assertEqual(resultado, esperado)
    
    def test_burbuja_numeros_duplicados(self):
        """Prueba burbuja con números duplicados"""
        entrada = [3, 1, 3, 1, 2]
        esperado = [1, 1, 2, 3, 3]
        resultado = self.ordenador.burbuja(entrada)
        self.assertEqual(resultado, esperado)
    
    def test_burbuja_numeros_negativos(self):
        """Prueba burbuja con números negativos"""
        entrada = [3, -1, 4, -5, 2]
        esperado = [-5, -1, 2, 3, 4]
        resultado = self.ordenador.burbuja(entrada)
        self.assertEqual(resultado, esperado)


class TestBusquedaBinaria(unittest.TestCase):
    """Unit Tests para la Búsqueda Binaria"""
    
    def setUp(self):
        self.buscador = AlgoritmosBusqueda()
        self.numeros = [11, 12, 22, 25, 34, 64, 90]
    
    def test_busqueda_numero_encontrado_inicio(self):
        """Prueba búsqueda encontrando número al inicio"""
        resultado = self.buscador.busqueda_binaria(self.numeros, 11)
        self.assertNotEqual(resultado, -1)
    
    def test_busqueda_numero_encontrado_final(self):
        """Prueba búsqueda encontrando número al final"""
        resultado = self.buscador.busqueda_binaria(self.numeros, 90)
        self.assertNotEqual(resultado, -1)
    
    def test_busqueda_numero_encontrado_medio(self):
        """Prueba búsqueda encontrando número en el medio"""
        resultado = self.buscador.busqueda_binaria(self.numeros, 25)
        self.assertEqual(resultado, 3)
    
    def test_busqueda_numero_no_encontrado(self):
        """Prueba búsqueda cuando número no existe"""
        resultado = self.buscador.busqueda_binaria(self.numeros, 50)
        self.assertEqual(resultado, -1)
    
    def test_busqueda_numero_menor_que_todos(self):
        """Prueba búsqueda con número menor que el menor del arreglo"""
        resultado = self.buscador.busqueda_binaria(self.numeros, 5)
        self.assertEqual(resultado, -1)
    
    def test_busqueda_numero_mayor_que_todos(self):
        """Prueba búsqueda con número mayor que el mayor del arreglo"""
        resultado = self.buscador.busqueda_binaria(self.numeros, 100)
        self.assertEqual(resultado, -1)
    
    def test_busqueda_un_elemento_encontrado(self):
        """Prueba búsqueda en arreglo con un solo elemento (encontrado)"""
        resultado = self.buscador.busqueda_binaria([42], 42)
        self.assertEqual(resultado, 0)
    
    def test_busqueda_un_elemento_no_encontrado(self):
        """Prueba búsqueda en arreglo con un solo elemento (no encontrado)"""
        resultado = self.buscador.busqueda_binaria([42], 10)
        self.assertEqual(resultado, -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
