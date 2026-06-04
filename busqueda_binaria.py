import unittest

 
def cargar_numeros():
    numeros = []
    print("Ingrese números entre 1 y 100000. Ingrese 0 para terminar.\n")
    while True:
        entrada = input("Ingrese un número: ")
        try:
            numero = int(entrada)
        except ValueError:
            print("Error: ingrese un valor numérico entero.")
            continue
 
        if numero == 0:
            break
        elif 1 <= numero <= 100000:
            numeros.append(numero)
        else:
            print(f"Error: {numero} está fuera del rango permitido (1-100000).")
 
    return numeros
 
 
def ordenar_burbuja(arreglo):
    arr = arreglo[:]          
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
 
 
def busqueda_binaria(arreglo, objetivo):
    izq, der = 0, len(arreglo) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if arreglo[mid] == objetivo:
            return mid
        elif arreglo[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1

 
def main():
    numeros = cargar_numeros()
 
    if not numeros:
        print("\nNo se ingresaron números. Fin del programa.")
        return
 
    print(f"\nNúmeros ingresados: {numeros}")
 
    numeros_ordenados = ordenar_burbuja(numeros)
    print(f"Números ordenados: {numeros_ordenados}")
 
    try:
        buscar = int(input("\nIngrese el número a buscar: "))
    except ValueError:
        print("Valor inválido.")
        return
 
    indice = busqueda_binaria(numeros_ordenados, buscar)
    if indice != -1:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()