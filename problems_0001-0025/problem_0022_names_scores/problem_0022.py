with open('p022_names.txt', 'r') as fh:
    names = fh.read().split(",")
    names = [name.strip('"') for name in names]
    names = sorted(names)
    breakpoint()


def calculate_alpha_value(string: str):
    string = string.lower()
    return sum([ord(letter) - 96 for letter in string])


new_list = []

for i, name in enumerate(names, start=1):
    alpha_value = calculate_alpha_value(name)
    new_list.append(i*alpha_value)
print(sum(new_list))
