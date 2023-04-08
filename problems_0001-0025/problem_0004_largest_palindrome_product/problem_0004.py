pallindromes = []

for i in range(1000):
	for a in range(1000):
		product = i * a
		if str(product) == str(product)[::-1]:
			pallindromes.append(product)

print max(pallindromes)