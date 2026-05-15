from ejpython import calcular_importe
from ejpython import calcular_totales_producto
from ejpython import actualizar_maximo, actualizar_minimo

def test_calcular_importe_normal():
    assert calcular_importe(3, 100.0) == 300.0

def test_calcular_importe_cero_cantidad():
    assert calcular_importe(0, 100.0) == 0.0

def test_calcular_importe_cero_precio():
    assert calcular_importe(3, 0.0) == 0.0
    
def test_calcular_totales_producto_normal():
    filas = [
        ["SUC1", "P001", "2024-01-01", "PROV1", "3", "100.0"],
        ["SUC1", "P001", "2024-01-01", "PROV1", "2", "100.0"],
    ]
    TOTUNI, TOTPES = calcular_totales_producto(filas)
    assert TOTUNI == 5
    assert TOTPES == 500.0

def test_calcular_totales_producto_una_fila():
    filas = [
        ["SUC1", "P001", "2024-01-01", "PROV1", "4", "50.0"],
    ]
    TOTUNI, TOTPES = calcular_totales_producto(filas)
    assert TOTUNI == 4
    assert TOTPES == 200.0

def test_actualizar_maximo_nuevo_mayor():
    importe, producto = actualizar_maximo(500.0, 200.0, "P002", "P001")
    assert importe == 500.0
    assert producto == "P002"

def test_actualizar_maximo_no_cambia():
    importe, producto = actualizar_maximo(100.0, 200.0, "P002", "P001")
    assert importe == 200.0
    assert producto == "P001"

def test_actualizar_minimo_nuevo_menor():
    importe, producto = actualizar_minimo(50.0, 200.0, "P002", "P001")
    assert importe == 50.0
    assert producto == "P002"

def test_actualizar_minimo_no_cambia():
    importe, producto = actualizar_minimo(300.0, 200.0, "P002", "P001")
    assert importe == 200.0
    assert producto == "P001"