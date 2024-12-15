import re
import numpy as np

with open(0) as f:
    machines = list(machine.splitlines() for machine in f.read().strip().split('\n\n'))

t = 0

def possible_combination(button_a, button_b, target_location, a_presses, b_presses) -> bool:
    return all([
        a_presses * button_a[0] + b_presses * button_b[0] == target_location[0],
        a_presses * button_a[1] + b_presses * button_b[1] == target_location[1]
    ])

for (button_a, button_b, target_location) in machines:
    button_a = [int(x) for x in re.findall(r'\d+', button_a)]
    button_b = [int(x) for x in re.findall(r'\d+', button_b)]
    target_location = [int(x) + 10000000000000 for x in re.findall(r'\d+', target_location)]

    a_presses, b_presses = map(round, np.linalg.solve(list(map(list, zip(button_a, button_b))), target_location))
    
    if possible_combination(button_a, button_b, target_location, a_presses, b_presses):
        t += 3 * a_presses + b_presses
    

print(t)