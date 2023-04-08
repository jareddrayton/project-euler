# 1x1 2
# 2x2 6
# 3x3 20

# 0 
# 1
# 3
# 6
# 10
# 15
# 21


def triangle_number():
    number = 0
    i = 1
    while True:
        number += i
        yield number
        i += 1


for i, number in enumerate(triangle_number(), start=1):

    # print(i,number)
    if i == 1 or i % 2 == 0:
        print(i//2, number*2)
    if i == 40:
        break