def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


def main():
    Numeros = []

    print("Ingrese numeros enteros entre 1 y 100000. Ingrese 0 para finalizar.")

    while True:
        try:
            numero = int(input("Ingrese un numero: "))
        except ValueError:
            print("Error: debe ingresar un numero entero.")
            continue

        if numero == 0:
            break
        elif 1 <= numero <= 100000:
            Numeros.append(numero)
        else:
            print("Error: el numero debe estar entre 1 y 100000.")

    if not Numeros:
        print("No se ingresaron numeros.")
        return

    bubble_sort(Numeros)
    print(f"\nArreglo ordenado: {Numeros}")

    try:
        buscar = int(input("\nIngrese el numero a buscar: "))
    except ValueError:
        print("Error: debe ingresar un numero entero.")
        return

    resultado = binary_search(Numeros, buscar)

    if resultado != -1:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()
