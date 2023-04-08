from itertools import permutations

for i, permutation in enumerate(permutations(range(0, 10)), start=1):
    if i == 1000000:
        print(permutation)
        print("".join(map(str, permutation)))
