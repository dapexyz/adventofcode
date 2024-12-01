with open(0) as f:
    lines = f.read().strip().splitlines()

t = 0

left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

for number in left_list:
    t += number * right_list.count(number)

print(t)

