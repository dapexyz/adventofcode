import networkx as nx

with open(0) as f:
    lines = f.read().strip().splitlines()

G = nx.Graph([line.split('-') for line in lines])

print(','.join(sorted(max(nx.find_cliques(G), key=len))))