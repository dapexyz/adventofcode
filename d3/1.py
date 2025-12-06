with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0
for line in lines:
    m = 0
    for a in range(len(line)):
        for b in range(a + 1, len(line)):
            cur = line[a] + line[b]
            if int(cur) > m:
                m = int(cur)
    t += m

print(t)