with open(0) as f:
    lines = f.read().strip().splitlines()

width = max(len(line) for line in lines)
grid = [line.ljust(width) for line in lines]

problems = []
operator = ''
cols = []
for c in range(width):
    if cols == []:
        operator = grid[-1][c]
    col = [grid[r][c] for r in range(len(grid) - 1)]
    if all(c == ' ' for c in col):
        problems.append((operator, cols))
        cols = []
        continue
    else:
        cols.append(col)
problems.append((operator, cols))

t = 0
for p in problems:
    prod = 1
    s = 0

    operator, nums = p
    nums = [int(''.join(num)) for num in nums]
    if operator == '*':
        prod = 1
        for num in nums:
            prod *= num
        t += prod
    else:
        t += sum(nums)

print(t)