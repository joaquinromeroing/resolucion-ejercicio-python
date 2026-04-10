import pandas as pd

df = pd.read_csv('Compras.csv')
i = 0 
j = 0
Ca = 0
impT = 0
numSuc = 0
TotalImp = 0
Mayor = 0
Menor = 0
CantxSuc = 0
while  i < len(df):
    Ca = 0
    impT = 0
    numSuc += 1
    CantxSuc = 0
    su = df['PRSUC'][i]
    print(f"Sucursal: {su}")
    while i < len(df) and df['PRSUC'][i] == su:
        pr = df['PRCOD'][i]
        while i < len(df) and df['PRCOD'][i] == pr:
            Ca += df['PRCANT'][i]
            impT = round(impT + (df['PRCANT'][i] * df['PRPRE'][i]), 2)
            TotalImp = round(TotalImp + (df['PRCANT'][i] * df['PRPRE'][i]), 2)
            CantxSuc += df['PRCANT'][i]
            i += 1 
        if impT > Mayor:
            Mayor = impT
            MyPR = pr
        if impT < Menor or Menor == 0:
            Menor = impT
            MnPR = pr    
        print(f"Producto: {pr} - Cantidad: {Ca} - Importe Total: {impT}")
        Ca = 0
        impT = 0
    print(f"Cantidad x Sucursal: {CantxSuc}")
    print(f"Producto con mayor importe: {MyPR}, y su importe es: {Mayor}")
    print(f"Producto con menor importe: {MnPR}, y su importe es: {Menor}")

print(f"Cantidad Total: {numSuc}")
print(f"Total Importe: {TotalImp}")