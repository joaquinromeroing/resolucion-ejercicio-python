#!/usr/bin/env python3


import pytest
from algoritmo import ordenamiento_burbuja, busqueda_binaria



class TestOrdenamientoBurbuja:

    def test_lista_desordenada(self):
        """Ordena correctamente una lista sin orden previo."""
        resultado = ordenamiento_burbuja([5, 3, 8, 1, 9, 2])
        assert resultado == [1, 2, 3, 5, 8, 9]

    def test_lista_ya_ordenada(self):
        """No altera una lista que ya está ordenada."""
        resultado = ordenamiento_burbuja([1, 2, 3, 4, 5])
        assert resultado == [1, 2, 3, 4, 5]

    def test_lista_orden_inverso(self):
        """Ordena correctamente una lista en orden descendente."""
        resultado = ordenamiento_burbuja([10, 8, 6, 4, 2])
        assert resultado == [2, 4, 6, 8, 10]

    def test_lista_un_elemento(self):
        """Una lista de un solo elemento no cambia."""
        resultado = ordenamiento_burbuja([42])
        assert resultado == [42]

    def test_lista_vacia(self):
        """Una lista vacía retorna lista vacía."""
        resultado = ordenamiento_burbuja([])
        assert resultado == []

    def test_lista_con_duplicados(self):
        """Maneja correctamente elementos repetidos."""
        resultado = ordenamiento_burbuja([3, 1, 3, 2, 1])
        assert resultado == [1, 1, 2, 3, 3]

    def test_no_modifica_original(self):
        """La función no modifica la lista original."""
        original = [4, 2, 7, 1]
        ordenamiento_burbuja(original)
        assert original == [4, 2, 7, 1]

    def test_valores_extremos_rango(self):
        """Ordena correctamente con valores en los extremos del rango permitido (1 y 100000)."""
        resultado = ordenamiento_burbuja([100000, 1, 50000])
        assert resultado == [1, 50000, 100000]


class TestBusquedaBinaria:

    def test_elemento_existe_inicio(self):
        """Encuentra un elemento ubicado al inicio del arreglo."""
        assert busqueda_binaria([1, 3, 5, 7, 9], 1) == 0

    def test_elemento_existe_medio(self):
        """Encuentra un elemento ubicado en el medio del arreglo."""
        assert busqueda_binaria([1, 3, 5, 7, 9], 5) == 2

    def test_elemento_existe_final(self):
        """Encuentra un elemento ubicado al final del arreglo."""
        assert busqueda_binaria([1, 3, 5, 7, 9], 9) == 4

    def test_elemento_no_existe(self):
        """Retorna -1 cuando el elemento no está en el arreglo."""
        assert busqueda_binaria([1, 3, 5, 7, 9], 4) == -1

    def test_lista_vacia(self):
        """Retorna -1 al buscar en una lista vacía."""
        assert busqueda_binaria([], 5) == -1

    def test_lista_un_elemento_encontrado(self):
        """Encuentra el único elemento de una lista de un elemento."""
        assert busqueda_binaria([7], 7) == 0

    def test_lista_un_elemento_no_encontrado(self):
        """Retorna -1 cuando el único elemento no coincide."""
        assert busqueda_binaria([7], 3) == -1

    def test_elemento_menor_que_todos(self):
        """Retorna -1 cuando el objetivo es menor que todos los elementos."""
        assert busqueda_binaria([10, 20, 30, 40], 5) == -1

    def test_elemento_mayor_que_todos(self):
        """Retorna -1 cuando el objetivo es mayor que todos los elementos."""
        assert busqueda_binaria([10, 20, 30, 40], 99) == -1

    def test_valores_extremos_rango(self):
        """Busca correctamente valores en los extremos del rango permitido."""
        arreglo = [1, 50000, 100000]
        assert busqueda_binaria(arreglo, 1) == 0
        assert busqueda_binaria(arreglo, 100000) == 2
