def floyd_warshall(grafo):
   
    nodos = list(grafo.keys())
    dist = {i: {j: float('inf') for j in nodos} for i in nodos}
    
    for i in nodos:
        dist[i][i] = 0
        for j, peso in grafo.get(i, {}).items():
            dist[i][j] = peso
    
    for k in nodos:
        for i in nodos:
            for j in nodos:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2},-
    'C': {}
}
print(floyd_warshall(grafo))  # {'A': {'A': 0, 'B': 1, 'C': 3}, 'B': {'A': inf, 'B': 0, 'C': 2}, 'C': {'A': inf, 'B': inf, 'C': 0}}