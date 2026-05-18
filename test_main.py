import os
import pytest

from main import (
    construir_ruta,
    leer_csv,
    escribir_csv,
    ordenar_datos_burbuja,
    procesar_corte_de_control,
    imprimir_reporte_corte,
    menu
)

# 1. Tests de Manejo de Archivos

def test_construir_ruta():
    directorio = "carpeta"
    archivo = "datos.csv"
    assert construir_ruta(directorio, archivo) == os.path.join(directorio, archivo)

def test_leer_csv(mocker):
    # Simulamos el contenido de un CSV
    contenido_csv_simulado = "Sucursal,Producto,Cat,Marca,Cant,Precio\nCentro,Arroz,X,Y,5,100.0\n"
    
    mocker.patch('builtins.open', mocker.mock_open(read_data=contenido_csv_simulado))
    
    encabezados, datos = leer_csv("ruta_falsa.csv")
    
    assert encabezados == ["Sucursal", "Producto", "Cat", "Marca", "Cant", "Precio"]
    assert datos == [["Centro", "Arroz", "X", "Y", "5", "100.0"]]

def test_escribir_csv(mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    
    encabezados = ["Col1", "Col2"]
    datos = [["A", "B"]]
    
    escribir_csv("ruta_falsa.csv", encabezados, datos)
    
    mock_open.assert_called_once_with("ruta_falsa.csv", mode='w', encoding='utf-8', newline='')

# 2. Test de Ordenar y Procesar

def test_ordenar_datos_burbuja():
    datos_desordenados = [
        ["Sucursal Sur", "Zanahoria", "X", "Y", "5", "10.0"],
        ["Sucursal Centro", "Manzana", "X", "Y", "2", "50.0"],
        ["Sucursal Centro", "Banana", "X", "Y", "10", "20.0"]
    ]
    
    datos_esperados = [
        ["Sucursal Centro", "Banana", "X", "Y", "10", "20.0"],
        ["Sucursal Centro", "Manzana", "X", "Y", "2", "50.0"],
        ["Sucursal Sur", "Zanahoria", "X", "Y", "5", "10.0"]
    ]

    resultado = ordenar_datos_burbuja(datos_desordenados)

    assert resultado == datos_esperados
    assert datos_desordenados != resultado

def test_procesar_corte_de_control():
    datos_ordenados = [
        ["Sucursal Centro", "Arroz", "Grano", "MarcaA", "2", "100.0"], 
        ["Sucursal Centro", "Arroz", "Grano", "MarcaA", "3", "100.0"], 
        ["Sucursal Centro", "Fideos", "Pasta", "MarcaB", "1", "150.0"],
        ["Sucursal Sur", "Arroz", "Grano", "MarcaA", "4", "100.0"]     
    ]

    resultado = procesar_corte_de_control(datos_ordenados)

    assert resultado["cantidad_sucursales"] == 2
    assert resultado["total_general"] == 1050.0 

    suc_centro = resultado["sucursales"][0]
    assert suc_centro["nombre"] == "Sucursal Centro"
    assert suc_centro["total_unidades_sucursal"] == 6
    assert suc_centro["mayor_producto"] == "Arroz"
    assert suc_centro["mayor_importe"] == 500.0

# 3. Test de Imprimir Resultados

def test_imprimir_reporte_corte(capsys):
    resultados_simulados = {
        "cantidad_sucursales": 1,
        "total_general": 1000.0,
        "sucursales": [{
            "nombre": "Sucursal Test",
            "productos": [{"nombre": "Prod A", "unidades": 10, "total_pesos": 1000.0}],
            "total_unidades_sucursal": 10,
            "mayor_producto": "Prod A",
            "mayor_importe": 1000.0,
            "menor_producto": "Prod A",
            "menor_importe": 1000.0
        }]
    }

    imprimir_reporte_corte(resultados_simulados)
    
    consola = capsys.readouterr()
    
    assert "SUCURSAL: Sucursal Test" in consola.out
    assert "Producto: Prod A - Unidades: 10 - Total: $1000.00" in consola.out
    assert "c) TOTALES GENERALES" in consola.out
    assert "Compra total general: $1000.00" in consola.out

# 4. Test del Menu Principal

def test_menu_archivo_no_existe(mocker, capsys):
    mocker.patch('builtins.input', side_effect=["./", "falso.csv"])
    mocker.patch('os.path.exists', return_value=False)
    
    menu()
    
    consola = capsys.readouterr()
    assert "Error: El archivo no existe en la ruta especificada." in consola.out

def test_menu_archivo_desordenado_N(mocker, capsys):
    # Simulamos inputs: carpeta, archivo, y "N" para que lo ordene
    mocker.patch('builtins.input', side_effect=["./", "real.csv", "N"])
    mocker.patch('os.path.exists', return_value=True)
    
    # Mockeamos las funciones internas para que no hagan el trabajo real
    mock_leer = mocker.patch('main.leer_csv', return_value=(["Enc"], [["Dat"]]))
    mock_ordenar = mocker.patch('main.ordenar_datos_burbuja', return_value=[["Dat_Ord"]])
    mock_escribir = mocker.patch('main.escribir_csv')
    mock_procesar = mocker.patch('main.procesar_corte_de_control', return_value={"mock": "data"})
    mock_imprimir = mocker.patch('main.imprimir_reporte_corte')
    
    menu()
    
    # Verificamos que pasó por el camino largo (ordenar y guardar)
    mock_leer.assert_called_once()
    mock_ordenar.assert_called_once()
    mock_escribir.assert_called_once()
    mock_procesar.assert_called_once()
    mock_imprimir.assert_called_once()
    
    consola = capsys.readouterr()
    assert "Ordenando el archivo..." in consola.out

def test_menu_archivo_ordenado_Y(mocker):
    # Simulamos inputs: carpeta, archivo, y "Y" (ya está ordenado)
    mocker.patch('builtins.input', side_effect=["./", "real.csv", "Y"])
    mocker.patch('os.path.exists', return_value=True)
    
    # Mockeamos las funciones
    mock_leer = mocker.patch('main.leer_csv', return_value=(["Enc"], [["Dat"]]))
    mock_ordenar = mocker.patch('main.ordenar_datos_burbuja')
    mock_escribir = mocker.patch('main.escribir_csv')
    mock_procesar = mocker.patch('main.procesar_corte_de_control', return_value={"mock": "data"})
    mock_imprimir = mocker.patch('main.imprimir_reporte_corte')
    
    menu()
    
    # Verificamos que pasó por el camino corto (lee y procesa directo)
    mock_leer.assert_called_once()
    mock_procesar.assert_called_once()
    mock_imprimir.assert_called_once()
    
    # Estas dos NO debieron ser llamadas
    mock_ordenar.assert_not_called()
    mock_escribir.assert_not_called()
    
# python3 -m pytest test_main.py -v