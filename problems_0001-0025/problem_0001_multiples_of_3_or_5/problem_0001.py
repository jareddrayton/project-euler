total = 0

for n in range(1, 1000):
    if n % 3 == 0:
        total += n
    elif n % 5 == 0:
        total += n

print(total)
