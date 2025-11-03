import bisect  # Para búsqueda binaria eficiente en la lista ordenada

# Estructura global: lista de [nombre_postre, lista_ingredientes]
postres = [
    ["Flan", ["leche", "huevos", "azúcar"]],
    ["Tiramisu", ["café", "mascarpone", "bizcochos"]],
    ["Tiramisu", ["café", "mascarpone", "bizcochos", "cacao"]],  # Ejemplo de duplicado para el punto 2
    ["Zanahoria", ["zanahoria", "harina", "huevos"]]
]

# Función auxiliar: Buscar un postre por nombre (búsqueda binaria, ya que la lista está ordenada)
def buscar_postre(nombre):
    # Ordenar la lista por nombre antes de buscar (para mantener consistencia)
    postres.sort(key=lambda x: x[0])
    nombres = [p[0] for p in postres]
    idx = bisect.bisect_left(nombres, nombre)
    if idx < len(nombres) and nombres[idx] == nombre:
        return idx
    return -1

# Función auxiliar: Imprimir la estructura completa (para depuración)
def imprimir_postres():
    print("Estructura actual de POSTRES:")
    for p in postres:
        print(f"  {p[0]}: {p[1]}")
    print()

# a. Dado el nombre de un postre, imprimir la lista de todos sus ingredientes.
def imprimir_ingredientes(nombre):
    idx = buscar_postre(nombre)
    if idx == -1:
        print(f"Error: El postre '{nombre}' no existe en la estructura.")
        return
    ingredientes = postres[idx][1]
    if not ingredientes:
        print(f"El postre '{nombre}' no tiene ingredientes registrados.")
    else:
        print(f"Ingredientes de '{nombre}': {ingredientes}")

# b. Dado el nombre de un postre, insertar nuevos ingredientes a su correspondiente lista.
def insertar_ingredientes(nombre, nuevos_ingredientes):
    if not isinstance(nuevos_ingredientes, list) or not nuevos_ingredientes:
        print("Error: Debe proporcionar una lista no vacía de nuevos ingredientes.")
        return
    idx = buscar_postre(nombre)
    if idx == -1:
        print(f"Error: El postre '{nombre}' no existe. No se pueden insertar ingredientes.")
        return
    # Agregar solo si no están ya en la lista (evitar duplicados en la lista de un postre)
    for ing in nuevos_ingredientes:
        if ing not in postres[idx][1]:
            postres[idx][1].append(ing)
    print(f"Ingredientes insertados en '{nombre}'. Lista actual: {postres[idx][1]}")

# c. Dado el nombre de un postre, elimine alguno de sus ingredientes.
def eliminar_ingrediente(nombre, ingrediente_a_eliminar):
    if not ingrediente_a_eliminar:
        print("Error: Debe proporcionar un ingrediente válido a eliminar.")
        return
    idx = buscar_postre(nombre)
    if idx == -1:
        print(f"Error: El postre '{nombre}' no existe.")
        return
    if ingrediente_a_eliminar not in postres[idx][1]:
        print(f"Error: El ingrediente '{ingrediente_a_eliminar}' no está en la lista de '{nombre}'.")
        return
    postres[idx][1].remove(ingrediente_a_eliminar)
    print(f"Ingrediente '{ingrediente_a_eliminar}' eliminado de '{nombre}'. Lista actual: {postres[idx][1]}")

# d. Dar de alta un postre con todos sus ingredientes.
def alta_postre(nombre, ingredientes):
    if not nombre or not isinstance(ingredientes, list):
        print("Error: Debe proporcionar un nombre válido y una lista de ingredientes.")
        return
    idx = buscar_postre(nombre)
    if idx != -1:
        print(f"Error: El postre '{nombre}' ya existe. No se puede dar de alta.")
        return
    # Insertar en la posición correcta para mantener orden alfabético
    postres.append([nombre, ingredientes])
    postres.sort(key=lambda x: x[0])
    print(f"Postre '{nombre}' dado de alta con ingredientes: {ingredientes}")

# e. Dar de baja un postre con todos sus ingredientes.
def baja_postre(nombre):
    if not nombre:
        print("Error: Debe proporcionar un nombre válido.")
        return
    idx = buscar_postre(nombre)
    if idx == -1:
        print(f"Error: El postre '{nombre}' no existe.")
        return
    eliminado = postres.pop(idx)
    print(f"Postre '{eliminado[0]}' dado de baja. Ingredientes eliminados: {eliminado[1]}")

# 2. Subprograma que elimina de manera automática a todos los elementos repetidos de la estructura “POSTRES”.
def eliminar_duplicados():
    # Usar un diccionario para eliminar duplicados basados en el nombre (mantiene la primera ocurrencia)
    vistos = {}
    for p in postres:
        nombre = p[0]
        if nombre not in vistos:
            vistos[nombre] = p[1]  # Guardar la lista de ingredientes de la primera ocurrencia
    # Reconstruir la lista ordenada
    global postres
    postres = [[nombre, ingredientes] for nombre, ingredientes in sorted(vistos.items())]
    print("Duplicados eliminados. Estructura actualizada.")

# Ejemplo de uso (puedes modificar o agregar más llamadas)
if __name__ == "__main__":
    imprimir_postres()
    
    # Ejemplos de cada punto
    imprimir_ingredientes("Tiramisu")  # a. Existe
    imprimir_ingredientes("NoExiste")  # a. No existe
    
    insertar_ingredientes("Flan", ["vainilla"])  # b. Agregar a existente
    insertar_ingredientes("NoExiste", ["algo"])  # b. No existe
    
    eliminar_ingrediente("Flan", "vainilla")  # c. Eliminar existente
    eliminar_ingrediente("Flan", "noexiste")  # c. Ingrediente no existe
    
    alta_postre("Arroz con Leche", ["arroz", "leche", "canela"])  # d. Nuevo
    alta_postre("Flan", ["duplicado"])  # d. Ya existe
    
    baja_postre("Zanahoria")  # e. Eliminar existente
    baja_postre("NoExiste")  # e. No existe
    
    imprimir_postres()
    
    # Punto 2: Eliminar duplicados
    eliminar_duplicados()
    imprimir_postres()
