class AlgoritmosOrdenamiento:
    """Clase que contiene algoritmos de ordenamiento"""
    
    @staticmethod
    def burbuja(numeros):
        """
        Ordena un arreglo usando el método de Burbuja (Bubble Sort)
        Args:
            numeros: lista de números a ordenar
        Returns:
            lista ordenada
        """
        arr = numeros.copy()
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr


class AlgoritmosBusqueda:
    """Clase que contiene algoritmos de búsqueda"""
    
    @staticmethod
    def busqueda_binaria(numeros, objetivo):
        """
        Busca un número en un arreglo ordenado usando Búsqueda Binaria
        Args:
            numeros: lista ordenada de números
            objetivo: número a buscar
        Returns:
            índice del número si existe, -1 si no existe
        """
        izquierda = 0
        derecha = len(numeros) - 1
        
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            
            if numeros[medio] == objetivo:
                return medio
            elif numeros[medio] < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        
        return -1


def ingresar_numeros():
    """
    Función principal que solicita números al usuario
    Returns:
        lista de números válidos ingresados
    """
    numeros = []
    
    print("=" * 50)
    print("INGRESO DE NÚMEROS")
    print("=" * 50)
    
    while True:
        try:
            num = int(input("\nIngrese un número (1-100000) o 0 para finalizar: "))
            
            if num == 0:
                if len(numeros) == 0:
                    print("❌ Debe ingresar al menos un número.")
                    continue
                break
            
            if num < 1 or num > 100000:
                print(f"❌ Error: {num} está fuera de rango. Ingrese un número entre 1 y 100000.")
                continue
            
            numeros.append(num)
            print(f"✅ Número {num} agregado. Total: {len(numeros)}")
        
        except ValueError:
            print("❌ Error: Ingrese un número válido.")
    
    return numeros


def buscar_numero(numeros_ordenados):
    """
    Función que solicita un número para buscar
    Args:
        numeros_ordenados: lista de números ordenados
    """
    buscador = AlgoritmosBusqueda()
    
    print("\n" + "=" * 50)
    print("BÚSQUEDA BINARIA")
    print("=" * 50)
    
    try:
        numero_buscar = int(input("\nIngrese el número a buscar: "))
        resultado = buscador.busqueda_binaria(numeros_ordenados, numero_buscar)
        
        if resultado != -1:
            print(f"\n✅ Numero encontrado en índice {resultado}")
        else:
            print(f"\n❌ Numero no encontrado")
    
    except ValueError:
        print("❌ Error: Ingrese un número válido.")


def main():
    """Función principal del programa"""
    
    print("\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " " * 48 + "║")
    print("║" + "  BÚSQUEDA BINARIA CON UNIT TESTING  ".center(48) + "║")
    print("║" + " " * 48 + "║")
    print("╚" + "=" * 48 + "╝")
    
    # Ingresar números
    numeros = ingresar_numeros()
    
    # Ordenar números
    ordenador = AlgoritmosOrdenamiento()
    numeros_ordenados = ordenador.burbuja(numeros)
    
    print("\n" + "=" * 50)
    print("NÚMEROS ORDENADOS")
    print("=" * 50)
    print(f"Original: {numeros}")
    print(f"Ordenado: {numeros_ordenados}")
    
    # Buscar número
    buscar_numero(numeros_ordenados)


if __name__ == "__main__":
    main()
