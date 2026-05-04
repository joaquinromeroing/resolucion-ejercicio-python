import os
import tempfile
import unittest

import pandas as pd

from tp_segmentado import (
    numero_sucursal,
    clave_orden,
    ordenar_registros_burbuja,
    ordenar_dataframe_burbuja,
    calcular_resumen_compras,
    guardar_salida,
    obtener_path_temporal
)


class TestTPSegmentado(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame([
            {"PRSUC": "SUC2", "PRCOD": "P2", "PRCANT": 1, "PRPRE": 50},
            {"PRSUC": "SUC1", "PRCOD": "P2", "PRCANT": 2, "PRPRE": 20},
            {"PRSUC": "SUC1", "PRCOD": "P1", "PRCANT": 3, "PRPRE": 5},
            {"PRSUC": "SUC2", "PRCOD": "P1", "PRCANT": 3, "PRPRE": 100},
            {"PRSUC": "SUC1", "PRCOD": "P1", "PRCANT": 1, "PRPRE": 5},
        ])

    def test_numero_sucursal(self):
        self.assertEqual(numero_sucursal("SUC1"), 1)
        self.assertEqual(numero_sucursal("SUC12"), 12)
        self.assertEqual(numero_sucursal("  SUC3  "), 3)

    def test_clave_orden(self):
        registro = {"PRSUC": "SUC10", "PRCOD": "P2"}
        self.assertEqual(clave_orden(registro), (10, "P2"))

    def test_ordenar_registros_burbuja(self):
        registros = self.df.to_dict(orient="records")
        ordenados = ordenar_registros_burbuja(registros)

        claves = [(r["PRSUC"], r["PRCOD"]) for r in ordenados]

        self.assertEqual(claves[0], ("SUC1", "P1"))
        self.assertEqual(claves[1], ("SUC1", "P1"))
        self.assertEqual(claves[2], ("SUC1", "P2"))
        self.assertEqual(claves[3], ("SUC2", "P1"))
        self.assertEqual(claves[4], ("SUC2", "P2"))

    def test_ordenar_dataframe_burbuja(self):
        df_ordenado = ordenar_dataframe_burbuja(self.df)

        self.assertEqual(df_ordenado.iloc[0]["PRSUC"], "SUC1")
        self.assertEqual(df_ordenado.iloc[0]["PRCOD"], "P1")
        self.assertEqual(df_ordenado.iloc[-1]["PRSUC"], "SUC2")
        self.assertEqual(df_ordenado.iloc[-1]["PRCOD"], "P2")

    def test_calcular_resumen_compras(self):
        resumen = calcular_resumen_compras(self.df)

        self.assertEqual(resumen["cansuc"], 2)
        self.assertAlmostEqual(resumen["totalimp"], 410.0)

        suc1 = resumen["sucursales"][0]
        self.assertEqual(suc1["sucursal"], "SUC1")
        self.assertEqual(suc1["totsuc"], 6)
        self.assertEqual(suc1["myprod"], "P2")
        self.assertAlmostEqual(suc1["myimpor"], 40.0)
        self.assertEqual(suc1["mnprod"], "P1")
        self.assertAlmostEqual(suc1["mnimpor"], 20.0)

        suc2 = resumen["sucursales"][1]
        self.assertEqual(suc2["sucursal"], "SUC2")
        self.assertEqual(suc2["totsuc"], 4)
        self.assertEqual(suc2["myprod"], "P1")
        self.assertAlmostEqual(suc2["myimpor"], 300.0)
        self.assertEqual(suc2["mnprod"], "P2")
        self.assertAlmostEqual(suc2["mnimpor"], 50.0)

    def test_guardar_salida(self):
        with tempfile.TemporaryDirectory() as carpeta_temporal:
            path_salida = os.path.join(carpeta_temporal, "salida_test.txt")

            guardar_salida(["Linea 1", "Linea 2"], path_salida)

            self.assertTrue(os.path.exists(path_salida))

            with open(path_salida, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            self.assertIn("Linea 1", contenido)
            self.assertIn("Linea 2", contenido)

    def test_obtener_path_temporal(self):
        path = "datos/compras.csv"
        resultado = obtener_path_temporal(path)

        self.assertEqual(resultado, "datos/compras_temporal_ordenado.csv")


if __name__ == "__main__":
    unittest.main()