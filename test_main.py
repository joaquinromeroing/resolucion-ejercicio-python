import unittest
from main import (
    validar_monto_positivo, 
    calcular_subtotal, 
    funcion_burbuja, 
    procesar_corte_control
)

class TestSistemaSupermercado(unittest.TestCase):

    # --- 1. Test de Validación (Caso TRUE) ---
    def test_validar_monto_positivo_exito(self):
        """Verifica que montos mayores a cero sean aceptados."""
        self.assertTrue(validar_monto_positivo(1500.50))

    # --- 2. Test de Validación (Caso FALSE) ---
    def test_validar_monto_negativo_error(self):
        """Verifica que montos menores o iguales a cero sean rechazados."""
        self.assertFalse(validar_monto_positivo(-50))
        self.assertFalse(validar_monto_positivo(0))

    # --- 3. Test de Cálculo Matemático ---
    def test_calculo_subtotal_exacto(self):
        """Verifica que la multiplicación de cantidad y precio sea correcta."""
        # 3 unidades a $10.50 = $31.50
        self.assertEqual(calcular_subtotal(3, 10.5), 31.5)

    # --- 4. Test de Ordenamiento (Burbuja) ---
    def test_ordenamiento_burbuja_manual(self):
        """Verifica que la burbuja ordene por Sucursal y luego por Producto."""
        datos_desordenados = [
            ["SUC02", "P500"],
            ["SUC01", "P100"],
            ["SUC02", "P100"]
        ]
        resultado = funcion_burbuja(datos_desordenados)
        # El orden esperado es SUC01-P100, SUC02-P100, SUC02-P500
        self.assertEqual(resultado[0][0], "SUC01")
        self.assertEqual(resultado[1][1], "P100")
        self.assertEqual(resultado[2][1], "P500")

    # --- 5. Test de Corte de Control (Acumuladores) ---
    def test_corte_control_sumatoria_pesos(self):
        """Verifica que el acumulador de los 'while' sume bien los totales[cite: 1]."""
        datos_mock = [
            ["SUC01", "P1", "f", "h", "2", "100"], # 200 pesos
            ["SUC01", "P1", "f", "h", "1", "50"]   # 50 pesos
        ]
        resultado = procesar_corte_control(datos_mock)
        self.assertEqual(resultado["SUC01"]["total"], 250.0)

    # --- 6. Test de Lógica de Mayor Producto (Máximos) ---
    def test_corte_control_producto_lider(self):
        """Verifica que identifique correctamente qué producto recaudó más en la sucursal[cite: 1]."""
        datos_mock = [
            ["SUC01", "P_BARATO", "f", "h", "1", "10"],
            ["SUC01", "P_CARO", "f", "h", "1", "1000"]
        ]
        resultado = procesar_corte_control(datos_mock)
        self.assertEqual(resultado["SUC01"]["max_p"], "P_CARO")
        self.assertEqual(resultado["SUC01"]["total"], 1010.0)

if __name__ == "__main__":
    unittest.main()