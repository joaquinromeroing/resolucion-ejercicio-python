import pytest
import os
import tempfile
from unittest.mock import patch
from io import StringIO
#las funciones a testear
from ejercicio import Order_product, analysis

 
def crear_csv(contenido: str) -> str:
    """Crea un archivo CSV temporal y devuelve su path."""
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8")
    tmp.write(contenido)
    tmp.close()
    return tmp.name
 
 
class TestOrderProduct:
 
    def test_archivo_ya_ordenado(self, tmp_path):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"
            "A,Fideos,2024-01-02,Alimentos,5,3.0\n"
            "B,Leche,2024-01-03,Lacteos,8,2.5\n"
        )
        path_entrada = crear_csv(contenido)
 
        resultado = Order_product(path_entrada)
 
        with open(resultado, "r") as f:
            lineas = f.readlines()
 
        assert lineas[1].startswith("A,Arroz")
        assert lineas[2].startswith("A,Fideos")
        assert lineas[3].startswith("B,Leche")
 
        os.unlink(path_entrada)
 
    def test_archivo_desordenado_queda_ordenado(self):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "B,Leche,2024-01-01,Lacteos,8,2.5\n"
            "A,Fideos,2024-01-02,Alimentos,5,3.0\n"
            "A,Arroz,2024-01-03,Alimentos,10,5.0\n"
        )
        path_entrada = crear_csv(contenido)
 
        resultado = Order_product(path_entrada)
 
        with open(resultado, "r") as f:
            lineas = f.readlines()
 
        assert lineas[1].startswith("A,Arroz")
        assert lineas[2].startswith("A,Fideos")
        assert lineas[3].startswith("B,Leche")
 
        os.unlink(path_entrada)
 
    def test_encabezado_se_conserva(self):
        encabezado = "sucursal,producto,fecha,categoria,cantidad,precio\n"
        contenido = encabezado + "B,Leche,2024-01-01,Lacteos,8,2.5\n"
        path_entrada = crear_csv(contenido)
 
        resultado = Order_product(path_entrada)
 
        with open(resultado, "r") as f:
            primera_linea = f.readline()
 
        assert primera_linea == encabezado
 
        os.unlink(path_entrada)
 
    def test_retorna_path_del_archivo_ordenado(self):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"
        )
        path_entrada = crear_csv(contenido)
 
        resultado = Order_product(path_entrada)
 
        assert resultado == "archivo_ordenado.csv"
        assert os.path.exists(resultado)
 
        os.unlink(path_entrada)
 
    def test_una_sola_fila_de_datos(self):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"
        )
        path_entrada = crear_csv(contenido)
 
        resultado = Order_product(path_entrada)
 
        with open(resultado, "r") as f:
            lineas = f.readlines()
 
        assert len(lineas) == 2  # encabezado y fila
        os.unlink(path_entrada)
 
    def test_multiples_sucursales_orden_correcto(self):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "C,Azucar,2024-01-01,Alimentos,2,1.0\n"
            "A,Sal,2024-01-02,Alimentos,3,0.5\n"
            "B,Yerba,2024-01-03,Infusiones,4,8.0\n"
            "A,Aceite,2024-01-04,Alimentos,1,12.0\n"
        )
        path_entrada = crear_csv(contenido)
 
        resultado = Order_product(path_entrada)
 
        with open(resultado, "r") as f:
            lineas = f.readlines()
 
        # Esperado: A-Aceite, A-Sal, B-Yerba, C-Azucar
        assert lineas[1].startswith("A,Aceite")
        assert lineas[2].startswith("A,Sal")
        assert lineas[3].startswith("B,Yerba")
        assert lineas[4].startswith("C,Azucar")
 
        os.unlink(path_entrada)
 
 
class TestAnalysis:
 
    def _csv_una_sucursal_un_producto(self):
        return (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"
        )
 
    def test_imprime_total_sucursales(self, capsys):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"
            "B,Leche,2024-01-02,Lacteos,5,3.0\n"
        )
        path = crear_csv(contenido)
 
        analysis(path)
 
        captured = capsys.readouterr()
        assert "Total sucursales: 2" in captured.out
 
        os.unlink(path)
 
    def test_imprime_total_importe(self, capsys):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"
        )
        path = crear_csv(contenido)
 
        analysis(path)
 
        captured = capsys.readouterr()
        assert "Total importe: $50.0" in captured.out
 
        os.unlink(path)
 
    def test_mayor_y_menor_producto_misma_sucursal(self, capsys):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"   
            "A,Fideos,2024-01-02,Alimentos,2,3.0\n"
        )
        path = crear_csv(contenido)
 
        analysis(path)
 
        captured = capsys.readouterr()
        assert "Mayor producto: Arroz" in captured.out
        assert "Menor producto: Fideos" in captured.out
 
        os.unlink(path)
 
    def test_unidades_por_producto(self, capsys):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,5.0\n"
            "A,Arroz,2024-01-02,Alimentos,5,5.0\n"
        )
        path = crear_csv(contenido)
 
        analysis(path)
 
        captured = capsys.readouterr()
        assert "Total unidades: 15" in captured.out
 
        os.unlink(path)
 
    def test_pesos_por_producto(self, capsys):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,4,2.5\n" 
        )
        path = crear_csv(contenido)
 
        analysis(path)
 
        captured = capsys.readouterr()
        assert "Total pesos: 10.0" in captured.out
 
        os.unlink(path)
 
    def test_multiple_sucursales_total_importe_acumulado(self, capsys):
        contenido = (
            "sucursal,producto,fecha,categoria,cantidad,precio\n"
            "A,Arroz,2024-01-01,Alimentos,10,2.0\n"   
            "B,Leche,2024-01-02,Lacteos,5,4.0\n" 
        )
        path = crear_csv(contenido)
 
        analysis(path)
 
        captured = capsys.readouterr()
        assert "Total importe: $40.0" in captured.out
 
        os.unlink(path)
