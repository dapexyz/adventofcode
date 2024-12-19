with open(0) as f:
    patterns, designs = f.read().strip().split('\n\n')
    patterns = patterns.split(', ')
    designs = designs.splitlines()

def is_possible(design: str):
    if len(design) == 0:
        return True
    
    for pattern in patterns:
        if design.startswith(pattern):
            if is_possible(design[len(pattern):]):
                return True

    return False

print(sum(is_possible(design) for design in designs))