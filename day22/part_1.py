with open(0) as f:
    secret_numbers = list(map(int, f.read().strip().splitlines()))

def evolve(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216

    return secret

t = 0

for secret in secret_numbers:
    for _ in range(2000):
        secret = evolve(secret)

    t += secret

print(t)