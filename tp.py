import os
import pandas as pd


def numero_sucursal(valor):
    """
    Convierte valores tipo 'SUC1', 'SUC12', etc. a entero.
    """
    texto = str(valor).replace("SUC", "").strip()
    return int(texto)


def clave_orden(registro):
    """
    Clave de ordenamiento:
    1) sucursal
    2) codigo de producto
    """
    return (numero_sucursal(registro["PRSUC"]), str(registro["PRCOD"]))


def ordenar_csv_burbuja(path_entrada, path_salida):
    """
    Lee un CSV desordenado, lo ordena con burbuja y genera un nuevo CSV ordenado.
    """
    df = pd.read_csv(path_entrada)

    # Pasamos el DataFrame a lista de diccionarios
    registros = df.to_dict(orient="records")
    n = len(registros)

    # Ordenamiento burbuja
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

    # Volver a DataFrame y guardar
    df_ordenado = pd.DataFrame(registros, columns=df.columns)
    df_ordenado.to_csv(path_salida, index=False)

    print("\nArchivo temporal ordenado generado correctamente.")
    print(f"Ruta: {path_salida}")

    return path_salida


def procesar_compras(path_csv):
    """
    Procesa el archivo ya ordenado y emite el informe.
    """
    df = pd.read_csv(path_csv)

    # Convertimos el DataFrame a lista de registros
    registros = df.to_dict(orient="records")

    n = len(registros)
    i = 0
    cansuc = 0
    totalimp = 0.0

    print("\n" + "=" * 60)
    print("INFORME DE COMPRAS")
    print("=" * 60)

    while i < n:
        suc_actual = registros[i]["PRSUC"]
        cansuc += 1

        totsuc = 0  # total comprado en unidades en esa sucursal

        myprod = None
        myimpor = -1

        mnprod = None
        mnimpor = float("inf")

        print(f"\nSucursal: {suc_actual}")

        # Mientras siga la misma sucursal
        while i < n and registros[i]["PRSUC"] == suc_actual:
            prod_actual = registros[i]["PRCOD"]

            totuni = 0
            totpes = 0.0

            # Mientras siga el mismo producto dentro de esa sucursal
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

            # Mostrar resultado por producto
            print(f"  Producto {prod_actual} -> TOTUNI: {totuni} | TOTPES: ${totpes:.2f}")

            # Acumular total de unidades de la sucursal
            totsuc += totuni

            # Acumular total general en pesos
            totalimp += totpes

            # Buscar mayor compra por producto en pesos
            if totpes > myimpor:
                myimpor = totpes
                myprod = prod_actual

            # Buscar menor compra por producto en pesos
            if totpes < mnimpor:
                mnimpor = totpes
                mnprod = prod_actual

        # Mostrar resultado por sucursal
        print(f"  TOTSUC  : {totsuc}")
        print(f"  MYPROD  : {myprod} | MYIMPOR: ${myimpor:.2f}")
        print(f"  MNPROD  : {mnprod} | MNIMPOR: ${mnimpor:.2f}")

    print("\n" + "=" * 60)
    print("TOTALES GENERALES")
    print("=" * 60)
    print(f"CANSUC   : {cansuc}")
    print(f"TOTALIMP : ${totalimp:.2f}")


def pedir_opcion_ordenado():
    """
    Pide al usuario si el archivo ya está ordenado.
    """
    while True:
        opcion = input("El archivo está ordenado? (Y/N): ").strip().upper()

        if opcion in ("Y", "N"):
            return opcion

        print("Opción inválida. Ingrese Y o N.")


def main():
    print("=" * 60)
    print("PROCESAMIENTO DE COMPRAS")
    print("=" * 60)

    path_csv = input("Indique el path del csv: ").strip()

    while path_csv == "":
        print("Debe ingresar una ruta válida.")
        path_csv = input("Indique el path del csv: ").strip()

    opcion = pedir_opcion_ordenado()

    try:
        if opcion == "N":
            carpeta = os.path.dirname(path_csv)
            nombre_base = os.path.splitext(os.path.basename(path_csv))[0]
            path_temporal = os.path.join(
                carpeta if carpeta else ".",
                f"{nombre_base}_temporal_ordenado.csv"
            )

            path_a_procesar = ordenar_csv_burbuja(path_csv, path_temporal)
        else:
            path_a_procesar = path_csv

        procesar_compras(path_a_procesar)

    except FileNotFoundError:
        print("\nError: no se encontró el archivo indicado.")
    except KeyError as e:
        print(f"\nError: falta la columna {e} en el CSV.")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")


if __name__ == "__main__":
    main()


