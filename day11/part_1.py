with open(0) as f:
    numbers = list(map(int, f.read().strip().split()))

for blink in range(25):
    new_numbers = []

    while numbers:
        cur = numbers.pop(0)

        if cur == 0:
            new_numbers += [1]
            continue

        strlen = len(str(cur))
        if strlen % 2 == 0:
            left = int(str(cur)[:strlen//2])
            right = int(str(cur)[strlen//2:])

            new_numbers += [left]
            new_numbers += [right]
            continue

        new_numbers += [cur * 2024]

    numbers = new_numbers[:]

print(len(numbers))
