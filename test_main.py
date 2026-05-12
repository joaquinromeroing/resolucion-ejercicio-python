import csv
import os
import tempfile
import pytest
from main import ordenar_por_sucursal, procesar_estadisticas

def crear_csv_temporal(filas):
    tmp = tempfile.NamedTemporaryFile(
        mode='w', suffix='.csv', delete=False, encoding='utf-8', newline=''
    )
    escritor = csv.DictWriter(tmp, fieldnames=['PRSUC', 'PRCOD', 'PRCANT', 'PRPRE'])
    escritor.writeheader()
    escritor.writerows(filas)
    tmp.close()
    return tmp.name

def test_ordenar_ordena_por_sucursal():
    filas = [
        {'PRSUC': 'SUC03', 'PRCOD': 'P001', 'PRCANT': '1', 'PRPRE': '5.00'},
        {'PRSUC': 'SUC01', 'PRCOD': 'P002', 'PRCANT': '2', 'PRPRE': '10.00'},
        {'PRSUC': 'SUC02', 'PRCOD': 'P003', 'PRCANT': '3', 'PRPRE': '15.00'},
    ]
    entrada = crear_csv_temporal(filas)
    salida  = entrada + '_sorted.csv'

    try:
        ordenar_por_sucursal(entrada, salida)

        with open(salida, encoding='utf-8') as f:
            resultado = list(csv.DictReader(f))
        sucursales = [fila['PRSUC'] for fila in resultado]
        assert sucursales == ['SUC01', 'SUC02', 'SUC03']

    finally:
        os.remove(entrada)
        if os.path.exists(salida):
            os.remove(salida)


def test_ordenar_archivo_ya_ordenado_no_cambia_orden():
    filas = [
        {'PRSUC': 'SUC01', 'PRCOD': 'P001', 'PRCANT': '1', 'PRPRE': '5.00'},
        {'PRSUC': 'SUC02', 'PRCOD': 'P002', 'PRCANT': '2', 'PRPRE': '10.00'},
    ]
    entrada = crear_csv_temporal(filas)
    salida  = entrada + '_sorted.csv'

    try:
        ordenar_por_sucursal(entrada, salida)

        with open(salida, encoding='utf-8') as f:
            resultado = list(csv.DictReader(f))
        sucursales = [fila['PRSUC'] for fila in resultado]
        assert sucursales == ['SUC01', 'SUC02']

    finally:
        os.remove(entrada)
        if os.path.exists(salida):
            os.remove(salida)

# --- procesar_estadisticas ---

def test_procesar_muestra_nombre_sucursal(capsys):
    filas = [{'PRSUC': 'SUC01', 'PRCOD': 'P001', 'PRCANT': '2', 'PRPRE': '5.00'}]
    archivo = crear_csv_temporal(filas)

    try:
        procesar_estadisticas(archivo)

        salida = capsys.readouterr().out
        assert 'SUC01' in salida

    finally:
        os.remove(archivo)


def test_procesar_calcula_importe_correcto(capsys):
    filas = [{'PRSUC': 'SUC01', 'PRCOD': 'P001', 'PRCANT': '2', 'PRPRE': '10.00'}]
    archivo = crear_csv_temporal(filas)

    try:
        procesar_estadisticas(archivo)
        salida = capsys.readouterr().out
        assert '20.00' in salida

    finally:
        os.remove(archivo)


def test_procesar_muestra_multiples_sucursales(capsys):
    filas = [
        {'PRSUC': 'SUC01', 'PRCOD': 'P001', 'PRCANT': '1', 'PRPRE': '5.00'},
        {'PRSUC': 'SUC02', 'PRCOD': 'P002', 'PRCANT': '1', 'PRPRE': '5.00'},
    ]
    archivo = crear_csv_temporal(filas)

    try:
        procesar_estadisticas(archivo)
        salida = capsys.readouterr().out
        assert 'SUC01' in salida
        assert 'SUC02' in salida

    finally:
        os.remove(archivo)


def test_procesar_muestra_total_acumulado(capsys):
    filas = [
        {'PRSUC': 'SUC01', 'PRCOD': 'P001', 'PRCANT': '2', 'PRPRE': '10.00'},
        {'PRSUC': 'SUC01', 'PRCOD': 'P002', 'PRCANT': '3', 'PRPRE': '10.00'},
    ]
    archivo = crear_csv_temporal(filas)

    try:
        procesar_estadisticas(archivo)
        salida = capsys.readouterr().out
        assert '50.00' in salida

    finally:
        os.remove(archivo)
