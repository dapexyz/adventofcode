with open(0) as f:
    blocks = f.read().strip().split('\n\n')
    lines, ids = blocks
    lines = lines.splitlines()
    ids = ids.splitlines()

ranges = [tuple(map(int, line.split('-'))) for line in lines]

reduced = []
for a,b in sorted(ranges):
    for idx, (ra, rb) in enumerate(reduced):
        if a <= rb:
            reduced[idx] = (ra, max(b, rb))
            break
    else:
        reduced.append((a, b))

print(sum(rb - ra + 1 for ra, rb in reduced))