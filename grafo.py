import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([('Monteiro', 'Sertânia')],)
G.add_edges_from(
        [('Monteiro' , 'Sumé'), 
    ('Monteiro','Camalaú'), ('Monteiro', 'Zabelê'),])
G.add_edges_from(
    [('São Sebastião do Umbuzeiro' , 'Zabelê'), ('Serra Branca','Sumé'),
    ('Congo', 'Sumé'), ('São José do Egito','Ouro Velho'), ('Ouro Velho', 'Prata'),
    ('Prata', 'Monteiro')])

val_map = {'Monteiro': 0.6,
           'Sertânia': 0.9,
           'Camalaú': 0.8,
           'Sumé': 0.7,
            'Zabelê':1.0,
            'São Sebastião do Umbuzeiro': 0.5,
            'Serra Branca': 0.4,
            'Congo': 0.3,
            'São José do Egito': 0.2
            }

values = [val_map.get(node, 0.25) for node in G.nodes()]

nx.draw(G, cmap = plt.get_cmap('jet'), node_color = values)
plt.show()
