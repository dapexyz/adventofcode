with open(0) as f:
    program = list(map(int, f.read().strip().split()[-1].split(',')))

t = None

possibilities = [(program, 0)]
while possibilities:
    program, cur_value = possibilities.pop()
    for x in range(8):
        # hardcoded...
        A = cur_value + x
        B = A & 7
        B = B ^ 2
        C = A >> B
        B = B ^ C
        B = B ^ 7

        if B & 7 == program[-1]:
            if len(program) == 1:
                t = A
                continue
            
            possibilities.append((program[:-1], A << 3))

print(t)