#Importar el módulo networkx de Python para trabajar con grafos

import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt

# Resolver el Grafo utilizando el qpu
#from dwave.system.samplers import DWaveSampler
#from dwave.system.composites import EmbeddingComposite

#Crear un grafo de 4 nodos
#G=nx.Graph()
#G.add_nodes_from(["s","1","2","t"])
#G.add_weighted_edges_from({("s","1", 1), ("s", "2", 2), ("1", "t", 2), ("2", "t", 1)})
#G.add_edge("s","1")
#G.add_edge("s","2")
#G.add_edge("1","t")
#G.add_edge("2","t")

G=nx.Graph()
#i=1
G.add_node("s",pos=(1,1))
G.add_node("1",pos=(2,2))
G.add_node("2",pos=(2,0))
G.add_node("t",pos=(3,1))
G.add_edge("s","1",weight=1)
G.add_edge("s","2",weight=2)
G.add_edge("1","t",weight=2)
G.add_edge("2","t",weight=1)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#nx.draw(G, with_labels = True, with_weights = True)
plt.savefig("maxflujo.png")