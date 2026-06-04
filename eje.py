def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def busqueda_binaria(lista, objetivo):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        med = (izq + der) // 2
        if lista[med] == objetivo:
            return True
        elif lista[med] < objetivo:
            izq = med + 1
        else:
            der = med - 1
    return False

def ejecutar():
    numeros = []
    while True:
        num = int(input("Ingrese número (1 a 100000) o 0 para terminar: "))
        if num == 0:
            break
        if 1 <= num <= 100000:
            numeros.append(num)
        else:
            print("Error: Fuera de rango.")

    if not numeros:
        return

    print("Original:", numeros)
    ordenados = ordenar_burbuja(numeros)
    print("Ordenado:", ordenados)

    buscar = int(input("Ingrese número a buscar: "))
    if busqueda_binaria(ordenados, buscar):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")

if __name__ == '__main__':
    ejecutar()