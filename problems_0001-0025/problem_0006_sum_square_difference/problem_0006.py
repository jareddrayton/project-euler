n = 100
sumofsquare = 0
squareofsum = 0

for i in range(1, 101):
	sumofsquare += i ** 2
print sumofsquare

for i in range(1, 101):
	squareofsum += i

squareofsum = squareofsum ** 2
print squareofsum

print squareofsum - sumofsquare