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

for cur_byte, coord in enumerate(coordinates):
    X, Y = coord
    if cur_byte == 1024:
        break
    corrupted.add((Y, X))

endpoint = (GRID_SIZE - 1, GRID_SIZE - 1)

def is_possible(corrupted):
    heap = [(0, 0, 0)]
    heapq.heapify(heap)
    seen = set()
    ret = False

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
            ret = True
            break

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            heapq.heappush(heap, (cost + 1, r + dr, c + dc))
    return ret

for cur_byte in range(cur_byte, len(coordinates)):
    X, Y = coordinates[cur_byte]

    corrupted.add((Y, X))

    if not is_possible(corrupted):
        answer = str(X) + ',' + str(Y)
        break

print(answer)