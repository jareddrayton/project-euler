# Need to use backtracking?

with open('problem_0018_input.txt', 'r') as f:
    lines = [list(map(int, line.strip().split(' '))) for line in f.readlines()]

i, total = 0, 0

for index, line in enumerate(lines, start=1):

    total += line[i]
    print(index, line[i], total)

    try:
        a = lines[index][i]
        b = lines[index][i + 1]
        if b > a:
            i += 1
    except IndexError:
        break


def backtrack():


print(total)
