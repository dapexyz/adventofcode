with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0

for line in lines:
    levels = list(map(int, line.split()))

    differences = [right - left for left, right in zip(levels, levels[1:])]
    increase_correct = all(difference >= 1 and difference <= 3 for difference in differences)
    decrease_correct = all(difference >= -3 and difference <= -1 for difference in differences)

    if increase_correct or decrease_correct:
        t += 1

print(t)