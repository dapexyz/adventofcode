with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0
for line in lines:
    m = ''
    midx = 0
    remaining = 12

    while remaining:
        cline = line[midx:len(line) - remaining + 1]
        cmidx = cline.index(max(cline))
        m += cline[cmidx]
        midx += cmidx + 1
        remaining -= 1

    t += int(m)

print(t)
