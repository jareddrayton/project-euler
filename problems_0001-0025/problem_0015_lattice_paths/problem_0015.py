from math import comb

n = 20
total = 0

for i, k in zip(range(n-1, n-1+n), range(0, n)):
    total += comb(i, k) * 2

print(total)
