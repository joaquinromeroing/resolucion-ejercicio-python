from main_join import calcular_importe, ordenar_registros, procesar_corte_control

def test_calculos():
    assert calcular_importe(5, 100) == 500.0
    assert calcular_importe("2", "50.5") == 101.0

def test_ordenamiento():
    data = [
        {'PRSUC': 'SUC_03', 'PRCOD': 'A'},
        {'PRSUC': 'SUC_01', 'PRCOD': 'B'}
    ]
    ordenada = ordenar_registros(data)
    assert ordenada[0]['PRSUC'] == 'SUC_01'
    assert ordenada[1]['PRSUC'] == 'SUC_03'

def test_corte_control():
    mock_datos = [
        {'PRSUC': '1', 'PRCOD': 'PAN', 'PRCANT': '10', 'PRPRE': '2'},
        {'PRSUC': '1', 'PRCOD': 'MILK', 'PRCANT': '1', 'PRPRE': '5'},
    ]
    res = procesar_corte_control(mock_datos)

    suc1 = res[0]
    assert suc1['sucursal'] == '1'
    assert suc1['total_unidades'] == 11
    assert suc1['mejor_prod'] == 'PAN'
    assert suc1['peor_prod'] == 'MILK'
    assert suc1['mejor_monto'] == 20.0