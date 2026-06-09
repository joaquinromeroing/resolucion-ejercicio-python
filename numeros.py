def burbuja(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def busqueda_binaria(arr, objetivo):
    izq, der = 0, len(arr) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1


def cargar_numeros():
    Numeros = []
    while True:
        try:
            n = int(input("Ingrese un numero (0 para terminar): "))
        except ValueError:
            print("Error: ingrese un numero entero valido.")
            continue

        if n == 0:
            break
        elif 1 <= n <= 100000:
            Numeros.append(n)
        else:
            print(f"Error: el numero {n} esta fuera del rango permitido (1 a 100000).")

    return Numeros


def main():
    Numeros = cargar_numeros()

    if not Numeros:
        print("No se ingresaron numeros.")
        return

    burbuja(Numeros)
    print(f"\nArreglo ordenado: {Numeros}")

    try:
        buscar = int(input("\nIngrese un numero a buscar: "))
    except ValueError:
        print("Error: ingrese un numero entero valido.")
        return

    indice = busqueda_binaria(Numeros, buscar)

    if indice != -1:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()
