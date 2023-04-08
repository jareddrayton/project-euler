from math import sqrt


def fibonacci():
    a, b = 0, 1
    while True:
        fib_num = a + b
        yield fib_num
        a, b = b, fib_num


phi = (1 + 5 ** 0.5) / 2

# F(k) = (phi^k - (-1/phi)^k)/sqrt(5)


# def fib(K):
#     return (phi ** K - (-1 / phi) ** K) / sqrt(5)

def fib(K):
    return (phi ** K / sqrt(5))


for i, fib_num in enumerate(fibonacci(), start=2):
    print(i, fib_num, int(fib(i)))
    if len(str(fib_num)) == 1000:
        print(i)
        break


print(fib(999))
