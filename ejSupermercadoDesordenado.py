import pandas as pd

csvPath = input("Indique el path del csv:   ")
orderedRes = input("Su csv esta ordenado? Y/N   ")

df = pd.read_csv(csvPath)
columns = df.columns
df.dropna(inplace=True)

def orderCsv(df : pd.DataFrame):
    columns = ["PRSUC", "PRCOD", "PRFEC"]

    rows = df.to_dict(orient="records")

    length = len(rows)
    for i in range(length):
        for j in range(0, length - i - 1):
            swap = False
            for col in columns:
                if rows[j][col] > rows[j + 1][col]:
                    swap = True
                    break
                elif rows[j][col] < rows[j + 1][col]:
                    break
            if swap:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]

    df = pd.DataFrame(rows)
    sortedDf = pd.DataFrame(rows)
    sortedDf.to_csv(f"{csvPath}.ordenado", index=False)
    return df

class sellerPurchaseLot:
    def __init__(self, productCode, purchaseDate, seller, amount, price):
        self.productCode = productCode
        self.purchaseDate = purchaseDate
        self.seller = seller
        self.amount = amount
        self.price = price

class product:
    def __init__(self, code, totalPrice):
        self.code = code
        self.totalPrice = totalPrice

if (orderedRes == "n" or orderedRes == "N"):
    df = orderCsv(df)

i = 0
n = len(df)
franchiseAmount = 0
totalPriceAllFranchises = 0
while i < n:
    currentFranchiseCode = df.iloc[i]["PRSUC"]
    print(f"\nSucursal: {currentFranchiseCode}")
    totalFranchisePurchases = 0
    mostBoughtProduct = product(0, 0)
    leastBoughtProduct = product(0, 0)

    j = i
    while j < n and df.iloc[j]["PRSUC"] == currentFranchiseCode:
        currentProductCode = df.iloc[j]["PRCOD"]
        print(f"  Producto: {currentProductCode}")
        totalProductSales = 0
        totalProductPrice = 0

        k = j
        while k < n and df.iloc[k]["PRCOD"] == currentProductCode and df.iloc[k]["PRSUC"] == currentFranchiseCode:
            row = df.iloc[k]
            purchase = sellerPurchaseLot(
                productCode=row["PRCOD"],
                purchaseDate=row["PRFEC"],
                seller=row["PRPROV"],
                amount=int(row["PRCANT"]),
                price=float(row["PRPRE"])
            )
            totalProductSales += purchase.amount
            totalProductPrice += purchase.price
            totalFranchisePurchases += purchase.amount
            totalPriceAllFranchises += totalProductPrice
            k += 1

        if (totalProductPrice < leastBoughtProduct.totalPrice and totalProductPrice > 0) or leastBoughtProduct.totalPrice == 0:
            leastBoughtProduct.code = currentProductCode
            leastBoughtProduct.totalPrice = totalProductPrice

        if (totalProductPrice > mostBoughtProduct.totalPrice and totalProductPrice > 0) or mostBoughtProduct.totalPrice == 0:
            mostBoughtProduct.code = currentProductCode
            mostBoughtProduct.totalPrice = totalProductPrice

        print(f"    Total ventas: {totalProductSales}")
        print(f"    Total precio: ${totalProductPrice}")

        j = k

    print(f"       Total de productos comprados: {totalFranchisePurchases}")
    print(f"       Producto de mayor compra {mostBoughtProduct.code} con mayor importe ${mostBoughtProduct.totalPrice}")
    print(f"       Producto de menor compra {leastBoughtProduct.code} con menor importe ${leastBoughtProduct.totalPrice}")
    franchiseAmount += 1

    i = j

print(f"El supermercado tiene un total de {franchiseAmount} sucursales")
print(f"La compra total en pesos de todas las sucursales es de: ${totalPriceAllFranchises}")
