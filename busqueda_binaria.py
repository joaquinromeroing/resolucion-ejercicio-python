def ordenamiento_burbuja(numeros):
    if not numeros:
        return numeros
    
    n = len(numeros)
    arreglo = numeros.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    
    return arreglo


def busqueda_binaria(numeros, numero_buscado):
    izquierda = 0
    derecha = len(numeros) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if numeros[medio] == numero_buscado:
            return True
        elif numeros[medio] < numero_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return False


def ingresar_numeros():
    Numeros = []
    
    while True:
        try:
            numero = int(input("Ingrese un número (1 a 100000) o 0 para terminar: "))
            
            if numero == 0:
                break
            
            if numero < 1 or numero > 100000:
                print("Error: El número debe estar entre 1 y 100000. Intente nuevamente.")
                continue
            
            Numeros.append(numero)
            print(f"Número {numero} agregado correctamente.")
            
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    
    return Numeros


def main():
    print("=" * 60)
    print("ALGORITMO DE BÚSQUEDA BINARIA CON ORDENAMIENTO BURBUJA")
    print("=" * 60)
    print()
    
    print("Paso 1: Ingresar números (1 a 100000)")
    print("Ingrese 0 para terminar la carga.")
    print()
    Numeros = ingresar_numeros()
    
    if not Numeros:
        print("\nError: No se ingresaron números válidos.")
        return
    
    print(f"\nNúmeros ingresados: {Numeros}")
    print()
    
    print("Paso 2: Ordenando números con método Burbuja...")
    Numeros_Ordenados = ordenamiento_burbuja(Numeros)
    print(f"Números ordenados: {Numeros_Ordenados}")
    print()
    
    print("Paso 3: Búsqueda Binaria")
    try:
        numero_a_buscar = int(input("Ingrese el número a buscar: "))
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return
    
    print()
    
    encontrado = busqueda_binaria(Numeros_Ordenados, numero_a_buscar)
    
    if encontrado:
        print("Numero encontrado")
    else:
        print("Numero no encontrado")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
