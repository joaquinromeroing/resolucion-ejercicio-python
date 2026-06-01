import unittest
from busqueda_binaria import ordenamiento_burbuja, busqueda_binaria


class TestOrdenamientoBurbuja(unittest.TestCase):
    
    def test_arreglo_vacio(self):
        resultado = ordenamiento_burbuja([])
        self.assertEqual(resultado, [])
    
    def test_arreglo_un_elemento(self):
        resultado = ordenamiento_burbuja([5])
        self.assertEqual(resultado, [5])
    
    def test_arreglo_dos_elementos_ordenado(self):
        resultado = ordenamiento_burbuja([1, 2])
        self.assertEqual(resultado, [1, 2])
    
    def test_arreglo_dos_elementos_desordenado(self):
        resultado = ordenamiento_burbuja([2, 1])
        self.assertEqual(resultado, [1, 2])
    
    def test_arreglo_multiplo_desordenado(self):
        resultado = ordenamiento_burbuja([64, 34, 25, 12, 22, 11, 90])
        self.assertEqual(resultado, [11, 12, 22, 25, 34, 64, 90])
    
    def test_arreglo_con_duplicados(self):
        resultado = ordenamiento_burbuja([5, 2, 8, 2, 9, 1, 5])
        self.assertEqual(resultado, [1, 2, 2, 5, 5, 8, 9])
    
    def test_arreglo_numeros_negativos(self):
        resultado = ordenamiento_burbuja([3, -1, 4, -5, 2])
        self.assertEqual(resultado, [-5, -1, 2, 3, 4])
    
    def test_arreglo_numeros_negativos_y_positivos(self):
        resultado = ordenamiento_burbuja([-50, 100, 0, -25, 75, 10])
        self.assertEqual(resultado, [-50, -25, 0, 10, 75, 100])
    
    def test_arreglo_ya_ordenado(self):
        resultado = ordenamiento_burbuja([1, 2, 3, 4, 5])
        self.assertEqual(resultado, [1, 2, 3, 4, 5])
    
    def test_arreglo_orden_inverso(self):
        resultado = ordenamiento_burbuja([5, 4, 3, 2, 1])
        self.assertEqual(resultado, [1, 2, 3, 4, 5])
    
    def test_arreglo_numeros_grandes(self):
        resultado = ordenamiento_burbuja([99999, 1, 50000, 100000, 25000])
        self.assertEqual(resultado, [1, 25000, 50000, 99999, 100000])
    
    def test_no_modifica_arreglo_original(self):
        original = [3, 1, 4, 1, 5]
        ordenamiento_burbuja(original)
        self.assertEqual(original, [3, 1, 4, 1, 5])


class TestBusquedaBinaria(unittest.TestCase):
    
    def test_arreglo_vacio(self):
        resultado = busqueda_binaria([], 5)
        self.assertFalse(resultado)
    
    def test_elemento_unico_encontrado(self):
        resultado = busqueda_binaria([5], 5)
        self.assertTrue(resultado)
    
    def test_elemento_unico_no_encontrado(self):
        resultado = busqueda_binaria([5], 3)
        self.assertFalse(resultado)
    
    def test_elemento_al_inicio(self):
        resultado = busqueda_binaria([1, 2, 3, 4, 5], 1)
        self.assertTrue(resultado)
    
    def test_elemento_al_final(self):
        resultado = busqueda_binaria([1, 2, 3, 4, 5], 5)
        self.assertTrue(resultado)
    
    def test_elemento_al_medio(self):
        resultado = busqueda_binaria([1, 2, 3, 4, 5], 3)
        self.assertTrue(resultado)
    
    def test_elemento_no_existe(self):
        resultado = busqueda_binaria([1, 2, 3, 4, 5], 6)
        self.assertFalse(resultado)
    
    def test_elemento_menor_que_todos(self):
        resultado = busqueda_binaria([10, 20, 30, 40, 50], 5)
        self.assertFalse(resultado)
    
    def test_elemento_mayor_que_todos(self):
        resultado = busqueda_binaria([10, 20, 30, 40, 50], 60)
        self.assertFalse(resultado)
    
    def test_arreglo_grande(self):
        arreglo_grande = list(range(1, 1001))
        resultado = busqueda_binaria(arreglo_grande, 500)
        self.assertTrue(resultado)
    
    def test_arreglo_grande_elemento_no_existe(self):
        arreglo_grande = list(range(1, 1001, 2))
        resultado = busqueda_binaria(arreglo_grande, 1000)
        self.assertFalse(resultado)
    
    def test_con_numeros_rango_enunciado(self):
        arreglo = [100, 5000, 25000, 50000, 99999, 100000]
        resultado = busqueda_binaria(arreglo, 50000)
        self.assertTrue(resultado)
    
    def test_con_numeros_rango_enunciado_no_existe(self):
        arreglo = [100, 5000, 25000, 50000, 99999, 100000]
        resultado = busqueda_binaria(arreglo, 51000)
        self.assertFalse(resultado)
    
    def test_con_duplicados(self):
        arreglo = [1, 2, 2, 2, 3, 4, 5]
        resultado = busqueda_binaria(arreglo, 2)
        self.assertTrue(resultado)


class TestIntegracionOrdenamientoYBusqueda(unittest.TestCase):
    
    def test_flujo_completo_encontrado(self):
        numeros_desordenados = [64, 34, 25, 12, 22, 11, 90]
        numeros_ordenados = ordenamiento_burbuja(numeros_desordenados)
        resultado = busqueda_binaria(numeros_ordenados, 34)
        self.assertTrue(resultado)
    
    def test_flujo_completo_no_encontrado(self):
        numeros_desordenados = [64, 34, 25, 12, 22, 11, 90]
        numeros_ordenados = ordenamiento_burbuja(numeros_desordenados)
        resultado = busqueda_binaria(numeros_ordenados, 100)
        self.assertFalse(resultado)
    
    def test_con_secuencia_aleatoria_grande(self):
        numeros = [45678, 12345, 99999, 1, 50000, 25000, 100000, 87654, 11111, 55555]
        numeros_ordenados = ordenamiento_burbuja(numeros)
        self.assertEqual(numeros_ordenados, sorted(numeros))
        for numero in numeros:
            self.assertTrue(busqueda_binaria(numeros_ordenados, numero))
    
    def test_flujo_con_duplicados(self):
        numeros_desordenados = [5, 2, 8, 2, 9, 1, 5, 8]
        numeros_ordenados = ordenamiento_burbuja(numeros_desordenados)
        self.assertEqual(numeros_ordenados, [1, 2, 2, 5, 5, 8, 8, 9])
        self.assertTrue(busqueda_binaria(numeros_ordenados, 5))
        self.assertTrue(busqueda_binaria(numeros_ordenados, 8))


if __name__ == '__main__':
    unittest.main(verbosity=2)
