with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0

left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

left_list = sorted(left_list)
right_list = sorted(right_list)

for left, right in zip(left_list, right_list):
    t += max(left, right) - min(left, right)

print(t)

