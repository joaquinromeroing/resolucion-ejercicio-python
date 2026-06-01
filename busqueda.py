from os import read


def InputValues():
    input_value = input("Ingrese un numero entre 1 y 100.000: ")
    if input_value == "0":
        print("Ingreso de numeros finalizado.")
        return False
    return input_value

def validate_input(input_value):
    if input_value.isdigit():
        number = int(input_value)
        if 1 <= number <= 100000:
            return number
    return None

def handle_message(number):
    if number is not None:
        print(f"El numero ingresado es: {number}")
    else:
        print("Entrada no valida. Por favor, ingrese un numero entre 1 y 100.000.")

def dicotomic_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def handle_search_result(result):
    if result != -1:
        print(f"El numero se encuentra en la posicion: {result}")
    else:
        print("El numero no se encuentra en el arreglo.")

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def main():
    numeros = []
    while True:
        input_value = InputValues()
        if input_value is False:
            break
        number = validate_input(input_value)
        handle_message(number)
        if number is not None:
            numeros.append(number)
    print("Numeros ingresados:", numeros)
    bubble_sort(numeros)
    print("Numeros ordenados:", numeros)

    search_number = int(InputValues())
    result = dicotomic_search(numeros, search_number)
    handle_search_result(result)

if __name__ == "__main__":
    main()
