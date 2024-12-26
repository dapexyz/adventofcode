from collections import deque
from itertools import permutations, combinations
import re

with open(0) as f:
    target_codes = f.read().strip().splitlines()

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""
numeric_keypad = [
    [ '7', '8', '9' ],
    [ '4', '5', '6' ],
    [ '1', '2', '3' ],
    [ ' ', '0', 'A' ]
]

numeric_keypad_coords = dict()
for r in range(len(numeric_keypad)):
    for c in range(len(numeric_keypad[r])):
        if numeric_keypad[r][c] == ' ':
            continue
        numeric_keypad_coords[numeric_keypad[r][c]] = (r, c)

"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
directional_keypad = [
    [ ' ', '^', 'A' ],
    [ '<', 'v', '>' ]
]

directional_keypad_coords = dict()
for r in range(len(directional_keypad)):
    for c in range(len(directional_keypad[r])):
        if directional_keypad[r][c] == ' ':
            continue
        directional_keypad_coords[directional_keypad[r][c]] = (r, c)

directions = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]

get_direction = lambda button: directions['^<v>'.index(button)]
in_keypad = lambda r, c, keypad: r in range(len(keypad)) and c in range(len(keypad[r])) and keypad[r][c] != ' '

KEYPAD_NUMERIC = 0
KEYPAD_DIRECTIONAL = 1
KEYPADS = {
    KEYPAD_NUMERIC: [numeric_keypad, numeric_keypad_coords],
    KEYPAD_DIRECTIONAL: [directional_keypad, directional_keypad_coords]
}

# (numeric/directional, from, to) -> list(string)
shortest_paths = dict()

for keypad_index, (keypad, keypad_coords) in KEYPADS.items():
    for FROM, TO in permutations(keypad_coords.values(), r=2):
        valid_paths = set()
        bfs = deque([(FROM, '', set())])

        while bfs:
            (r, c), sequence, seen = bfs.popleft()

            if not in_keypad(r, c, keypad):
                continue

            if (r, c) in seen:
                continue
            seen.add((r, c))

            if (r, c) == TO:
                valid_paths.add(sequence)
                continue
            
            if len(valid_paths) != 0:
                continue

            for direction in '^v<>':
                dr, dc = get_direction(direction)
                nr, nc = r + dr, c + dc

                bfs.append(((nr, nc), sequence + direction, seen | set([(r, c)])))

        shortest_paths[(keypad_index, FROM, TO)] = list(valid_paths)

# TODO