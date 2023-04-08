import math

primes = [2,3,5,7,11]
n = 11

while len(primes) != 10001:
	nooffactors = 0
	
	#for i in range(len(primes) -1, 0, -1):
	for i in xrange(1, len(primes)):
		#print i
		if n % primes[i] == 0:
			nooffactors += 1
			break
	if nooffactors == 0:
		primes.append(n)
	n += 2

print len(primes)
print primes[10000]



