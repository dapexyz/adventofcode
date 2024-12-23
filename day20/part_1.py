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

t = 0

for (r, c), dist in distances.items():
    if dist == -1:
        continue

    for nr, nc in [(r + 2, c), (r - 2, c), (r, c + 2), (r, c - 2), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)]:
        t += (nr, nc) in distances and distances[(nr, nc)] - dist >= 102

print(t)
