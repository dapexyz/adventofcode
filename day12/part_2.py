with open(0) as f:
    grid = list(map(list, f.read().strip().splitlines()))

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

diagonal_directions = [
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1)
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

def is_corner(plants, r, c, dr, dc):
    adj1 = (r + dr, c) in plants
    adj2 = (r, c + dc) in plants
    diagonal = (r + dr, c + dc) in plants
    return (adj1 and adj2 and not diagonal) or (not adj1 and not adj2)

def get_sides(plants):
    sides = 0
    
    for plant in plants:
        sides += sum(is_corner(plants, *plant, dr, dc) for dr, dc in diagonal_directions)

    return sides

t = 0

visited = set()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r, c) in visited:
            continue

        plants = get_plants(r, c)
        visited.update(plants)

        t += len(plants) * get_sides(plants)

print(t)