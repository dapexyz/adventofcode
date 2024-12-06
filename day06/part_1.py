with open(0) as f:
    grid = [list(c) for c in f.read().splitlines()]

directions = [
    (-1, 0), # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1)  # left
]

def is_obstruction_ahead(r, c):
    new_coord = (r + directions[guard[2]][0], c + directions[guard[2]][1])
    return 0 <= new_coord[0] < len(grid) and 0 <= new_coord[1] < len(grid[0]) and grid[new_coord[0]][new_coord[1]] == '#'

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '^':
            guard = [r, c, 0]

visited = set()

while 0 <= guard[0] < len(grid) and 0 <= guard[1] < len(grid[0]):
    visited.add((guard[0], guard[1]))

    while is_obstruction_ahead(guard[0], guard[1]):
        guard[2] = (guard[2] + 1) % len(directions)
    
    guard[0] = guard[0] + directions[guard[2]][0]
    guard[1] = guard[1] + directions[guard[2]][1]

print(len(visited))