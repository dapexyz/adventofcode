import heapq
from collections import defaultdict

with open(0) as f:
    grid = [list(line) for line in f.read().strip().splitlines()]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

walls = set()

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            startpoint = (r, c)
        elif grid[r][c] == 'E':
            endpoint = (r, c)
        elif grid[r][c] == '#':
            walls.add((r, c))

seen = set()
distances = defaultdict(lambda: -1)
heap = [(*startpoint, 0)]
heapq.heapify(heap)

while heap:
    r, c, dist = heapq.heappop(heap)

    if (r, c) in walls:
        continue

    if (r, c) in seen:
        continue

    if not (r in range(len(grid)) and c in range(len(grid[0]))):
        continue

    seen.add((r, c))
    distances[(r, c)] = dist

    for dr, dc in directions:
        heapq.heappush(heap, (r + dr, c + dc, dist + 1))

cheats = set()

for (r, c), dist in distances.items():
    if dist == -1:
        continue
    
    for cheat in range(21):
        for cheat_diff in range(cheat + 1):
            row_diff = cheat - cheat_diff
            col_diff = cheat_diff

            for nr, nc in [(r + row_diff, c + col_diff), (r + row_diff, c - col_diff), (r - row_diff, c + col_diff), (r - row_diff, c - col_diff)]:
                if (nr, nc) in distances and distances[(nr, nc)] - dist >= 100 + cheat:
                    cheats.add((r, c, nr, nc))

print(len(cheats))