with open(0) as f:
    ordering_rules, updates = f.read().strip().split('\n\n')
    ordering_rules = ordering_rules.splitlines()
    updates = updates.splitlines()

t = 0

required_numbers = {}

for rule in ordering_rules:
    X, Y = map(int, rule.split('|'))

    required_numbers[Y] = required_numbers.get(Y, []) + [X]

for update in updates:
    update_numbers = list(map(int, update.split(',')))

    correct_order = all(
        not any(
            remaining_number in required_numbers.get(update_number, [])
            for remaining_number in update_numbers[update_number_index + 1:]
        )
        for update_number_index, update_number in enumerate(update_numbers)
    )
    
    if correct_order:
        t += update_numbers[len(update_numbers) // 2]

print(t)