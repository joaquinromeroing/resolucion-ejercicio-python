import pytest
from app.principal import calcular_importe, debe_intercambiar, algoritmo_burbuja


def test_calcular_importe():
    assert calcular_importe(3, 100) == 300


def test_debe_intercambiar_por_sucursal():
    r1 = {'PRSUC': 'Sucursal 2'}
    r2 = {'PRSUC': 'Sucursal 1'}

    assert debe_intercambiar(r1, r2) == True


def test_no_debe_intercambiar():
    r1 = {'PRSUC': 'Sucursal 1'}
    r2 = {'PRSUC': 'Sucursal 2'}

    assert debe_intercambiar(r1, r2) == False


def test_algoritmo_burbuja_funciona():
    registros = [
        {'PRSUC': 'B'},
        {'PRSUC': 'A'}
    ]
    resultado = algoritmo_burbuja(registros)

    assert resultado[0]['PRSUC'] == 'A'