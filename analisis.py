import pandas as pd

df = pd.read_csv("COMPRAS_supermercado_ordenado.csv")

#por prod
i = 0

while i < len(df):
    suc = df["PRSUC"][i]
    prod = df["PRCOD"][i]

    totuni = 0
    totpes = 0

    while i < len(df) and df["PRSUC"][i] == suc and df["PRCOD"][i] == prod:
        totuni = totuni + df["PRCANT"][i]
        totpes = totpes + df["PRCANT"][i] * df["PRPRE"][i]
        i = i + 1

    print("Sucursal:", suc, "| Producto:", prod, "| Unidades:", totuni, "| Total $:", totpes)
    print("")


#por suc

i = 0

while i < len(df):
    suc = df["PRSUC"][i]

    totsuc = 0
    myprod = ""
    myimpor = 0
    mnprod = ""
    mnimpor = 999999999

    while i < len(df) and df["PRSUC"][i] == suc:
        prod = df["PRCOD"][i]

        totuni = 0
        totpes = 0

        while i < len(df) and df["PRSUC"][i] == suc and df["PRCOD"][i] == prod:
            totuni = totuni + df["PRCANT"][i]
            totpes = totpes + df["PRCANT"][i] * df["PRPRE"][i]
            i = i + 1

        totsuc = totsuc + totuni

        if totpes > myimpor:
            myimpor = totpes
            myprod = prod

        if totpes < mnimpor:
            mnimpor = totpes
            mnprod = prod

    print("Sucursal:", suc)
    print("Total unidades:", totsuc)
    print("Mayor producto:", myprod, "| Importe:", myimpor)
    print("Menor producto:", mnprod, "| Importe:", mnimpor)
    print("")


#totales
i = 0
cansuc = 0
totalimp = 0

while i < len(df):
    suc = df["PRSUC"][i]
    cansuc = cansuc + 1

    while i < len(df) and df["PRSUC"][i] == suc:
        totalimp = totalimp + df["PRCANT"][i] * df["PRPRE"][i]
        i = i + 1

print("Cantidad de sucursales:", cansuc)
print("Total general $:", totalimp)