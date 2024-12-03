import re

with open(0) as f:
    instruction_string = f.read().strip()

t = 0

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', instruction_string)

for match in matches:
    x, y = map(int, match)

    t += x * y

print(t)