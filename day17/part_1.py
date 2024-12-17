with open(0) as f:
    A, B, C, program = [line.split(': ')[1] for line in f.read().strip().replace('\n\n', '\n').splitlines()]
    A, B, C = map(int, (x for x in [A, B, C]))
    program = list(map(int, program.split(',')))

instruction_pointer = 0
output = []

def get_combo_operand(operand):
    if 0 <= operand <= 3:
        return operand
    
    if operand == 4:
        return A
    
    if operand == 5:
        return B
    
    if operand == 6:
        return C
    
    assert False


while instruction_pointer < len(program) - 1:
    opcode, operand = program[instruction_pointer:instruction_pointer + 2]
    jumped = False
    
    # adv
    if opcode == 0:
        numerator = A
        denominator = 2 ** get_combo_operand(operand)

        A = int(numerator // denominator)
    
    # bxl
    elif opcode == 1: 
        B = B ^ operand

    # bst
    elif opcode == 2:
        B = get_combo_operand(operand) % 8

    # jnz
    elif opcode == 3: 

        if A != 0:
            instruction_pointer = operand
            jumped = True

    # bxc            
    elif opcode == 4: 
        B = B ^ C

    # out        
    elif opcode == 5: 
        output.append(str(get_combo_operand(operand) % 8))

    # bdv        
    elif opcode == 6: 
        numerator = A
        denominator = 2 ** get_combo_operand(operand)

        B = int(numerator // denominator)

    # cdv        
    elif opcode == 7: 
        numerator = A
        denominator = 2 ** get_combo_operand(operand)

        C = int(numerator // denominator)

    else:
        assert False

    if not jumped:
        instruction_pointer += 2

print(','.join(output))
