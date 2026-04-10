import csv

# Funcion de burbuja
def Order_product(path):
    updated_lines = []

    with open(path, "r") as file:
        encabezado = file.readline() 

        for linea in file:
            updated_lines.append(linea.strip().split(","))

    n = len(updated_lines)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (updated_lines[j][0], updated_lines[j][1]) > (updated_lines[j + 1][0], updated_lines[j + 1][1]):
                updated_lines[j], updated_lines[j + 1] = updated_lines[j + 1], updated_lines[j]

    nuevo_path = "archivo_ordenado.csv"

    with open(nuevo_path, "w") as file:
        file.write(encabezado)
        for fila in updated_lines:
            file.write(",".join(fila) + "\n")
    
    return nuevo_path


# Logica de while
def analysis(path):
    canSuc = 0
    totalImp = 0

    with open(path, "r") as archivo:
        archivo.readline()
        linea = archivo.readline().strip()

        while linea != "":

            data = linea.split(",")

            sucActual = data[0]
            canSuc += 1

            totSuc = 0

            myImport = -1
            mnImport = float("inf")
            myProd = ""
            mnProd = ""

            while linea != "" and data[0] == sucActual:

                prodActual = data[1]

                totUni = 0
                totPes = 0

                while linea != "" and data[0] == sucActual and data[1] == prodActual:

                    cant = int(data[4])
                    prec = float(data[5])

                    totUni += cant
                    totPes += cant * prec
                    totSuc += cant
                    totalImp += cant * prec

                    linea = archivo.readline().strip()
                    if linea != "":
                        data = linea.split(",")

                print(f"Sucursal {sucActual} - Producto {prodActual}")
                print(f"  Total unidades: {totUni}")
                print(f"  Total pesos: {totPes}")

                # Mayor / menor
                if totPes > myImport:
                    myImport = totPes
                    myProd = prodActual

                if totPes < mnImport:
                    mnImport = totPes
                    mnProd = prodActual

            print("-----------------------------------")
            print(f"Sucursal: {sucActual}")
            print(f"Total Unidades: {totSuc}")
            print(f"Mayor producto: {myProd} - ${myImport}")
            print(f"Menor producto: {mnProd} - ${mnImport}")
            print("-----------------------------------")


        print("===================================")
        print(f"Total sucursales: {canSuc}")
        print(f"Total importe: ${totalImp}")
        print("===================================")

# Menu
def menu():
    path = input("Indique el path del csv: ")
    option = input("El archivo esta ordenado (Y/N): ")

    if option == "N":
        print("Ordenando archivo...")
        new_path = Order_product(path)
        analysis(new_path)

    else:
        print("Analizando archivo...")
        analysis(path)

if __name__ == "__main__":
    menu()