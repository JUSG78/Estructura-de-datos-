class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamano(self):
        return len(self.items)
    
    def mostrar(self):
        if self.esta_vacia():
            return "[]"
        # Muestra el tope al inicio (arriba)
        return str(self.items[::-1])


def torres_hanoi(n, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar):
   
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")
        mostrar_estado(origen, auxiliar, destino)
        return
    
    # Mover n-1 discos del origen al auxiliar
    torres_hanoi(n-1, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino)
    
    # Mover el disco más grande al destino
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")
    mostrar_estado(origen, auxiliar, destino)
    
    # Mover los n-1 discos del auxiliar al destino
    torres_hanoi(n-1, auxiliar, destino, origen, nombre_auxiliar, nombre_destino, nombre_origen)


def mostrar_estado(origen, auxiliar, destino):

    print(f"Origen:  {origen.mostrar()}")
    print(f"Auxiliar: {auxiliar.mostrar()}")
    print(f"Destino: {destino.mostrar()}")
    print("-" * 40)


# Programa principal
if __name__ == "__main__":
    origen = Pila()
    auxiliar = Pila()
    destino = Pila()
    
    # Apilar discos en la torre origen (3 es el más grande)
    for disco in range(3, 0, -1):
        origen.apilar(disco)
    
    print("🔹 Estado inicial:")
    mostrar_estado(origen, auxiliar, destino)
    
    print("🔹 Pasos para resolver las Torres de Hanoi:\n")
    torres_hanoi(3, origen, destino, auxiliar, "Origen", "Destino", "Auxiliar")
    
    print("\n🔹 Estado final:")
    mostrar_estado(origen, auxiliar, destino)

