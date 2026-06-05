class BusquedaBinaria:

    def __init__(self):
        self.Numeros = []

    def ingresar_numeros(self):
        while True:
            try:
                numero = int(input("Ingrese un número (0 para finalizar): "))
            except ValueError:
                print("Error: ingrese un número entero válido.")
                continue

            if numero == 0:
                break
            elif 1 <= numero <= 100000:
                self.Numeros.append(numero)
            else:
                print("Error: el número debe estar entre 1 y 100000.")

    def ordenar_burbuja(self, lista):
        arr = lista[:]
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def busqueda_binaria(self, lista, objetivo):
        izquierda = 0
        derecha = len(lista) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if lista[medio] == objetivo:
                return medio
            elif lista[medio] < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return -1

    def ejecutar(self):
        self.ingresar_numeros()

        if not self.Numeros:
            print("No se ingresaron números.")
            return

        self.Numeros = self.ordenar_burbuja(self.Numeros)
        print(f"Números ordenados: {self.Numeros}")

        try:
            objetivo = int(input("Ingrese el número a buscar: "))
        except ValueError:
            print("Error: ingrese un número entero válido.")
            return

        resultado = self.busqueda_binaria(self.Numeros, objetivo)

        if resultado != -1:
            print("Numero encontrado")
            print(f"Posición: {resultado}")
        else:
            print("Numero no encontrado")


if __name__ == "__main__":
    app = BusquedaBinaria()
    app.ejecutar()
