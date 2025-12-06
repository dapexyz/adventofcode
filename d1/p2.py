with open(0) as f:
    lines = f.read().strip().splitlines()

cur = 50
t = 0
for line in lines:
    d,v = line[0], int(line[1:])

    for _ in range(v):
        cur += -1 if d == 'L' else 1
        cur %= 100
        t += cur == 0

print(t)
