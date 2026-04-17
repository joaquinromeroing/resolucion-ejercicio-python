import pandas as pd

df = pd.read_csv("COMPRAS_supermercado(in).csv")
columns = df.columns
df.dropna()

class sellerPurchaseLot:
    def __init__(self, productCode, purchaseDate, seller, amount, price):
        self.productCode = productCode
        self.purchaseDate = purchaseDate
        self.seller = seller
        self.amount = amount
        self.price = price
class product:
    def __init__(self, code, totalPrice):
        self.code = code,
        self.totalPrice = totalPrice
        
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
            purchase = sellerPurchaseLot(productCode=row["PRCOD"], purchaseDate=row["PRFEC"], seller=row["PRPROV"], amount=int(row["PRCANT"]), price=float(row["PRPRE"]))
            totalProductSales += purchase.amount
            totalProductPrice += purchase.price
            totalFranchisePurchases += purchase.amount
            totalPriceAllFranchises += totalProductPrice
            k += 1
        if (totalProductPrice < leastBoughtProduct.totalPrice and totalProductPrice > 0 or leastBoughtProduct.totalPrice == 0):
            leastBoughtProduct.code = currentProductCode
            leastBoughtProduct.totalPrice = totalProductPrice

        if (totalProductPrice > mostBoughtProduct.totalPrice and totalProductPrice > 0 or mostBoughtProduct.totalPrice == 0):
            mostBoughtProduct.code = currentProductCode
            mostBoughtProduct.totalPrice = totalProductPrice

        print(f"    Total ventas: {totalProductSales}")
        print(f"    Total precio: ${totalProductPrice}")

        j = k
    print (f"       Total de productos comprados: {totalFranchisePurchases}")
    print (f"       Producto de mayor compra {mostBoughtProduct.code} con mayor importe ${mostBoughtProduct.totalPrice}")
    print (f"       Producto de menor compra {leastBoughtProduct.code} con menor importe ${leastBoughtProduct.totalPrice}")
    franchiseAmount += 1

    i = j

print (f"El supermercado tiene un total de {franchiseAmount} sucursales")
print (f"La compra total en pesos de todas las sucursales es de: ${totalPriceAllFranchises}")

with open("/output/salida.txt", "w") as f:
    f.write(f"El supermercado tiene un total de {franchiseAmount} sucursales\n")
    f.write(f"La compra total en pesos de todas las sucursales es de: ${totalPriceAllFranchises}\n")
