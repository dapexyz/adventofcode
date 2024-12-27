with open(0) as f:
    schematics = list(map(str.splitlines, f.read().strip().split('\n\n')))

locks = set()
keys = set()

for schematic in schematics:
    heights = tuple(l.count('#') for l in zip(*schematic))
    if all(x == '#' for x in schematic[0]):
        locks.add(heights)
    else:
        keys.add(heights)

print(sum(all(x + y <= 7 for x, y in zip(lock, key)) for key in keys for lock in locks))