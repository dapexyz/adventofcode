import itertools

with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0

operators = ['+', '*', '||']

for line in lines:
    target_result, numbers = line.split(': ')
    target_result = int(target_result)
    numbers = list(map(int, numbers.split()))

    for possible_operator_combination in itertools.product(operators, repeat=len(numbers) - 1):
        result = numbers[0]

        for i in range(1, len(numbers)):
            operator = possible_operator_combination[i - 1]
            if operator == '||':
                result = int(str(result) + str(numbers[i]))
            elif operator == '*':
                result *= numbers[i]
            else:
                result += numbers[i]

        if result == target_result:
            t += target_result
            break

print(t)

