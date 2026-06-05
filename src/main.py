# Importamos las funciones del archivo vecino
from metodos import ordenamiento_burbuja, busqueda_binaria

def ejecutar_programa():
    Numeros = []
    
    print("--- Carga de Números (Ingrese 0 para terminar) ---")
    
    # 1. Carga de datos con validación
    while True:
        try:
            num = int(input("Ingrese un número entero (1 a 100000): "))
            
            if num == 0:
                break # Finaliza la carga
                
            if 1 <= num <= 100000:
                Numeros.append(num)
            else:
                print("Error: El número está fuera del rango permitido (1-100000).")
                
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

    # Verificar si el usuario cargó datos antes de continuar
    if not Numeros:
        print("No se ingresaron números válidos. Fin del programa.")
        return

    # 2. Ordenamiento utilizando Burbuja
    print("\nOrdenando el arreglo...")
    ordenamiento_burbuja(Numeros)
    print(f"Arreglo ordenado: {Numeros}") # Opcional: para que veas el resultado

    # 3. Búsqueda Binaria
    print("\n--- Búsqueda de un Número ---")
    try:
        buscar = int(input("Ingrese el número que desea buscar: "))
        
        # Ejecutar la búsqueda
        encontrado = busqueda_binaria(Numeros, buscar)
        
        # 4. Mostrar resultado exacto solicitado
        if encontrado:
            print("Numero encontrado")
        else:
            print("Numero no encontrado")
            
    except ValueError:
        print("Error: Entrada inválida. Se esperaba un número entero.")

if __name__ == "__main__":
    ejecutar_programa()
