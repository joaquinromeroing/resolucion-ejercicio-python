import csv

def ejecutar():
    print("--- INICIANDO PROCESAMIENTO ---")
    CANSUC = 0
    TOTALIMP = 0

    try:
        with open('COMPRAS.csv', mode='r', encoding='utf-8') as archivo:
            lector = list(csv.reader(archivo))
            i = 1 
            n = len(lector)

            while i < n:
                PRSUC_ACTUAL = lector[i][0]
                CANSUC += 1
                TOTSUC = 0
                SUC_PESOS = 0
                MYPROD, MYIMPOR = "", -1.0
                MNPROD, MNIMPOR = "", float('inf')

                while i < n and lector[i][0] == PRSUC_ACTUAL:
                    PRCOD_ACTUAL = lector[i][1]
                    TOTUNI = 0
                    TOTPES = 0

                    while i < n and lector[i][0] == PRSUC_ACTUAL and lector[i][1] == PRCOD_ACTUAL:
                        CANT = int(lector[i][4])
                        PRECIO = float(lector[i][5])
                        TOTUNI += CANT
                        TOTPES += (CANT * PRECIO)
                        i += 1 

                    print(f"Suc: {PRSUC_ACTUAL} | Prod: {PRCOD_ACTUAL} | Unidades: {TOTUNI} | $: {TOTPES:.2f}")

                    if TOTPES > MYIMPOR:
                        MYIMPOR = TOTPES
                        MYPROD = PRCOD_ACTUAL
                    if TOTPES < MNIMPOR:
                        MNIMPOR = TOTPES
                        MNPROD = PRCOD_ACTUAL
                    
                    TOTSUC += TOTUNI
                    SUC_PESOS += TOTPES

                print("-" * 50)
                print(f"RESUMEN SUCURSAL {PRSUC_ACTUAL}: Total {TOTSUC} uni | Mayor: {MYPROD} | Menor: {MNPROD}")
                print("-" * 50)
                TOTALIMP += SUC_PESOS

            print(f"\nTOTAL GENERAL: ${TOTALIMP:.2f} en {CANSUC} sucursales.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar()
    