import csv


def ordenar_burbuja(filas):
    n = len(filas)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if filas[j]["PRSUC"] > filas[j + 1]["PRSUC"]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]

    return filas


def leer_csv(path):
    archivo = open(path, encoding="utf-8")
    lector = csv.DictReader(archivo)
    filas = list(lector)
    encabezados = lector.fieldnames
    archivo.close()

    return filas, encabezados


def escribir_csv(path, filas, encabezados):
    archivo = open(path, "w", newline="", encoding="utf-8")
    escritor = csv.DictWriter(archivo, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(filas)
    archivo.close()


def procesar_corte_control(filas):
    n = len(filas)
    i = 0

    CANSUC = 0
    TOTALIMP = 0

    resultado = {
        "sucursales": [],
        "totales_generales": {}
    }

    while i < n:
        suc_actual = filas[i]["PRSUC"]

        TOTSUC = 0
        IMP_SUC = 0
        MYPROD = ""
        MYIMPOR = -1
        MNPROD = ""
        MNIMPOR = 999999999

        productos = []

        while i < n and filas[i]["PRSUC"] == suc_actual:
            prod_actual = filas[i]["PRCOD"]

            TOTUNI = 0
            TOTPES = 0

            while (
                i < n
                and filas[i]["PRSUC"] == suc_actual
                and filas[i]["PRCOD"] == prod_actual
            ):
                cantidad = int(filas[i]["PRCANT"])
                precio = float(filas[i]["PRPRE"])

                TOTUNI += cantidad
                TOTPES += cantidad * precio

                i += 1

            productos.append({
                "producto": prod_actual,
                "total_unidades": TOTUNI,
                "total_pesos": TOTPES
            })

            TOTSUC += TOTUNI
            IMP_SUC += TOTPES

            if TOTPES > MYIMPOR:
                MYIMPOR = TOTPES
                MYPROD = prod_actual

            if TOTPES < MNIMPOR:
                MNIMPOR = TOTPES
                MNPROD = prod_actual

        resultado["sucursales"].append({
            "sucursal": suc_actual,
            "productos": productos,
            "total_unidades": TOTSUC,
            "mayor_producto": MYPROD,
            "mayor_importe": MYIMPOR,
            "menor_producto": MNPROD,
            "menor_importe": MNIMPOR
        })

        CANSUC += 1
        TOTALIMP += IMP_SUC

    resultado["totales_generales"] = {
        "cantidad_sucursales": CANSUC,
        "total_importe": TOTALIMP
    }

    return resultado


def mostrar_resultado(resultado):
    for sucursal in resultado["sucursales"]:
        for producto in sucursal["productos"]:
            print(f"Producto {producto['producto']}")
            print(f"Total unidades: {producto['total_unidades']}")
            print(f"Total pesos: ${producto['total_pesos']:.2f}")

        print(f"\nSucursal {sucursal['sucursal']}")
        print(f"Total unidades: {sucursal['total_unidades']}")
        print(
            f"Mayor compra: {sucursal['mayor_producto']} "
            f"${sucursal['mayor_importe']:.2f}"
        )
        print(
            f"Menor compra: {sucursal['menor_producto']} "
            f"${sucursal['menor_importe']:.2f}"
        )

    print("\nTotales generales")
    print(f"Sucursales: {resultado['totales_generales']['cantidad_sucursales']}")
    print(f"Total: ${resultado['totales_generales']['total_importe']:.2f}")


def main():
    path = input("Indique el path del csv: ")
    ordenado = input("El archivo esta ordenado? (Y/N): ").upper()

    filas, encabezados = leer_csv(path)

    if ordenado == "N":
        print("Ordenando archivo...")

        filas = ordenar_burbuja(filas)

        archivo_temp = "archivo_ordenado_temp.csv"
        escribir_csv(archivo_temp, filas, encabezados)

        path = archivo_temp
        filas, encabezados = leer_csv(path)

    resultado = procesar_corte_control(filas)
    mostrar_resultado(resultado)


if __name__ == "__main__":
    main()