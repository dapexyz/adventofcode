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

paths = [(0, startpoint, 3, None, None)]
min_score = None
seen = set()

best = dict()

while paths:
    paths = sorted(paths)
    path = paths.pop(0)

    score, pos, dir, prev_pos, prev_dir = path
        
    best_cost, best_src = best.get((pos, dir), (None, []))

    if score == best_cost:
        best[(pos, dir)] = (best_cost, best_src + [(prev_pos, prev_dir)])
    elif best_cost == None or score < best_cost:
        best[(pos, dir)] = (score, [(prev_pos, prev_dir)])

    if pos in walls:
        continue

    if (pos, dir) in seen:
        continue

    seen.add((pos, dir))

    if pos == endpoint:
        min_score = score if min_score == None else min(score, min_score)
        continue

    left = (dir - 1) % len(directions)
    left_dir = directions[left]

    right = (dir + 1) % len(directions)
    right_dir = directions[right]


    straight = dir
    straight_dir = directions[dir]

    paths.append((score + 1001, (pos[0] + left_dir[0], pos[1] + left_dir[1]), left, pos, dir))
    paths.append((score + 1001, (pos[0] + right_dir[0], pos[1] + right_dir[1]), right, pos, dir))
    paths.append((score + 1, (pos[0] + straight_dir[0], pos[1] + straight_dir[1]), straight, pos, dir))

stack = [(endpoint, x) for x in range(4) if (endpoint, x) in best and best[(endpoint, x)][0] == min_score]
seen = set()

while stack:
    cur = stack.pop()

    if cur in seen:
        continue
    seen.add(cur)

    for x in best[cur][1]:
        if x != (None, None):
            stack.append(x)

print(len(set(pos for pos, _ in seen)))