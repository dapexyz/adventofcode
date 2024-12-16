with open(0) as f:
    grid, instructions = f.read().strip().split('\n\n')
    grid = [list(line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')) for line in grid.splitlines()]
    instructions = ''.join(instructions.splitlines())

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            robot = (r, c)
            grid[r][c] = '.'

for instruction in instructions:
    dr, dc = [(-1, 0), (1, 0), (0, -1), (0, 1)]['^v<>'.index(instruction)]
    r, c = robot
    nr, nc = r + dr, c + dc

    if grid[nr][nc] == '.':
        robot = (nr, nc)
    elif grid[nr][nc] in '[]':
        br, bc = nr, nc
        checking = set([(br, bc)])
        moving = set()
        possible = True

        while checking:
            cr, cc = checking.pop()

            if (cr, cc) in moving or (cr, cc) in checking:
                continue

            if grid[cr][cc] == '#':
                possible = False
                break

            if grid[cr][cc] == '[':
                moving.add((cr, cc))
                moving.add((cr, cc + 1))
                checking.add((cr + dr, cc + dc))
                checking.add((cr + dr, cc + dc + 1))

            if grid[cr][cc] == ']':
                moving.add((cr, cc))
                moving.add((cr, cc - 1))
                checking.add((cr + dr, cc + dc))
                checking.add((cr + dr, cc + dc - 1))
        
        if possible:
            copy = [row[:] for row in grid]

            for mr, mc in moving:
                grid[mr][mc] = '.'

            for mr, mc in moving:
                grid[mr + dr][mc + dc] = copy[mr][mc]

            robot = (nr, nc)
    
print(sum(100 * r + c for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '['))