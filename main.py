# Jules Perrin de Brichambaut & Louiza Chenaoui
# COMPLEX - Projet Couverture de graphes
 
from random import random

class Graph:
    # Representation d'un graphe par des listes d'adjacences
    def __init__(self, vertices):
        """
        Entrée : liste de sommets
        Sortie : graphe
        """
        self.V = set(vertices)  # Nombre de sommets
        self.adj = {v: [] for v in vertices}  # Listes d'adjacences

    def print(self):
        for i in self.V:
            print(f"{i}: {self.adj[i]}")

        print("Listes des sommets :", self.V)

    def add_edge(self, u, v):
        if u in self.V and v in self.V and v not in self.adj[u]:
            self.adj[u].append(v)
            self.adj[v].append(u)

    def remove_edge(self, u, v):
        if u in self.V and v in self.V and v in self.adj[u]:
            self.adj[u].remove(v)
            self.adj[v].remove(u)

    def get_neighbors(self, v):
        return self.adj[v]
    
    def remove_vertex(self, v):
        for neighbor in self.adj[v]:
            self.adj[neighbor].remove(v)
        self.adj[v] = []
        self.V.remove(v)

    def remove_vertices(self, vertices):
        for v in vertices:
            self.remove_vertex(v)

    def add_vertex(self, v):
        if v not in self.V:
            self.V.add(v)
            self.adj[v] = []

    def degree(self, v):
        return len(self.adj[v])
    


def get_degrees(graph):
    return [graph.degree(v) for v in range(graph.V)]

def get_max_degree_vertex(graph):
    degrees = get_degrees(graph)
    max_degree = max(degrees)
    return degrees.index(max_degree), max_degree

def gen_alea_graph(n, p):
    g = Graph(list(range(n)))
    for i in range(n):
        for j in range(i + 1, n):
            if random() < p:
                g.add_edge(i, j)
    return g

def algo_couplage(G):
    """ 
    Entrée : un graphe G
    Sortie : une couverture de G
    """
    C = set()
    for i in range(len(G.V)):
        if i not in C:
            for j in G.get_neighbors(i):
                if j not in C:
                    C.add(i)
                    C.add(j)
                    break
    return C


#TODO : vérifier que l'algo glouton fonctionne
def algo_glouton(G):
    """
    Entrée : un graphe G
    Sortie : une couverture de G
    """
    C = set()
    g = Graph(list(G.V))
    g.adj = {v: list(G.adj[v]) for v in G.V}  # Copier les listes d'adjacences

    while g.V:
        u, deg = get_max_degree_vertex(g)
        if deg == 0:
            break
        v = g.get_neighbors(u)[0]
        C.add(u)
        C.add(v)
        g.remove_vertex(u)
        g.remove_vertex(v)

    return C