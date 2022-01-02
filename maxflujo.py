#Importar el módulo networkx de Python para trabajar con grafos

import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt

# Resolver el Grafo utilizando el qpu
#from dwave.system.samplers import DWaveSampler
#from dwave.system.composites import EmbeddingComposite

G=nx.Graph()
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
plt.savefig("maxflujo.png")

#A maximum cut is a subset S of the vertices of G such that the number of edges between S and the complementary subset
# is as large as possible.

import dimod

# Cálculo del flujo máximo
# mediante un algoritmo clásico (Edmonds-Karp)
sampler = dimod.SimulatedAnnealingSampler()
cut=dnx.weighted_maximum_cut(G,sampler)
print(cut)

# Matriz Q de restricciones QUBO
alpha_s=0.3
bqm = dimod.BinaryQuadraticModel({},{'aa': 1-alpha_s, 'ad': -2, 'ae': -2, 'bb': 1-alpha_s, 'bc': 2, 
                           'bf': -2, 'cc': 1-alpha_s, 'cf': -2, 'dd': 1, 'de': 2, 'ee': 1, 'ff': 1},0,'BINARY')

from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
sampleset = sampler.sample(bqm)

# Redirigimos la salida a un fichero
import sys
file_path = 'randomfile.txt'
sys.stdout = open(file_path, "w")

print('Algoritmo clásico: Edmonds-Karp')
print('===============================')
print(sampleset.lowest(atol=.5))
print(' ')
 
# Resolviendo el problema en la QPU
# Uso el software de OCEAN para hacer embdding automatico
from dwave.system import DWaveSampler, EmbeddingComposite
sampler_auto = EmbeddingComposite(DWaveSampler(solver={'topology__type':'chimera'}))

# Pasamos los valores de los coecientes del problema:
linear = {('a', 'a'): 1-alpha_s, ('b', 'b'): 1-alpha_s, ('c', 'c'): 1-alpha_s,('d','d'): 1, ('e','e'): 1, ('f','f'): 1}
quadratic = {('a', 'd'): -2, ('a', 'e'): -2, ('b', 'c'): 2, ('b','f'): -2, ('c','f'): -2, ('d','e'): 2}
Q = {**linear, **quadratic}
sampleset = sampler_auto.sample_qubo(Q, num_reads=5000)

print('Resolución en QPU')
print('=================')
print(sampleset)