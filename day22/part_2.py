from collections import defaultdict, deque

with open(0) as f:
    secret_numbers = list(map(int, f.read().strip().splitlines()))

def evolve(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216

    return secret

all_seq_max = defaultdict(int)

for secret in secret_numbers:
    seq_max = dict()
    cur_seq = deque(maxlen=4)


    prev_price = secret % 10

    for _ in range(2000):
        secret = evolve(secret)
        
        price = secret % 10
        diff = price - prev_price

        cur_seq.append(diff)

        if len(cur_seq) == 4:
            seq = tuple(cur_seq)
            if seq not in seq_max:
                seq_max[seq] = price

        prev_price = price

    for k,v in seq_max.items():
        all_seq_max[k] += v

print(max(all_seq_max.values()))