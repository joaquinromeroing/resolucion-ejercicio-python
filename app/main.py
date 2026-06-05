from algorithms import bubble_sort, binary_search

Numeros = []

print("Ingrese números enteros entre 1 y 100000. Ingrese 0 para finalizar.")

while True:
    try:
        number = int(input("Número: "))
    except ValueError:
        print("Error: ingrese un número entero válido.")
        continue

    if number == 0:
        break
    elif 1 <= number <= 100000:
        Numeros.append(number)
    else:
        print("Error: el número debe estar entre 1 y 100000.")

if not Numeros:
    print("No se ingresaron números.")
else:
    Numeros = bubble_sort(Numeros)
    print(f"\nArreglo ordenado: {Numeros}")

    try:
        target = int(input("\nIngrese el número a buscar: "))
    except ValueError:
        print("Error: ingrese un número entero válido.")
    else:
        index = binary_search(Numeros, target)
        if index != -1:
            print("Numero encontrado")
        else:
            print("Numero no encontrado")
