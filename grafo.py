import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from(
    [('Sumé', 'Congo'), ('Serra Branca' , 'Sumé'), 
    ('Sumé','Umbuzeiro'), ('Serra Branca' , 'Umbuzeiro')])

val_map = {'Sumé': 1.0,
           'Congo': 0.5714285714285714,
           'Umbuzeiro': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

nx.draw(G, cmap = plt.get_cmap('jet'), node_color = values)
plt.show()