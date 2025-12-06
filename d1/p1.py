with open(0) as f:
    lines = f.read().strip().splitlines()

cur = 50
t = 0
for line in lines:
    d,v = line[0], int(line[1:])

    if d == 'L':
        v *= -1

    cur += v
    cur %= 100
    t += cur == 0

print(t)
