import os
import pandas as pd


SALIDA_TXT = "salida.txt"
COLUMNAS_REQUERIDAS = ["PRSUC", "PRCOD", "PRCANT", "PRPRE"]


def emitir(lineas_salida, texto=""):
    print(texto)
    lineas_salida.append(str(texto))


def guardar_salida(lineas_salida, path_salida=SALIDA_TXT):
    with open(path_salida, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas_salida))
        archivo.write("\n")

    print(f"\nInforme guardado correctamente en: {path_salida}")


def validar_columnas(df):
    faltantes = []

    for columna in COLUMNAS_REQUERIDAS:
        if columna not in df.columns:
            faltantes.append(columna)

    if len(faltantes) > 0:
        raise KeyError(f"Faltan columnas: {faltantes}")


def leer_csv(path_csv):
    df = pd.read_csv(path_csv)
    validar_columnas(df)
    return df


def numero_sucursal(valor):
    texto = str(valor).replace("SUC", "").strip()
    return int(texto)


def clave_orden(registro):
    return (numero_sucursal(registro["PRSUC"]), str(registro["PRCOD"]))


def ordenar_registros_burbuja(registros):
    registros = [dict(registro) for registro in registros]
    n = len(registros)

    for i in range(n - 1):
        intercambio = False

        for j in range(n - 1 - i):
            if clave_orden(registros[j]) > clave_orden(registros[j + 1]):
                aux = registros[j]
                registros[j] = registros[j + 1]
                registros[j + 1] = aux
                intercambio = True

        if not intercambio:
            break

    return registros


def ordenar_dataframe_burbuja(df):
    validar_columnas(df)

    registros = df.to_dict(orient="records")
    registros_ordenados = ordenar_registros_burbuja(registros)

    return pd.DataFrame(registros_ordenados, columns=df.columns)


def ordenar_csv_burbuja(path_entrada, path_salida, lineas_salida=None):
    df = leer_csv(path_entrada)
    df_ordenado = ordenar_dataframe_burbuja(df)

    df_ordenado.to_csv(path_salida, index=False)

    if lineas_salida is not None:
        emitir(lineas_salida, "")
        emitir(lineas_salida, "Archivo temporal ordenado generado correctamente.")
        emitir(lineas_salida, f"Ruta: {path_salida}")

    return path_salida


def calcular_resumen_compras(df):
    validar_columnas(df)

    df_ordenado = ordenar_dataframe_burbuja(df)
    registros = df_ordenado.to_dict(orient="records")

    n = len(registros)
    i = 0

    resumen = {
        "sucursales": [],
        "cansuc": 0,
        "totalimp": 0.0
    }

    while i < n:
        suc_actual = registros[i]["PRSUC"]

        sucursal = {
            "sucursal": suc_actual,
            "productos": [],
            "totsuc": 0,
            "myprod": None,
            "myimpor": -1,
            "mnprod": None,
            "mnimpor": float("inf")
        }

        while i < n and registros[i]["PRSUC"] == suc_actual:
            prod_actual = registros[i]["PRCOD"]

            totuni = 0
            totpes = 0.0

            while (
                i < n
                and registros[i]["PRSUC"] == suc_actual
                and registros[i]["PRCOD"] == prod_actual
            ):
                cantidad = int(registros[i]["PRCANT"])
                precio = float(registros[i]["PRPRE"])
                importe = cantidad * precio

                totuni += cantidad
                totpes += importe

                i += 1

            producto = {
                "producto": prod_actual,
                "totuni": totuni,
                "totpes": totpes
            }

            sucursal["productos"].append(producto)
            sucursal["totsuc"] += totuni
            resumen["totalimp"] += totpes

            if totpes > sucursal["myimpor"]:
                sucursal["myimpor"] = totpes
                sucursal["myprod"] = prod_actual

            if totpes < sucursal["mnimpor"]:
                sucursal["mnimpor"] = totpes
                sucursal["mnprod"] = prod_actual

        resumen["sucursales"].append(sucursal)

    resumen["cansuc"] = len(resumen["sucursales"])

    return resumen


