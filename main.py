# Jules Perrin de Brichambaut & Louiza Chenaoui
# COMPLEX - Projet Couverture de graphes
 
from random import random

class Graph:
    # Representation d'un graphe par des listes d'adjacences
    def __init__(self, vertices):
        self.V = vertices  # Nombre de sommets
        self.adj = [[] for _ in range(vertices)]  # Listes d'adjacences

    def print(self):
        for i in range(self.V):
            print(f"{i}: {self.adj[i]}")

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def remove_edge(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def get_neighbors(self, v):
        return self.adj[v]
    
    def remove_vertex(self, v):
        for neighbor in self.adj[v]:
            self.adj[neighbor].remove(v)
        self.adj[v] = []

    def remove_vertices(self, vertices):
        for v in vertices:
            self.remove_vertex(v)

    def degree(self, v):
        return len(self.adj[v])
    


def get_degrees(graph):
    return [graph.degree(v) for v in range(graph.V)]

def get_max_degree_vertex(graph):
    degrees = get_degrees(graph)
    max_degree = max(degrees)
    return degrees.index(max_degree), max_degree

def gen_alea_graph(n, p):
    g = Graph(n)
    for i in range(n):
        for j in range(i + 1, n):
            if random() < p:
                g.add_edge(i, j)
    return g