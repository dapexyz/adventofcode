with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0

for line in lines:
    levels = list(map(int, line.split()))

    for remove_index in range(len(levels)):
        adjusted_levels = (levels[:remove_index] + levels[remove_index + 1:])

        differences = [right - left for left, right in zip(adjusted_levels, adjusted_levels[1:])]
        increase_correct = all(difference >= 1 and difference <= 3 for difference in differences)
        decrease_correct = all(difference >= -3 and difference <= -1 for difference in differences)

        if increase_correct or decrease_correct:
            t += 1
            break

print(t)