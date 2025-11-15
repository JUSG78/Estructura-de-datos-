def warshall(grafo):
  
    nodos = list(grafo.keys())
    alcance = {i: {j: (j in grafo.get(i, set())) for j in nodos} for i in nodos}
    
    for i in nodos:
        alcance[i][i] = True
    
    for k in nodos:
        for i in nodos:
            for j in nodos:
                if alcance[i][k] and alcance[k][j]:
                    alcance[i][j] = True
    
    return alcance


grafo = {
    'A': {'B'},
    'B': {'C'},
    'C': set()
}
print(warshall(grafo))  