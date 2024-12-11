from collections import defaultdict

with open(0) as f:
    numbers = defaultdict(int)

    for number in list(map(int, f.read().strip().split())):
        numbers[number] += 1

def get_result(cur):
    if cur == 0:
        return [1]

    strlen = len(str(cur))
    if strlen % 2 == 0:
        factor = 10 ** (strlen // 2)
        left = cur // factor
        right = cur % factor

        return [left, right]

    return [cur * 2024]

for blink in range(75):
    tmp = defaultdict(int)

    for num in numbers.keys():
        for res in get_result(num):
            tmp[res] += numbers[num]

    numbers = tmp

print(sum(numbers.values()))