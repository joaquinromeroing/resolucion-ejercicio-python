from datetime import date
import csv

route = 'COMPRAS_supermercado.csv'


archivo = open(route, mode='r', encoding='utf-8')
lector  = csv.reader(archivo)
next(lector)


def leer(lector):
    fila = next(lector, None)
    if fila is None:
        return None
    return {
        'PRSUC' : fila[0],
        'PRCOD' : fila[1],
        'PRFEC' : fila[2],
        'PRPROV': fila[3],
        'PRCANT': int(fila[4]),
        'PRPRE' : float(fila[5])
    }


CANSUC   = 0
TOTALIMP = 0.0

print("=" * 66)
print("   ESTADÍSTICA DE COMPRAS - SUPERMERCADO")
print("=" * 66)

reg = leer(lector)


while reg is not None:

    SUC_ACTUAL = reg['PRSUC']
    TOTSUC_UNI = 0
    TOTSUC_IMP = 0.0
    MYPROD     = None;  MYIMPOR = None
    MNPROD     = None;  MNIMPOR = None

    print()
    print("-" * 66)
    print(f" SUCURSAL: {SUC_ACTUAL}")
    print("-" * 66)
    print(f"  {'PRODUCTO':<10}  {'UNIDADES':>10}  {'IMPORTE':>18}")
    print(f"  {'-'*10}  {'-'*10}  {'-'*18}")


    while reg is not None and reg['PRSUC'] == SUC_ACTUAL:

        PROD_ACTUAL = reg['PRCOD']
        TOTUNI      = 0
        TOTPES      = 0.0


        while reg is not None and reg['PRSUC'] == SUC_ACTUAL and reg['PRCOD'] == PROD_ACTUAL:
            TOTUNI += reg['PRCANT']
            TOTPES += reg['PRCANT'] * reg['PRPRE']
            reg     = leer(lector)

        print(f"  {PROD_ACTUAL:<10}  {TOTUNI:>10,}  ${TOTPES:>17,.2f}")

        TOTSUC_UNI += TOTUNI
        TOTSUC_IMP += TOTPES

        if MYIMPOR is None or TOTPES > MYIMPOR:
            MYPROD = PROD_ACTUAL;  MYIMPOR = TOTPES
        if MNIMPOR is None or TOTPES < MNIMPOR:
            MNPROD = PROD_ACTUAL;  MNIMPOR = TOTPES


    print(f"  {'-'*10}  {'-'*10}  {'-'*18}")
    print(f"  {'TOTAL':<10}  {TOTSUC_UNI:>10,}  ${TOTSUC_IMP:>17,.2f}")
    print()
    print(f"  >> Mayor compra: {MYPROD:<10}  ${MYIMPOR:>17,.2f}")
    print(f"  >> Menor compra: {MNPROD:<10}  ${MNIMPOR:>17,.2f}")

    CANSUC   += 1
    TOTALIMP += TOTSUC_IMP

archivo.close()

print()
print("=" * 66)
print("            RESUMEN GENERAL")
print("=" * 66)
print(f"  Total sucursales  : {CANSUC}")
print(f"  Total en pesos    : ${TOTALIMP:>17,.2f}")
print("=" * 66)