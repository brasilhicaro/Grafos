import networkx as nx
import matplotlib.pyplot as plt
import pylab

G = nx.Graph()

G.add_edges_from([('Monteiro', 'Sertânia')])
G.add_edges_from([('Monteiro' , 'Sumé'), ('Monteiro','Camalaú'), ('Monteiro', 'Zabelê')])
G.add_edges_from([('São Sebastião do Umbuzeiro' , 'Zabelê')
,('Serra Branca','Sumé'),('Congo', 'Sumé'), ('São José do Egito','Ouro Velho')
, ('Ouro Velho', 'Prata'), ('Prata', 'Monteiro')]) 
#Monteiro para Recife
G.add_edges_from([("Congo", "Jataúba"), ('Jataúba', 'Toritama')
, ('Toritama','Caruaru'), ('Caruaru', 'Recife')])
#Monteiro para Recife, indo por JP
G.add_edges_from([('Sumé','São José do Cariri'), ('São José do Cariri', 'Campina Grande')
, ('Campina Grande','João Pessoa'), ('João Pessoa','Goiania'),('Goiania', 'Igarassu'), ('Igarassu','Recife')])
val_map = { 'João Pessoa': 0.9525525,
            'Campina Grande': 0.815646,
            'Recife': 0.55739485,
            'Monteiro': 0.6,
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

red_edges = [('Monteiro', 'Sertânia'), ('São José do Egito','Ouro Velho'), ('Jataúba','Toritama')
,('Toritama','Caruaru'),('Caruaru', 'Recife')]
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
pos=nx.spring_layout(G)
nx.draw(G,pos, node_color = values, node_size=900,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
pylab.show()
