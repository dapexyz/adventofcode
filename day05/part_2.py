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
    
    if not correct_order:
        reordered_numbers = []

        while update_numbers:
            for update_number in list(update_numbers):
                if all(required_number not in update_numbers or required_number in reordered_numbers for required_number in required_numbers.get(update_number, [])):
                    reordered_numbers.append(update_number)
                    update_numbers.remove(update_number)
                    break
        
        t += reordered_numbers[len(reordered_numbers) // 2]

print(t)