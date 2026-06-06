def ordenar_burbuja(numeros):
    lista = numeros.copy()
    n = len(lista)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def busqueda_binaria(numeros, objetivo):
    izquierda = 0
    derecha = len(numeros) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if numeros[medio] == objetivo:
            return True
        elif numeros[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False


def cargar_numeros():
    Numeros = []

    print("Ingrese numeros entre 1 y 100000. Ingrese 0 para finalizar.")

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
            print(f"Error: el numero {numero} esta fuera del rango permitido (1 a 100000).")

    return Numeros


def main():
    Numeros = cargar_numeros()

    if not Numeros:
        print("No se ingresaron numeros.")
        return

    Numeros = ordenar_burbuja(Numeros)
    print(f"\nNumeros ordenados: {Numeros}")

    try:
        buscar = int(input("\nIngrese el numero a buscar: "))
    except ValueError:
        print("Error: debe ingresar un numero entero.")
        return

    if busqueda_binaria(Numeros, buscar):
        print("Numero encontrado")
    else:
        print("Numero no encontrado")


if __name__ == "__main__":
    main()
