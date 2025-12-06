with open(0) as f:
    grid = [list(line) for line in f.read().strip().splitlines()]

dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

t = 0
for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] != '@': continue
        count = 0
        for dr,dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == '@':
                    count += 1

        if count < 4:
            t += 1

print(t)