import csv
import sys


def leer_entero(texto):
    texto_limpio = texto.strip()
    return int(texto_limpio)


def leer_decimal(texto):
    texto_limpio = texto.strip().replace(",", ".")
    return float(texto_limpio)


def cargar_compras(nombre_archivo):
    datos = {}

    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        filas = list(lector)
        i = 0
        while i < len(filas):
            fila = filas[i]
            sucursal = fila["PRSUC"].strip().upper()
            producto = fila["PRCOD"].strip().upper()
            cantidad = leer_entero(fila["PRCANT"])
            precio = leer_decimal(fila["PRPRE"])

            gasto = cantidad * precio

            if sucursal not in datos:
                datos[sucursal] = {}

            if producto not in datos[sucursal]:
                datos[sucursal][producto] = {
                    "unidades": 0,
                    "importe": 0.0,
                }

            datos[sucursal][producto]["unidades"] += cantidad
            datos[sucursal][producto]["importe"] += gasto
            
            i += 1

    return datos


def mostrar_informe(datos):
    total_general = 0.0

    print("INFORME DE COMPRAS")
    print("==================")

    sucursales = sorted(datos.keys())
    i = 0
    while i < len(sucursales):
        sucursal = sucursales[i]
        print()
        print("Sucursal:", sucursal)
        print("------------------------------")

        tot_suc = 0
        myprod = ""
        myimpor = -1.0
        mnprod = ""
        mnimpor = float("inf")

        productos = sorted(datos[sucursal].keys())
        j = 0
        while j < len(productos):
            producto = productos[j]
            totuni = datos[sucursal][producto]["unidades"]
            totpes = datos[sucursal][producto]["importe"]

            print("Producto:", producto)
            print("  TOTUNI:", totuni)
            print(f"  TOTPES: ${totpes:.2f}")

            tot_suc += totuni
            total_general += totpes

            if totpes > myimpor:
                myimpor = totpes
                myprod = producto

            if totpes < mnimpor:
                mnimpor = totpes
                mnprod = producto
            
            j += 1

        print("Resumen de la sucursal")
        print("  TOTSUC:", tot_suc)
        print(f"  Mayor compra: {myprod} (${myimpor:.2f})")
        print(f"  Menor compra: {mnprod} (${mnimpor:.2f})")
        
        i += 1

    print()
    print("TOTALES DEL SUPERMERCADO")
    print("========================")
    print("CANSUC:", len(datos))
    print(f"TOTALIMP: ${total_general:.2f}")


def procesar_compras(nombre_archivo):
    datos = cargar_compras(nombre_archivo)
    mostrar_informe(datos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python procesar_compras.py archivo.csv")
        sys.exit(1)

    try:
        procesar_compras(sys.argv[1])
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except KeyError:
        print("El CSV no tiene las columnas esperadas: PRSUC, PRCOD, PRCANT, PRPRE")
    except ValueError:
        print("Hay un dato numerico invalido en el archivo.")
