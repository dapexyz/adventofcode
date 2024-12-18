import heapq

with open(0) as f:
    coordinates = [list(map(int, line.split(','))) for line in f.read().strip().splitlines()]

GRID_SIZE = 71

corrupted = set()

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

for i, coord in enumerate(coordinates):
    X, Y = coord
    if i == 1024:
        break
    corrupted.add((Y, X))

endpoint = (GRID_SIZE - 1, GRID_SIZE - 1)

heap = [(0, 0, 0)]
heapq.heapify(heap)
min_cost = None
seen = set()

while heap:
    cost, r, c = heapq.heappop(heap)

    if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
        continue

    if (r, c) in corrupted:
        continue

    if (r, c) in seen:
        continue
    seen.add((r, c))

    if (r, c) == endpoint:
        min_cost = cost
        break

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        heapq.heappush(heap, (cost + 1, r + dr, c + dc))

print(min_cost)