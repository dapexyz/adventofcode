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

t = 0
while True:
    for i, (px, py, vx, vy) in enumerate(robots):
        positions[(px, py)] -= 1

        if positions[(px, py)] == 0:
            del positions[(px, py)]

        px = (px + vx) % WIDTH
        py = (py + vy) % HEIGHT
        positions[(px, py)] += 1

        robots[i][0] = px
        robots[i][1] = py

    t += 1
    
    if len(positions.keys()) == len(robots):
        break

print(t)