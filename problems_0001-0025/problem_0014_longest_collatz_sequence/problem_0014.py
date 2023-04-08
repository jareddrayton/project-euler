from operator import itemgetter

def generate_collatz_sequence(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

results = {}

for i in range(500000, 1000000):
    if i // 2 
    results[len(generate_collatz_sequence(i))] = i

print(max(results, key=itemgetter(0)))

