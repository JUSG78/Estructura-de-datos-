import heapq

def dijkstra(grafo, origen):
    
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    cola = [(0, origen)]  
    visitados = set()
    
    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)
       
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        
        for vecino, peso in grafo.get(nodo_actual, []):
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))
    
    return distancias


grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1)],
    'C': []
}
print(dijkstra(grafo, 'A')) 