import os
import pandas as pd


def pedir_path_csv():
    while True:
        ruta = input('Ingrese el path del archivo CSV (o presione Enter para usar Compras.csv): ').strip()
        if ruta == '':
            ruta = 'Compras.csv'
        if os.path.isfile(ruta):
            return ruta
        print('Ruta inválida. Verifique el nombre y la ubicación del archivo.')


def cargar_csv(ruta):
    return pd.read_csv(ruta)


def esta_ordenado(df):
    if len(df) < 2:
        return True
    for i in range(1, len(df)):
        anterior = (df.at[i - 1, 'PRSUC'], df.at[i - 1, 'PRCOD'])
        actual = (df.at[i, 'PRSUC'], df.at[i, 'PRCOD'])
        if actual < anterior:
            return False
    return True


def ordenar_burbuja(df):
    registros = df.reset_index(drop=True).to_dict('records')
    n = len(registros)
    for i in range(n - 1):
        intercambiado = False
        for j in range(n - 1 - i):
            actual = (registros[j]['PRSUC'], registros[j]['PRCOD'])
            siguiente = (registros[j + 1]['PRSUC'], registros[j + 1]['PRCOD'])
            if actual > siguiente:
                registros[j], registros[j + 1] = registros[j + 1], registros[j]
                intercambiado = True
        if not intercambiado:
            break
    return pd.DataFrame(registros)


def guardar_csv(df, ruta):
    df.to_csv(ruta, index=False)


def mostrar_menu(df):
    i = 0
    numSuc = 0
    TotalImp = 0
    Mayor = 0
    Menor = 0

    while i < len(df):
        Ca = 0
        impT = 0
        numSuc += 1
        CantxSuc = 0
        su = df.at[i, 'PRSUC']
        print(f'Sucursal: {su}')

        while i < len(df) and df.at[i, 'PRSUC'] == su:
            pr = df.at[i, 'PRCOD']
            while i < len(df) and df.at[i, 'PRCOD'] == pr:
                Ca += df.at[i, 'PRCANT']
                impT = round(impT + (df.at[i, 'PRCANT'] * df.at[i, 'PRPRE']), 2)
                TotalImp = round(TotalImp + (df.at[i, 'PRCANT'] * df.at[i, 'PRPRE']), 2)
                CantxSuc += df.at[i, 'PRCANT']
                i += 1
            if impT > Mayor:
                Mayor = impT
                MyPR = pr
            if impT < Menor or Menor == 0:
                Menor = impT
                MnPR = pr
            print(f'Producto: {pr} - Cantidad: {Ca} - Importe Total: {impT}')
            Ca = 0
            impT = 0

        print(f'Cantidad x Sucursal: {CantxSuc}')
        print(f'Producto con mayor importe: {MyPR}, y su importe es: {Mayor}')
        print(f'Producto con menor importe: {MnPR}, y su importe es: {Menor}')

    print(f'Cantidad Total: {numSuc}')
    print(f'Total Importe: {TotalImp}')


def main():
    ruta = pedir_path_csv()
    df = cargar_csv(ruta)

    respuesta = input('¿Desea verificar si el archivo está ordenado antes de continuar? (S/N): ').strip().upper()
    if respuesta == 'S':
        if not esta_ordenado(df):
            print('El archivo no está ordenado. Se aplicará el ordenamiento por burbuja en memoria, sin modificar el CSV original.')
            df = ordenar_burbuja(df)
            print('Ordenamiento temporal aplicado. El archivo original no se modificó.')
    else:
        print('No se verificó el orden. Se continuará con el menú normal.')

    mostrar_menu(df)


if __name__ == '__main__':
    main()
