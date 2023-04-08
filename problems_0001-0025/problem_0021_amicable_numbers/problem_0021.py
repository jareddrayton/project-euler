def divisors(n):

    divisors = []
    for i in range(1, (n // 2)+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


def is_pair(a):
    res_a = divisors(a)
    b = res_a
    res_b = divisors(b)
    if a == res_b and a != b:
        return a, b
    else:
        return False


amicable_numbers = set()

for i in range(1, 10001):

    if is_pair(i):
        amicable_numbers.update(is_pair(i))
        print(amicable_numbers)

breakpoint()