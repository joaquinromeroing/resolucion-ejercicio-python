def burbuja(arreglo):
    n = len(arreglo)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arreglo[j] > arreglo[j + 1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = temp
            j += 1
        i += 1
    return arreglo

def busqueda_binaria(arreglo, objetivo):
    izquierda = 0
    derecha = len(arreglo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arreglo[medio] == objetivo:
            return True
        elif arreglo[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return False

def main():
    Numeros = []
    
    print("Ingreso de Datos")
    while True:
        try:
            num = int(input("Ingrese un numero (1 a 100000, o 0 para salir): "))
            
            if num == 0:
                break
            elif 1 <= num <= 100000:
                Numeros.append(num)
            else:
                print("Error: El numero ingresado esta fuera del rango (1 a 100000).")
        except ValueError:
            print("Error: Ingrese un numero entero valido.")

    if len(Numeros) == 0:
        print("No se ingresaron numeros validos para procesar.")
        return

    burbuja(Numeros)

    print("\nBusqueda Binaria")
    try:
        buscar = int(input("Ingrese el numero que desea buscar: "))
        
        if busqueda_binaria(Numeros, buscar):
            print("Numero encontrado")
        else:
            print("Numero no encontrado")
    except ValueError:
         print("Error: Ingrese un numero entero valido para la busqueda.")

if __name__ == "__main__":
    main()