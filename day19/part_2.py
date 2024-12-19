with open(0) as f:
    patterns, designs = f.read().strip().split('\n\n')
    patterns = patterns.split(', ')
    designs = designs.splitlines()


known = dict()

def count_possible(design: str):
    if design in known:
        return known[design]

    if len(design) == 0:
        return True
    
    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += count_possible(design[len(pattern):])

    known[design] = count
    return count

print(sum(count_possible(design) for design in designs))