def generar_informe(resumen, lineas_salida):
    emitir(lineas_salida, "")
    emitir(lineas_salida, "=" * 60)
    emitir(lineas_salida, "INFORME DE COMPRAS")
    emitir(lineas_salida, "=" * 60)

    for sucursal in resumen["sucursales"]:
        emitir(lineas_salida, f"\nSucursal: {sucursal['sucursal']}")

        for producto in sucursal["productos"]:
            emitir(
                lineas_salida,
                f"  Producto {producto['producto']} -> "
                f"TOTUNI: {producto['totuni']} | "
                f"TOTPES: ${producto['totpes']:.2f}"
            )

        emitir(lineas_salida, f"  TOTSUC  : {sucursal['totsuc']}")
        emitir(
            lineas_salida,
            f"  MYPROD  : {sucursal['myprod']} | MYIMPOR: ${sucursal['myimpor']:.2f}"
        )
        emitir(
            lineas_salida,
            f"  MNPROD  : {sucursal['mnprod']} | MNIMPOR: ${sucursal['mnimpor']:.2f}"
        )

    emitir(lineas_salida, "")
    emitir(lineas_salida, "=" * 60)
    emitir(lineas_salida, "TOTALES GENERALES")
    emitir(lineas_salida, "=" * 60)
    emitir(lineas_salida, f"CANSUC   : {resumen['cansuc']}")
    emitir(lineas_salida, f"TOTALIMP : ${resumen['totalimp']:.2f}")


def procesar_compras(path_csv, lineas_salida):
    df = leer_csv(path_csv)
    resumen = calcular_resumen_compras(df)
    generar_informe(resumen, lineas_salida)

    return resumen


def pedir_opcion_ordenado():
    while True:
        opcion = input("El archivo está ordenado? (Y/N): ").strip().upper()

        if opcion in ("Y", "N"):
            return opcion

        print("Opción inválida. Ingrese Y o N.")


def obtener_path_temporal(path_csv):
    carpeta = os.path.dirname(path_csv)
    nombre_base = os.path.splitext(os.path.basename(path_csv))[0]

    return os.path.join(
        carpeta if carpeta else ".",
        f"{nombre_base}_temporal_ordenado.csv"
    )


def main():
    lineas_salida = []

    emitir(lineas_salida, "=" * 60)
    emitir(lineas_salida, "PROCESAMIENTO DE COMPRAS")
    emitir(lineas_salida, "=" * 60)

    path_csv = input("Indique el path del csv: ").strip()

    while path_csv == "":
        print("Debe ingresar una ruta válida.")
        path_csv = input("Indique el path del csv: ").strip()

    emitir(lineas_salida, f"Archivo indicado: {path_csv}")

    opcion = pedir_opcion_ordenado()
    emitir(lineas_salida, f"Archivo ordenado: {opcion}")

    try:
        if opcion == "N":
            path_temporal = obtener_path_temporal(path_csv)

            path_a_procesar = ordenar_csv_burbuja(
                path_csv,
                path_temporal,
                lineas_salida
            )
        else:
            path_a_procesar = path_csv

        procesar_compras(path_a_procesar, lineas_salida)
        guardar_salida(lineas_salida)

    except FileNotFoundError:
        emitir(lineas_salida, "")
        emitir(lineas_salida, "Error: no se encontró el archivo indicado.")
        guardar_salida(lineas_salida)

    except KeyError as e:
        emitir(lineas_salida, "")
        emitir(lineas_salida, f"Error: falta una columna en el CSV: {e}")
        guardar_salida(lineas_salida)

    except Exception as e:
        emitir(lineas_salida, "")
        emitir(lineas_salida, f"Ocurrió un error: {e}")
        guardar_salida(lineas_salida)


if __name__ == "__main__":
    main()