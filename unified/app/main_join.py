import csv
import os


def calcular_importe(cantidad, precio):
    return int(cantidad) * float(precio)


def debe_intercambiar(r1, r2, clave='PRSUC'):
    return r1[clave] > r2[clave]


def ordenar_registros(registros):
    reg = list(registros)
    n = len(reg)
    for i in range(n):
        for j in range(0, n - i - 1):
            if debe_intercambiar(reg[j], reg[j + 1]):
                reg[j], reg[j + 1] = reg[j + 1], reg[j]
    return reg


def procesar_corte_control(registros):
    resultados = []
    i = 0
    while i < len(registros):
        suc_actual = registros[i]['PRSUC']
        sucursal_data = {
            'sucursal': suc_actual,
            'productos': [],
            'total_unidades': 0,
            'mejor_prod': None,
            'peor_prod': None,
            'mejor_monto': -1.0,
            'peor_monto': float('inf')
        }

        while i < len(registros) and registros[i]['PRSUC'] == suc_actual:
            prod_actual = registros[i]['PRCOD']
            tot_uni_prod = 0
            tot_pesos_prod = 0.0

            while i < len(registros) and \
                    registros[i]['PRSUC'] == suc_actual and \
                    registros[i]['PRCOD'] == prod_actual:
                unidades = int(registros[i]['PRCANT'])
                importe = calcular_importe(unidades, registros[i]['PRPRE'])
                tot_uni_prod += unidades
                tot_pesos_prod += importe
                i += 1

            sucursal_data['productos'].append({
                'cod': prod_actual,
                'unidades': tot_uni_prod,
                'pesos': tot_pesos_prod
            })
            sucursal_data['total_unidades'] += tot_uni_prod

            if tot_pesos_prod > sucursal_data['mejor_monto']:
                sucursal_data['mejor_monto'] = tot_pesos_prod
                sucursal_data['mejor_prod'] = prod_actual
            if tot_pesos_prod < sucursal_data['peor_monto']:
                sucursal_data['peor_monto'] = tot_pesos_prod
                sucursal_data['peor_prod'] = prod_actual

        resultados.append(sucursal_data)
    return resultados


def imprimir_reporte(resultados):
    total_general = 0
    print("\n" + "=" * 60)
    print(f"{'REPORTE CONSOLIDADO DE VENTAS':^60}")
    print("=" * 60)

    for suc in resultados:
        print(f"\nSUCURSAL: {suc['sucursal']}")
        print("-" * 60)
        for p in suc['productos']:
            print(f"  > {p['cod']:<12} | Uni: {p['unidades']:>5} | Subtotal: ${p['pesos']:>12.2f}")

        print("-" * 60)
        print(f"  Total Unidades: {suc['total_unidades']}")
        print(f"  Max: {suc['mejor_prod']} (${suc['mejor_monto']:.2f})")
        print(f"  Min: {suc['peor_prod']} (${suc['peor_monto']:.2f})")
        total_general += sum(p['pesos'] for p in suc['productos'])

    print("\n" + "*" * 60)
    print(f"  INGRESOS TOTALES COMPAÑÍA: ${total_general:>15.2f}")
    print("*" * 60)


def menu():
    ruta = input("Path del CSV: ").strip()
    if not os.path.exists(ruta):
        print("Archivo no encontrado.")
        return

    with open(ruta, 'r', encoding='utf-8') as f:
        datos = list(csv.DictReader(f))

    estado = input("¿Está ordenado? (S/N): ").strip().upper()
    if estado == 'N':
        print("Ordenando...")
        datos = ordenar_registros(datos)

    resultados = procesar_corte_control(datos)
    imprimir_reporte(resultados)


if __name__ == "__main__":
    menu()