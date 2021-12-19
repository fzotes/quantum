# Importación de Librerías
import networkx as nx
import matplotlib.pyplot as mpl
import dwave_networkx as dnx
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dimod.reference.samplers import ExactSolver

# Creación del Grafo de 5 nodos
s5=nx.star_graph(5)

# Resolución sobre qpu
sampler=EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(s5,sampler))

nx.draw(s5, with_labels = True)
mpl.savefig("graficoestrella.png")

# Resolución sobre un Computador Clásico
#  sampler=ExactSolver()
#  print(dnx.min_vertex_cover(s5,sampler))