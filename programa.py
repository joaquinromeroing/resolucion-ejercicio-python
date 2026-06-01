from typing import List

def ordenar_burbuja(arr: List[int]) -> List[int]:
    n = len(arr)
    resultado = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    return resultado

def busqueda_binaria(arr: List[int], objetivo: int) -> bool:
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return True
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return False

def ejecutar_carga() -> List[int]:
    numeros = []
    print("--- Carga de Números Enteros (0 para finalizar) ---")
    
    while True:
        try:
            entrada = int(input("Ingrese un número entero (1 a 100000): "))
            
            if entrada == 0:
                break
                
            if 1 <= entrada <= 100000:
                numeros.append(entrada)
            else:
                print("Error: El número debe estar entre 1 y 100000 (o ser 0 para salir).")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            
    return numeros

if __name__ == "__main__":
    # 1. Carga de datos
    lista_numeros = ejecutar_carga()
    
    if not lista_numeros:
        print("No se ingresaron números válidos. Programa finalizado.")
    else:
        # 2. Ordenamiento
        numeros_ordenados = ordenar_burbuja(lista_numeros)
        print(f"Arreglo ordenado (Burbuja): {numeros_ordenados}")
        
        # 3. Búsqueda
        try:
            buscar = int(input("\nIngrese el número que desea buscar en el arreglo: "))
            encontrado = busqueda_binaria(numeros_ordenados, buscar)
            
            if encontrado:
                print("Número encontrado")
            else:
                print("Número no encontrado")
        except ValueError:
            print("Entrada inválida. Se esperaba un número entero.")