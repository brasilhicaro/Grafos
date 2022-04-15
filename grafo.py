import networkx as nx
import matplotlib.pyplot as plt
import pylab

G = nx.Graph()

G.add_edges_from([('Monteiro', 'Sertânia')], weight = 4)
G.add_edges_from([('Monteiro' , 'Sumé'), 
    ('Monteiro','Camalaú'), ('Monteiro', 'Zabelê')], weight = 3)
G.add_edges_from(
    [('São Sebastião do Umbuzeiro' , 'Zabelê'), ('Serra Branca','Sumé'),
    ('Congo', 'Sumé'), ('São José do Egito','Ouro Velho'), ('Ouro Velho', 'Prata'),
    ('Prata', 'Monteiro')], weight=2)

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
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
red_edges = [('Monteiro', 'Sertânia'), ('São José do Egito','Ouro Velho')]
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
pos=nx.spring_layout(G)

nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_color = values, node_size=900,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
pylab.show()
