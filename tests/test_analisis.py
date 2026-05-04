import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from supermercado import calcular_importe, debe_intercambiar, ordenar_burbuja


def test_calcular_importe():
    assert calcular_importe(3, 100) == 300


def test_debe_intercambiar_por_sucursal():
    f1 = ["2", "A", "2024", "P1", "1", "100"]
    f2 = ["1", "A", "2024", "P1", "1", "100"]

    assert debe_intercambiar(f1, f2) == True


def test_no_debe_intercambiar():
    f1 = ["1", "A", "2024", "P1", "1", "100"]
    f2 = ["2", "A", "2024", "P1", "1", "100"]

    assert debe_intercambiar(f1, f2) == False


def test_ordenar_burbuja():
    filas = [
        ["2", "A", "2024", "P1", "1", "100"],
        ["1", "A", "2024", "P1", "1", "100"],
    ]

    resultado = ordenar_burbuja(filas)

    assert resultado[0][0] == "1"
    assert resultado[1][0] == "2"