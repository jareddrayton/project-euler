# fibonacci_a = 1
# fibonacci_b = 1
# fibonacci_number = 0

# total = 0

# while fibonacci_number < 4000000:

#     fibonacci_number = fibonacci_a + fibonacci_b
#     fibonacci_a = fibonacci_b
#     fibonacci_b = fibonacci_number

#     if fibonacci_number % 2 == 0:
#         total += fibonacci_number

# print(total)

total = 0

def sum_fibonacci_even(fibonacci_a=1, fibonacci_b=1):

    fibonacci_number = fibonacci_a + fibonacci_b

    if fibonacci_number % 2 == 0 and fibonacci_number <= 4000000:
        return fibonacci_number + [fibonacci_number]
    if fibonacci_number < 4000000:
        sum_fibonacci_even(fibonacci_b, fibonacci_number)

sum_fibonacci_even()

print(total)
