with open(0) as f:
    grid = [list(map(int, line)) for line in f.read().strip().splitlines()]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

t = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != 0:
            continue

        nines = set()
        queue = [(r, c)]

        while queue:
            cur_r, cur_c = queue.pop()
            cur_value = grid[cur_r][cur_c]

            if cur_value == 9:
                nines.add((cur_r, cur_c))
                continue

            for dr, dc in directions:
                if (cur_r + dr) in range(len(grid)) and (cur_c + dc) in range(len(grid[0])):
                    if grid[cur_r + dr][cur_c + dc] == cur_value + 1:
                        queue.append((cur_r + dr, cur_c + dc))
        t += len(nines)

print(t)