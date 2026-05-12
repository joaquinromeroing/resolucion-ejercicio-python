import csv
import os

SEPARADOR = "=" * 50

def leer_compras(path):
    with open(path, mode='r', encoding='utf-8') as archivo:
        return list(csv.DictReader(archivo))

def ordenar_por_sucursal(path_entrada, path_salida):
    compras = leer_compras(path_entrada)
    n = len(compras)
    print(f"Ordenando {n} registros...")

    for i in range(n):
        for j in range(0, n - i - 1):
            if compras[j]['PRSUC'] > compras[j + 1]['PRSUC']:
                compras[j], compras[j + 1] = compras[j + 1], compras[j]

    columnas = compras[0].keys()
    with open(path_salida, mode='w', encoding='utf-8', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(compras)

def acumular_compra(datos, sucursal, producto, cantidad, precio):
    if sucursal not in datos:
        datos[sucursal] = {}
    if producto not in datos[sucursal]:
        datos[sucursal][producto] = {'total_unidades': 0, 'total_importe': 0.0}
    datos[sucursal][producto]['total_unidades'] += cantidad
    datos[sucursal][producto]['total_importe']  += cantidad * precio

def calcular_estadisticas(compras):
    datos = {}
    total_importe = 0.0

    for fila in compras:
        sucursal = fila['PRSUC']
        producto = fila['PRCOD']
        cantidad = int(fila['PRCANT'])
        precio   = float(fila['PRPRE'])
        acumular_compra(datos, sucursal, producto, cantidad, precio)
        total_importe += cantidad * precio

    return datos, total_importe

def imprimir_detalle_productos(productos):
    print("A) Detalle por Producto:")
    for producto, valores in productos.items():
        print(f"   {producto} | Unidades: {valores['total_unidades']} | Importe: ${valores['total_importe']:.2f}")

def imprimir_resumen_sucursal(sucursal, productos):
    total_unidades  = 0
    producto_mayor  = None
    importe_mayor   = -1.0
    producto_menor  = None
    importe_menor   = float('inf')

    for producto, valores in productos.items():
        total_unidades += valores['total_unidades']
        if valores['total_importe'] > importe_mayor:
            importe_mayor  = valores['total_importe']
            producto_mayor = producto
        if valores['total_importe'] < importe_menor:
            importe_menor  = valores['total_importe']
            producto_menor = producto

    print(f"\nB) Resumen de {sucursal}:")
    print(f"   - Total unidades: {total_unidades}")
    print(f"   - Mayor compra: {producto_mayor} (${importe_mayor:.2f})")
    print(f"   - Menor compra: {producto_menor} (${importe_menor:.2f})")
    print("-" * 50)

def procesar_estadisticas(path_archivo):
    compras = leer_compras(path_archivo)
    datos, total_importe = calcular_estadisticas(compras)

    print("\n" + SEPARADOR)
    print(" ESTADÍSTICAS DEL SUPERMERCADO ".center(50, "="))
    print(SEPARADOR)

    for sucursal, productos in datos.items():
        print(f"\n--- SUCURSAL: {sucursal} ---")
        imprimir_detalle_productos(productos)
        imprimir_resumen_sucursal(sucursal, productos)

    print(f"\nC) TOTALES GENERALES")
    print(f"   - Total sucursales: {len(datos)}")
    print(f"   - Compra total acumulada: ${total_importe:.2f}")
    print(SEPARADOR + "\n")

def menu():
    path_usuario = input("Indique el path del csv: ")

    if not os.path.exists(path_usuario):
        print("Error: El archivo no existe.")
        return

    esta_ordenado = input("¿El archivo está ordenado? (Y/N): ").strip().upper()

    if esta_ordenado == 'N':
        path_temp = "temp_ordenado.csv"
        ordenar_por_sucursal(path_usuario, path_temp)
        procesar_estadisticas(path_temp)
        os.remove(path_temp)
    elif esta_ordenado == 'Y':
        procesar_estadisticas(path_usuario)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()