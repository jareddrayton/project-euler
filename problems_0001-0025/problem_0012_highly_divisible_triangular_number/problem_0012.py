def find_factors(n):
    factors = [1, n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors += [i, n//i]
    return len(factors)


def triangle_number():
    number = 0
    i = 1
    while True:
        number += i
        yield number
        i += 1


def main():
    for number in triangle_number():
        if number % 10 != 0:
            continue
        else:
            total_factors = find_factors(number)
            if total_factors > 500:
                print(total_factors, number)
                break


if __name__ == '__main__':
    main()
