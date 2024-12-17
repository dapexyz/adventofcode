with open(0) as f:
    grid = list(map(list, [line for line in f.read().strip().splitlines()]))

walls = set()

for r in range(len(grid)):
    for c in range(len(grid[0])):
        cur = grid[r][c]
        if cur == 'E':
            endpoint = (r, c)
        elif cur == 'S':
            startpoint = (r, c)
        elif cur == '#':
            walls.add((r, c))

directions = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]

paths = [(0, startpoint, 3)]
min_score = None
seen = set()

while paths:
    paths = sorted(paths)
    path = paths.pop(0)

    score, pos, dir = path

    if pos in walls:
        continue

    if (pos, dir) in seen:
        continue

    seen.add((pos, dir))

    if pos == endpoint:
        min_score = score
        break

    left = (dir - 1) % len(directions)
    left_dir = directions[left]

    right = (dir + 1) % len(directions)
    right_dir = directions[right]


    straight = dir
    straight_dir = directions[dir]

    paths.append((score + 1001, (pos[0] + left_dir[0], pos[1] + left_dir[1]), left))
    paths.append((score + 1001, (pos[0] + right_dir[0], pos[1] + right_dir[1]), right))
    paths.append((score + 1, (pos[0] + straight_dir[0], pos[1] + straight_dir[1]), straight))

print(min_score)
