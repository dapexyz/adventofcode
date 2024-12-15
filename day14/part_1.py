import re
from collections import defaultdict

with open(0) as f:
    robots = f.read().strip().splitlines()

HEIGHT = 103
WIDTH = 101

# HEIGHT = 7
# WIDTH = 11

positions = defaultdict(int)

robots = [[px, py, vx, vy] for px, py, vx, vy in list(map(int, re.findall(r'-?\d+', robot)) for robot in robots)]

for (px, py, _, _) in robots:
    positions[(px, py)] += 1

for _ in range(100):
    for i, (px, py, vx, vy) in enumerate(robots):
        positions[(px, py)] -= 1

        px = (px + vx) % WIDTH
        py = (py + vy) % HEIGHT
        positions[(px, py)] += 1

        robots[i][0] = px
        robots[i][1] = py

t = sum(positions[(x, y)] for x in range(WIDTH // 2) for y in range(HEIGHT // 2))
t *= sum(positions[(x, y)] for x in range(WIDTH // 2 + 1, WIDTH + 1) for y in range(HEIGHT // 2))
t *= sum(positions[(x, y)] for x in range(WIDTH // 2) for y in range(HEIGHT // 2 + 1, HEIGHT + 1))
t *= sum(positions[(x, y)] for x in range(WIDTH // 2 + 1, WIDTH + 1) for y in range(HEIGHT // 2 + 1, HEIGHT + 1))

print(t)