import networkx as nx
import matplotlib.pyplot as plt

n = 10
k = 3

G = nx.random_regular_graph(k, n)

num_arestas = G.number_of_edges()

nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=15, font_color='black')
plt.title(f"Grafo {k}-regular com {n} vértices")
plt.show()

num_arestas
print(num_arestas)