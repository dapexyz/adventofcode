from collections import defaultdict

with open(0) as f:
    initial_values, gates = map(str.splitlines, f.read().strip().split('\n\n'))
    initial_values = [x.split(': ') for x in initial_values]

wire_values = defaultdict(lambda: None)

for wire, value in initial_values:
    wire_values[wire] = int(value)

working = True
while working:
    working = False
    for gate in gates:
        instruction, target = gate.split(' -> ')

        if target in wire_values:
            continue

        instruction = instruction.replace(' AND ', ' & ')
        instruction = instruction.replace(' XOR ', ' ^ ')
        instruction = instruction.replace(' OR ', ' | ')

        wire1, operation, wire2 = instruction.split()

        if wire1 not in wire_values or wire2 not in wire_values:
            continue

        working = True
        wire_values[target] = eval(f"wire_values['{wire1}'] {operation} wire_values['{wire2}']")

print(int(''.join(str(value) for wire, value in sorted(wire_values.items(), reverse=True) if wire.startswith('z')), 2))