class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.elementos.pop()
        else:
            return None

    def isEmpty(self):
        return self.elementos == []

def menu():
    pila = Pila()
    while True:
        print("\nOpciones disponibles:")
        print("1. Insertar un nuevo número entero")
        print("2. Eliminar el último elemento")
        print("3. Comprobar si la pila está vacía")
        print("4. Mostrar todos los elementos de la pila")
        print("5. Terminar programa")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            entrada = input("Introduce un número entero para insertar: ")
            try:
                numero = int(entrada)
                pila.push(numero)
                print(f"Número {numero} insertado correctamente.")
            except ValueError:
                print("Error: Debes ingresar un número entero válido.")
        elif opcion == '2':
            elemento = pila.pop()
            if elemento is None:
                print("La pila está vacía, no hay elementos para eliminar.")
            else:
                print(f"Elemento '{elemento}' eliminado de la pila.")
        elif opcion == '3':
            if pila.isEmpty():
                print("La pila está vacía.")
            else:
                print("La pila contiene elementos.")
        elif opcion == '4':
            print("Contenido actual de la pila:", pila.elementos)
        elif opcion == '5':
            print("Finalizando el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor intenta nuevamente.")

if __name__ == "__main__":
    menu()
