with open(0) as f:
    numbers = list(map(int, f.read().strip()))

arr = []
cur = 0

for i in range(len(numbers)):
    if i % 2 == 0:
        arr += [str(cur)] * int(numbers[i])
        cur += 1
    else:
        arr += ['.'] * int(numbers[i])

while True:
    if '.' not in arr:
        break


    last_num_index = len(arr) - 1 - next((index for index, value in enumerate(arr[::-1]) if value.isdigit()))
    free_space = arr.index('.')

    if last_num_index < free_space:
        break

    arr[free_space] = arr[last_num_index]
    del arr[last_num_index]

print(sum(int(num) * i for i, num in enumerate(arr) if num.isdigit()))