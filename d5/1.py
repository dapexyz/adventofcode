with open(0) as f:
    blocks = f.read().strip().split('\n\n')
    lines, ids = blocks
    lines = lines.splitlines()
    ids = ids.splitlines()

ranges = [tuple(map(int, line.split('-'))) for line in lines]

print(sum(any(a <= int(id) <= b for a,b in ranges) for id in ids))
