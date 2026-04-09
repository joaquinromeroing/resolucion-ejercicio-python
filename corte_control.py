import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ARCHIVO = "COMPRAS_supermercado.csv"

archivo = open(ARCHIVO, newline="", encoding="utf-8-sig")
lector  = csv.DictReader(archivo)

registros = list(lector)
archivo.close()

total_registros = len(registros)
i = 0 


def leer_registro(idx):
    """Devuelve el registro en la posición idx, o None si ya no hay más."""
    if idx < total_registros:
        r = registros[idx]
        return (
            r["PRSUC"],
            r["PRCOD"],
            r["PRFEC"],
            r["PRPROV"],
            int(r["PRCANT"]),
            float(r["PRPRE"]),
        )
    return None

CANSUC    = 0          
TOTALIMP  = 0.0        

reg = leer_registro(i)
i += 1

while reg is not None:

    suc_actual = reg[0]
    CANSUC   += 1
    TOTSUC    = 0.0   
    TOTSUC_P  = 0.0   

    MYPROD   = None
    MYIMPOR  = -1.0
    MNPROD   = None
    MNIMPOR  = float("inf")

    print("=" * 60)
    print(f"SUCURSAL: {suc_actual}")
    print("=" * 60)

    while reg is not None and reg[0] == suc_actual:

        prod_actual = reg[1]
        TOTUNI = 0      
        TOTPES = 0.0     

        while reg is not None and reg[0] == suc_actual and reg[1] == prod_actual:
            prsuc, prcod, prfec, prprov, prcant, prpre = reg

            TOTUNI += prcant
            TOTPES += prcant * prpre

            reg = leer_registro(i)
            i += 1

        TOTSUC   += TOTUNI
        TOTSUC_P += TOTPES

        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD  = prod_actual
        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPROD  = prod_actual

        print(f"  Producto: {prod_actual:>6}  |  "
              f"Total unidades: {TOTUNI:>7,}  |  "
              f"Total pesos: ${TOTPES:>14,.2f}")

    TOTALIMP += TOTSUC_P

    print("-" * 60)
    print(f"  TOTAL SUCURSAL {suc_actual}")
    print(f"    Total unidades compradas : {TOTSUC:>10,}")
    print(f"    Total pesos comprados    : ${TOTSUC_P:>14,.2f}")
    print(f"    Producto mayor compra    : {MYPROD}  (${MYIMPOR:,.2f})")
    print(f"    Producto menor compra    : {MNPROD}  (${MNIMPOR:,.2f})")
    print()

print("=" * 60)
print("  TOTALES GENERALES")
print("=" * 60)
print(f"  Total de sucursales          : {CANSUC}")
print(f"  Compra total en pesos        : ${TOTALIMP:>16,.2f}")
print("=" * 60)