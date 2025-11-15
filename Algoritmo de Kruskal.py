class UnionFind:
    def __init__(self, nodos):
        self.padre = {nodo: nodo for nodo in nodos}
        self.rango = {nodo: 0 for nodo in nodos}
    
    def find(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.find(self.padre[nodo])
        return self.padre[nodo]
    
    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)
        if raiz_u != raiz_v:
            if self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            elif self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1

def kruskal(grafo):
    
    aristas = sorted(grafo)
    nodos = set()
    for _, u, v in aristas:
        nodos.add(u)
        nodos.add(v)
    uf = UnionFind(nodos)
    mst = []
    
    for peso, u, v in aristas:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, peso))
    
    return mst


grafo = [(1, 'A', 'B'), (2, 'B', 'C'), (3, 'A', 'C')]
print(kruskal(grafo))  
