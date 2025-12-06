with open(0) as f:
    lines = f.read().strip().splitlines()

problems = {}
for c in range(len(lines[0].split())):
    operator = lines[-1].split()[c].strip()
    _, cur = problems.get(c, (operator, []))
    problems
    for line in lines[:-1]:
        cur = cur + [line.split()[c].strip()]
    problems[c] = (operator, cur)

t = 0
for p in problems:
    prod = 1
    s = 0

    operator, nums = problems[p]
    nums = [int(num) for num in nums]
    if operator == '*':
        prod = 1
        for num in nums:
            prod *= num
        t += prod
    else:
        t += sum(nums)

print(t)