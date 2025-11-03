class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def obtener_dato(self):
        return self.dato

    def establecer_siguiente(self, siguiente):
        self.siguiente = siguiente

    def obtener_siguiente(self):
        return self.siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.establecer_siguiente(self.cabeza)
        self.cabeza = nuevo_nodo

    def longitud(self):
        actual = self.cabeza
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.obtener_siguiente()
        return contador

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        if self.cabeza.obtener_dato() == dato:
            self.cabeza = self.cabeza.obtener_siguiente()
            return

        anterior = None
        actual = self.cabeza
        while actual is not None:
            if actual.obtener_dato() == dato:
                anterior.establecer_siguiente(actual.obtener_siguiente())
                return
            anterior = actual
            actual = actual.obtener_siguiente()

    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.obtener_dato() == dato:
                return actual
            actual = actual.obtener_siguiente()
        return None

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.obtener_dato())
            actual = actual.obtener_siguiente()

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

print(f"La lista tiene {lista.longitud()} elementos.")
lista.mostrar()

print("\nEliminando el elemento 20...")
lista.eliminar(20)
print(f"La lista tiene {lista.longitud()} elementos.")
lista.mostrar()

print("\nBuscando el elemento 30...")
nodo = lista.buscar(30)
if nodo:
    print(f"Encontrado: {nodo.obtener_dato()}")
else:
    print("Elemento no encontrado.")
