with open('problem_10', 'r') as f:
    input_data = [int(x.strip()) for x in f.readlines()]
print(str(sum(input_data))[:10])