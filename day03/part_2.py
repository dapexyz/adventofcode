import re

with open(0) as f:
    instruction_string = f.read().strip()

t = 0

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', instruction_string)

enabled = True

for match in matches:
    if match[3]:
        enabled = False
    elif match[2]:
        enabled = True
    elif enabled:
        x, y = map(int, match[:2])

        t += x * y

print(t)