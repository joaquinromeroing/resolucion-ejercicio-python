import pytest
from main import calcular_total, producto_mas_vendido

def test_calcular_total_sin_descuento():
    compras = [
        {"nombre": "Leche", "precio": 1200, "cantidad": 2},
        {"nombre": "Pan", "precio": 1500, "cantidad": 1}
    ]
    assert calcular_total(compras) == 3900


def test_calcular_total_con_descuento():
    compras = [
        {"nombre": "Fernet", "precio": 8000, "cantidad": 2}
    ]

    assert calcular_total(compras) == 14400


def test_producto_mas_vendido():
    compras = [
        {"nombre": "Yerba", "precio": 3000, "cantidad": 1},
        {"nombre": "Galletitas", "precio": 800, "cantidad": 5}
    ]
    assert producto_mas_vendido(compras) == "Galletitas"


def test_valores_negativos_lanzan_error():
    compras = [
        {"nombre": "Azúcar", "precio": -500, "cantidad": 1}
    ]
    with pytest.raises(ValueError):
        calcular_total(compras)


def test_lista_vacia_producto_mas_vendido():
    assert producto_mas_vendido([]) is None