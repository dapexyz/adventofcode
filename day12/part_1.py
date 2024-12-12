with open(0) as f:
    grid = list(map(list, f.read().strip().splitlines()))

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def get_plants(r, c):
    letter = grid[r][c]
    plants = []
    queue = [(r, c)]
    while queue:
        r, c = queue.pop(0)

        if r not in range(len(grid)) or c not in range(len(grid[0])):
            continue

        if grid[r][c] != letter:
            continue

        if (r, c) in plants:
            continue

        plants.append((r, c))

        for cr, cc in directions:
            queue.append((r + cr, c + cc))

    return plants

def get_perimeter(plants):
    perimeter = 0

    for r, c in plants:
        for cr, cc in directions:
            if (r + cr, c + cc) not in plants:
                perimeter += 1

    return perimeter

t = 0

visited = set()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r, c) in visited:
            continue

        plants = get_plants(r, c)
        visited.update(plants)

        t += len(plants) * get_perimeter(plants)

print(t)