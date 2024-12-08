import itertools
from collections import defaultdict

with open(0) as f:
    grid = [list(line) for line in f.read().strip().splitlines()]

antennas = defaultdict(list)

for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] != '.':
            antennas[grid[r][c]].append((r, c))

antinodes = set()

for antenna_locations in antennas.values():
    for loc1, loc2 in itertools.combinations(antenna_locations, 2):
        cr = loc2[0] - loc1[0]
        cc = loc2[1] - loc1[1]

        for loc, cr, cc in [(loc1, -cr, -cc), (loc2, cr, cc)]:
            while loc[0] in range(len(grid)) and loc[1] in range(len(grid[0])):
                antinodes.add(loc)
                loc = (loc[0] + cr, loc[1] + cc)

print(len(antinodes))