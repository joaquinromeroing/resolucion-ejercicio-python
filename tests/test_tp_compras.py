import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tp_compras import ordenar_burbuja, calcular_importe


def test_calcular_importe():
    resultado = calcular_importe(10, 25.5)
    assert resultado == 255.0


def test_ordenar_burbuja_por_sucursal():
    lista = [
        {"PRSUC": "SUC03", "PRCOD": "P100"},
        {"PRSUC": "SUC01", "PRCOD": "P200"},
        {"PRSUC": "SUC02", "PRCOD": "P300"},
    ]

    resultado = ordenar_burbuja(lista)

    assert resultado[0]["PRSUC"] == "SUC01"
    assert resultado[1]["PRSUC"] == "SUC02"
    assert resultado[2]["PRSUC"] == "SUC03"


def test_ordenar_burbuja_lista_ya_ordenada():
    lista = [
        {"PRSUC": "SUC01", "PRCOD": "P100"},
        {"PRSUC": "SUC02", "PRCOD": "P200"},
        {"PRSUC": "SUC03", "PRCOD": "P300"},
    ]

    resultado = ordenar_burbuja(lista)

    assert resultado[0]["PRSUC"] == "SUC01"
    assert resultado[1]["PRSUC"] == "SUC02"
    assert resultado[2]["PRSUC"] == "SUC03"