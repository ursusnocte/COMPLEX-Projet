from main import *



if __name__ == "__main__":
    # Création d'un graphe
    g = Graph(9)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 8)
    g.add_edge(8, 4)
    g.add_edge(4, 5)

    # Affichage du graphe
    print("Graphe initial:")
    g.print()

    # Suppression d'un sommet
    g.remove_vertex(0)

    # Affichage du graphe après suppression
    print("Graphe après suppression du sommet 0:")
    g.print()

    # Suppression de plusieurs sommets
    g.remove_vertices([8, 2])

    # Affichage du graphe après suppression
    print("Graphe après suppression des sommets 8 et 2:")
    g.print()

    # Test graphe aléatoire
    print("Graphe aléatoire:")
    g_random = gen_alea_graph(9, 0.3)
    g_random.print()