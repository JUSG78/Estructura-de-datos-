class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pila = []
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.pila.append(elemento)
            self.tope += 1
            print(f"Insertar {elemento}: {self.pila} (TOPE={self.tope})")
        else:
            print("Error: Desbordamiento de pila")

    def eliminar(self):
        if self.tope > 0:
            elemento = self.pila.pop()
            self.tope -= 1
            print(f"Eliminar {elemento}: {self.pila} (TOPE={self.tope})")
        else:
            print("Error: Subdesbordamiento de pila")

# Inicialización de la pila
pila = Pila(capacidad=8)

# Operaciones
pila.insertar('X')
pila.insertar('Y')
pila.eliminar()
pila.eliminar()
pila.eliminar()  # Este debería generar un error de subdesbordamiento
pila.insertar('V')
pila.insertar('W')
pila.eliminar()
pila.insertar('R')

# Estado final de la pila
print(f"Elementos finales en la pila: {pila.pila} (TOPE={pila.tope})")
