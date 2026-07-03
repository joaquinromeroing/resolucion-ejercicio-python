from script_ordenamiento import ordenar_por_sucursal, calcular_totales_por_sucursal


def test_ordenar_por_sucursal():

    datos = [
        ["B", "prod1"],
        ["A", "prod2"],
        ["C", "prod3"]
    ]

    resultado = ordenar_por_sucursal(datos)

    assert resultado[0][0] == "A"
    assert resultado[1][0] == "B"
    assert resultado[2][0] == "C"


def test_calcular_totales_por_sucursal():

    datos = [
        ["A", "", "", "", "10"],
        ["A", "", "", "", "5"],
        ["B", "", "", "", "7"]
    ]

    resultado = calcular_totales_por_sucursal(datos)

    assert resultado["A"] == 15
    assert resultado["B"] == 7
    assert resultado["B"] == 7