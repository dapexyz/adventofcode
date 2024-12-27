import networkx as nx
from itertools import combinations

with open(0) as f:
    lines = f.read().strip().splitlines()

G = nx.Graph([line.split('-') for line in lines])

sets = set()

for pc1, pc2, pc3 in combinations(G.nodes(), 3):
    if not all([G.has_edge(pc1, pc2), G.has_edge(pc1, pc3), G.has_edge(pc2, pc3)]):
        continue

    if not any(pc.startswith('t') for pc in [pc1, pc2, pc3]):
        continue

    sets.add(tuple(sorted([pc1, pc2, pc3])))

print(len(sets))