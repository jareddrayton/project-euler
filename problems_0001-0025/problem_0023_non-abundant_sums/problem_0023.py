from itertools import product


def number_type(n):
    # print(n)
    divisors = []
    for i in range(1, (n // 2)+1):
        if n % i == 0:
            divisors.append(i)

    total = sum(divisors)
    if total == n:
        return (n, 'p', total)
    elif total < n:
        return (n, 'd', total)
    elif total > n:
        return (n, 'a', total)


abun_nums = []
can = set()
cannot = []

for i in range(1, 28123+1):
    print(i)
    tup = number_type(i)
    if tup[1] == 'a':
        abun_nums.append(tup[0])
        combs = product(abun_nums, [tup[0]])
        for comb in combs:
            can.add(sum(comb))
        # print(can)

    if i not in can:
        cannot.append(i)

print(cannot)
print(len(cannot), sum(cannot))
breakpoint()
