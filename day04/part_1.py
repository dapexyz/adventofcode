with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

for r in range(len(lines)):
    for c in range(len(lines[r])):

        for dr, dc in directions:
            if all(0 <= r + dr * i < len(lines) and 0 <= c + dc * i < len(lines[r]) and lines[r + dr * i][c + dc * i] == 'XMAS'[i] for i in range(len('XMAS'))):
                t += 1

print(t)