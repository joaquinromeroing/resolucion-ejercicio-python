import runpy
import pandas as pd
from pathlib import Path


RUTA_UNIFICADO = Path(__file__).resolve().parent.parent / "unificado.py"


def test_crea_archivo_ordenado(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    archivo = tmp_path / "COMPRAS_supermercado_desordenado_solo_sucursal.csv"

    archivo.write_text(
        "PRSUC,PRCOD,PRFEC,PRPROV,PRCANT,PRPRE\n"
        "SUC08,P100,2025-04-10,PROV09,58,252.38\n"
        "SUC08,P100,2025-02-04,PROV08,55,266.91\n"
        "SUC08,P100,2025-03-03,PROV01,54,254.8\n"
    )

    runpy.run_path(str(RUTA_UNIFICADO))

    archivo_ordenado = tmp_path / "COMPRAS_supermercado_ordenado.csv"

    assert archivo_ordenado.exists()


def test_archivo_ordenado_correctamente(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    archivo = tmp_path / "COMPRAS_supermercado_desordenado_solo_sucursal.csv"

    archivo.write_text(
        "PRSUC,PRCOD,PRFEC,PRPROV,PRCANT,PRPRE\n"
        "SUC08,P100,2025-04-10,PROV09,58,252.38\n"
        "SUC08,P100,2025-02-04,PROV08,55,266.91\n"
        "SUC08,P100,2025-03-03,PROV01,54,254.8\n"
    )

    runpy.run_path(str(RUTA_UNIFICADO))

    df = pd.read_csv("COMPRAS_supermercado_ordenado.csv")

    assert list(df["PRFEC"]) == [
        "2025-02-04",
        "2025-03-03",
        "2025-04-10"
    ]


def test_total_general_correcto(tmp_path, monkeypatch, capsys):

    monkeypatch.chdir(tmp_path)

    archivo = tmp_path / "COMPRAS_supermercado_desordenado_solo_sucursal.csv"

    archivo.write_text(
        "PRSUC,PRCOD,PRFEC,PRPROV,PRCANT,PRPRE\n"
        "SUC08,P100,2025-02-04,PROV08,55,266.91\n"
        "SUC08,P100,2025-02-17,PROV08,44,257.81\n"
    )

    runpy.run_path(str(RUTA_UNIFICADO))

    salida = capsys.readouterr().out

    total = (55 * 266.91) + (44 * 257.81)

    assert f"Total general $: {total}" in salida


def test_cantidad_sucursales_correcta(tmp_path, monkeypatch, capsys):

    monkeypatch.chdir(tmp_path)

    archivo = tmp_path / "COMPRAS_supermercado_desordenado_solo_sucursal.csv"

    archivo.write_text(
        "PRSUC,PRCOD,PRFEC,PRPROV,PRCANT,PRPRE\n"
        "SUC08,P100,2025-02-04,PROV08,55,266.91\n"
        "SUC09,P100,2025-02-17,PROV08,44,257.81\n"
    )

    runpy.run_path(str(RUTA_UNIFICADO))

    salida = capsys.readouterr().out

    assert "Cantidad de sucursales: 2" in salida

    #cicd
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parents[1]))

    from unificado import calcular_total_compra

    def test_calcular_total_compra():
        resultado = calcular_total_compra(3, 150)
        assert resultado == 450