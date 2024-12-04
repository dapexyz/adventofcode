with open(0) as f:
    lines = f.read().strip().splitlines()

directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
center_coordinates = []

for r in range(len(lines)):
    for c in range(len(lines[r])):

        for dr, dc in directions:
            if all(0 <= r + dr * i < len(lines) and 0 <= c + dc * i < len(lines[r]) and lines[r + dr * i][c + dc * i] == 'MAS'[i] for i in range(len('MAS'))):
                center_coordinates.append((r + dr, c + dc))

center_coordinates.sort()
print(sum(A == B for A, B in zip(center_coordinates, center_coordinates[1:])))