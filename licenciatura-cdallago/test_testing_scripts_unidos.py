from scripts_unidos import ordenar_por_sucursal, procesar_sucursal


def test_flujo_completo_ordenamiento_y_analisis():

    # 1. Datos desordenados
    datos_desordenados = [
        ["Sucursal_B", "P01", "Producto 1", "100", "2"],
        ["Sucursal_A", "P02", "Producto 2", "50", "10"],
        ["Sucursal_A", "P01", "Producto 1", "100", "5"]
    ]

    # 2. Test de ordenamiento
    ordenados = ordenar_por_sucursal(datos_desordenados)

    assert ordenados[0][0] == "Sucursal_A"
    assert ordenados[-1][0] == "Sucursal_B"

    # 3. Datos simulados para análisis
    datos_para_analisis = [
        {'PRSUC': 'Sucursal_A', 'PRCOD': 'P01', 'PRPRE': '100', 'PRCANT': '5'},
        {'PRSUC': 'Sucursal_A', 'PRCOD': 'P02', 'PRPRE': '50', 'PRCANT': '10'},
        {'PRSUC': 'Sucursal_B', 'PRCOD': 'P01', 'PRPRE': '100', 'PRCANT': '2'}
    ]

    # 4. Test procesamiento sucursal A
    resumen_a, siguiente_idx = procesar_sucursal(datos_para_analisis, 0)

    assert resumen_a['sucursal'] == "Sucursal_A"
    assert resumen_a['total_pesos'] == 1000.0

    # 5. Test sucursal B
    resumen_b, final = procesar_sucursal(datos_para_analisis, siguiente_idx)

    assert resumen_b['total_pesos'] == 200.0


if __name__ == "__main__":
    test_flujo_completo_ordenamiento_y_analisis()
    print("✅ Tests ejecutados con éxito.")