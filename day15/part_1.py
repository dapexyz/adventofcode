with open(0) as f:
    grid, instructions = f.read().strip().split('\n\n')
    grid = [list(line) for line in grid.splitlines()]
    instructions = ''.join(instructions.splitlines())

boxes = []
walls = []

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            robot = (r, c)
        elif grid[r][c] == 'O':
            boxes.append((r, c))
        elif grid[r][c] == '#':
            walls.append((r, c))

for instruction in instructions:
    dr, dc = [(-1, 0), (1, 0), (0, -1), (0, 1)]['^v<>'.index(instruction)]
    r, c = robot
    nr, nc = r + dr, c + dc

    if (nr, nc) not in boxes and (nr, nc) not in walls:
        robot = (nr, nc)
    elif (nr, nc) in boxes:
        br, bc = nr, nc

        while br in range(len(grid)) and bc in range(len(grid[0])):
            if (br, bc) in walls:
                break

            if (br, bc) not in boxes:
                del boxes[boxes.index((nr, nc))]
                boxes.append((br, bc))
                robot = (nr, nc)
                break

            br += dr
            bc += dc

print(sum(100 * box[0] + box[1] for box in boxes))