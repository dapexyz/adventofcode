with open(0) as f:
    numbers = list(map(int, f.read().strip()))

t = 0

arr = []
cur = 0
idx = 0

files = []
free_spaces = []

for i in range(len(numbers)):
    if numbers[i] == 0:
        continue

    if i % 2 == 0:
        files += [(cur, idx, int(numbers[i]))]
        cur += 1
    else:
        free_spaces += [(idx, int(numbers[i]))]

    idx += int(numbers[i])

for (file_id, file_start_index, file_length) in files[::-1]:
    for space_index, (space_start_index, space_length) in enumerate(free_spaces):
        if space_start_index > file_start_index:
            break
        if space_length >= file_length:
            files[file_id] = (file_id, space_start_index, file_length)
            free_spaces[space_index] = (space_start_index + file_length, space_length - file_length)
            break

    t += sum(range(files[file_id][1], files[file_id][1] + file_length)) * file_id

print(t)