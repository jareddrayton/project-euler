import math

n = 600851475143
#prime = int(math.sqrt(prime))

listoffactors = []
listofprimes = []

for i in range(2, int(math.sqrt(n)) - 1):
	
	if n % i == 0:
		print "Factor"
		listoffactors.append(i)



print listoffactors
print listofprimes

