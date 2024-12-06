with open(0) as f:
    grid = [list(c) for c in f.read().splitlines()]

directions = [
    (-1, 0), # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1)  # left
]

def is_obstruction_ahead(r, c, new_obstruction_r, new_obstruction_c, guard):
    new_coord = (r + directions[guard[2]][0], c + directions[guard[2]][1])
    return 0 <= new_coord[0] < len(grid) and 0 <= new_coord[1] < len(grid[0]) and (grid[new_coord[0]][new_coord[1]] == '#' or (new_coord[0] == new_obstruction_r and new_coord[1] == new_obstruction_c))

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '^':
            initial_guard = [r, c, 0]

t = 0

def simulate_run(new_obstruction_r = -1, new_obstruction_c = -1):
    guard = initial_guard[:]
    is_loop = False
    visited = set()

    while 0 <= guard[0] < len(grid) and 0 <= guard[1] < len(grid[0]):
        if (guard[0], guard[1], guard[2]) in visited:
            is_loop = True
            break

        visited.add((guard[0], guard[1], guard[2]))

        while is_obstruction_ahead(guard[0], guard[1], new_obstruction_r, new_obstruction_c, guard):
            guard[2] = (guard[2] + 1) % len(directions)
        
        guard[0] = guard[0] + directions[guard[2]][0]
        guard[1] = guard[1] + directions[guard[2]][1]

    return (visited, is_loop)

checked_spots = set()
for initially_visited_point in simulate_run()[0]:
    new_obstruction_r = initially_visited_point[0]
    new_obstruction_c = initially_visited_point[1]

    if (new_obstruction_r, new_obstruction_c) in checked_spots or (initial_guard[0] == new_obstruction_r and initial_guard[1] == new_obstruction_c):
        continue

    checked_spots.add((new_obstruction_r, new_obstruction_c))

    if simulate_run(new_obstruction_r, new_obstruction_c)[1]:
        t += 1

print(t)