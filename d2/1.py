with open(0) as f:
    ranges = [tuple(map(int, r.split('-'))) for r in f.read().strip().split(',')]

t = 0
for a,b in ranges:
    for num in range(a, b + 1):
        num = str(num)
        if num[:len(num)//2] == num[len(num)//2:]:
            t += int(num)

print(t)