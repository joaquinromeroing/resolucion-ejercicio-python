import unittest
from unittest.mock import patch, call
from busqueda_binaria import cargar_numeros, ordenar_burbuja, busqueda_binaria
 
 
class TestOrdenarBurbuja(unittest.TestCase):
 
    def test_lista_desordenada(self):
        self.assertEqual(ordenar_burbuja([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])
 
    def test_lista_ya_ordenada(self):
        self.assertEqual(ordenar_burbuja([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
 
    def test_lista_orden_inverso(self):
        self.assertEqual(ordenar_burbuja([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
 
    def test_lista_un_elemento(self):
        self.assertEqual(ordenar_burbuja([42]), [42])
 
    def test_lista_vacia(self):
        self.assertEqual(ordenar_burbuja([]), [])
 
    def test_lista_con_duplicados(self):
        self.assertEqual(ordenar_burbuja([3, 3, 1, 2, 2]), [1, 2, 2, 3, 3])
 
    def test_no_modifica_original(self):
        original = [5, 2, 8]
        ordenar_burbuja(original)
        self.assertEqual(original, [5, 2, 8])
 
    def test_valores_extremos_del_rango(self):
        self.assertEqual(ordenar_burbuja([100000, 1]), [1, 100000])
 
 
class TestBusquedaBinaria(unittest.TestCase):
 
    def setUp(self):
        self.arr = [1, 3, 5, 7, 9, 11, 13, 15]
 
    def test_elemento_existe_al_inicio(self):
        self.assertEqual(busqueda_binaria(self.arr, 1), 0)
 
    def test_elemento_existe_al_final(self):
        self.assertEqual(busqueda_binaria(self.arr, 15), 7)
 
    def test_elemento_existe_al_medio(self):
        self.assertNotEqual(busqueda_binaria(self.arr, 7), -1)
 
    def test_elemento_no_existe(self):
        self.assertEqual(busqueda_binaria(self.arr, 4), -1)
 
    def test_lista_vacia(self):
        self.assertEqual(busqueda_binaria([], 5), -1)
 
    def test_lista_un_elemento_encontrado(self):
        self.assertEqual(busqueda_binaria([42], 42), 0)
 
    def test_lista_un_elemento_no_encontrado(self):
        self.assertEqual(busqueda_binaria([42], 10), -1)
 
    def test_elemento_mayor_que_todos(self):
        self.assertEqual(busqueda_binaria(self.arr, 99), -1)
 
    def test_elemento_menor_que_todos(self):
        self.assertEqual(busqueda_binaria(self.arr, 0), -1)
 
    def test_retorna_indice_correcto(self):
        # El 9 está en el índice 4
        self.assertEqual(busqueda_binaria(self.arr, 9), 4)
 
 
class TestCargarNumeros(unittest.TestCase):
 
    @patch('builtins.input', side_effect=['10', '50', '0'])
    def test_carga_numeros_validos(self, mock_input):
        resultado = cargar_numeros()
        self.assertEqual(resultado, [10, 50])
 
    @patch('builtins.input', side_effect=['0'])
    def test_termina_con_cero_sin_cargar_nada(self, mock_input):
        resultado = cargar_numeros()
        self.assertEqual(resultado, [])
 
    @patch('builtins.input', side_effect=['100000', '1', '0'])
    def test_acepta_valores_en_los_limites(self, mock_input):
        resultado = cargar_numeros()
        self.assertEqual(resultado, [100000, 1])
 
    @patch('builtins.input', side_effect=['-5', '50', '0'])
    def test_rechaza_numero_fuera_de_rango_negativo(self, mock_input):
        resultado = cargar_numeros()
        # -5 se descarta, solo queda 50
        self.assertEqual(resultado, [50])
 
    @patch('builtins.input', side_effect=['100001', '50', '0'])
    def test_rechaza_numero_mayor_al_rango(self, mock_input):
        resultado = cargar_numeros()
        self.assertEqual(resultado, [50])
 
    @patch('builtins.input', side_effect=['abc', '25', '0'])
    def test_rechaza_entrada_no_numerica(self, mock_input):
        resultado = cargar_numeros()
        self.assertEqual(resultado, [25])
 
 
if __name__ == '__main__':
    unittest.main(verbosity=2)