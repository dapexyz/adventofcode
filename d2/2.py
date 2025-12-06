with open(0) as f:
    ranges = [tuple(map(int, r.split('-'))) for r in f.read().strip().split(',')]

t = 0
for a,b in ranges:
    for num in range(a, b + 1):
        num = str(num)
        for d in range(1, len(num)//2 + 1):
            if len(num) % d != 0: continue
            if num[:d]*(len(num)//d) == num:
                t += int(num)
                break

print(t)