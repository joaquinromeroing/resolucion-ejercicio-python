from pathlib import Path
import os

import pandas as pd


RUTA_ENTRADA_PREDETERMINADA = Path("/data/datos.csv")
RUTA_ENTRADA_EMBEBIDA = Path("/app/data/datos.csv")
DIRECTORIO_SALIDA = Path(os.getenv("OUTPUT_DIR", "/output"))
ARCHIVO_SALIDA = DIRECTORIO_SALIDA / "resultado.txt"


def moneda(valor):
    return f"${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def obtener_archivo_entrada():
    ruta_configurada = Path(os.getenv("INPUT_CSV", str(RUTA_ENTRADA_PREDETERMINADA)))

    for ruta in (ruta_configurada, RUTA_ENTRADA_EMBEBIDA):
        if ruta.exists():
            return ruta

    raise FileNotFoundError(
        "No se encontro el archivo de entrada ni en /data/datos.csv ni en /app/data/datos.csv."
    )


def generar_reporte(df):
    trabajo = df.copy()
    trabajo["PRCANT"] = pd.to_numeric(trabajo["PRCANT"])
    trabajo["PRPRE"] = pd.to_numeric(trabajo["PRPRE"])
    trabajo["IMPORTE"] = trabajo["PRCANT"] * trabajo["PRPRE"]

    por_producto = (
        trabajo.groupby(["PRSUC", "PRCOD"], as_index=False)
        .agg(TOTUNI=("PRCANT", "sum"), TOTPES=("IMPORTE", "sum"))
        .sort_values(["PRSUC", "PRCOD"])
    )

    lineas = []
    lineas.append("A) POR PRODUCTO")
    lineas.append("-" * 60)
    for fila in por_producto.itertuples(index=False):
        lineas.append(
            f"Sucursal: {fila.PRSUC} | Producto: {fila.PRCOD} | "
            f"TOTUNI: {int(fila.TOTUNI)} | TOTPES: {moneda(fila.TOTPES)}"
        )

    lineas.append("")
    lineas.append("B) POR SUCURSAL")
    lineas.append("-" * 60)
    for sucursal, grupo in por_producto.groupby("PRSUC", sort=True):
        fila_mayor = grupo.loc[grupo["TOTPES"].idxmax()]
        fila_menor = grupo.loc[grupo["TOTPES"].idxmin()]
        total_unidades = int(grupo["TOTUNI"].sum())
        total_pesos = grupo["TOTPES"].sum()

        lineas.append(f"Sucursal: {sucursal}")
        lineas.append(f"Total unidades: {total_unidades}")
        lineas.append(f"Total pesos: {moneda(total_pesos)}")
        lineas.append(
            f"Producto mayor: {fila_mayor['PRCOD']} | Importe mayor: {moneda(fila_mayor['TOTPES'])}"
        )
        lineas.append(
            f"Producto menor: {fila_menor['PRCOD']} | Importe menor: {moneda(fila_menor['TOTPES'])}"
        )
        lineas.append("-" * 60)

    lineas.append("")
    lineas.append("C) TOTAL GENERAL")
    lineas.append("-" * 60)
    lineas.append(f"Cantidad sucursales: {por_producto['PRSUC'].nunique()}")
    lineas.append(f"Importe total: {moneda(trabajo['IMPORTE'].sum())}")

    return "\n".join(lineas) + "\n"


def main():
    archivo_entrada = obtener_archivo_entrada()
    df = pd.read_csv(archivo_entrada)
    reporte = generar_reporte(df)

    DIRECTORIO_SALIDA.mkdir(parents=True, exist_ok=True)
    ARCHIVO_SALIDA.write_text(reporte, encoding="utf-8")

    print(f"Analisis terminado. Archivo generado en {ARCHIVO_SALIDA}")


if __name__ == "__main__":
    main()
