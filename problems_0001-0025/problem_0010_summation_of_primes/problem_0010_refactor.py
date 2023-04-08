import math

n = 200

def Eratosthenes(n):
	
	a = [True for x in range(2, n+1)]
	
	for i in range(2, n):
		for t in range(0,n+1, i):
			a[t] = False
	print a


 
def FindPrimes(limit):
    isPrime = {}
 
    isPrime[1] = False
    for i in range(2, limit + 1):
        isPrime[i] = True
 
    checkLimit = int(math.sqrt(limit)) + 1
    for i in range(2, checkLimit):
        if isPrime[i]:
            for factor in range(2, limit + 1):
                j = i * factor
                if (j > limit): break
                isPrime[j] = False
 
    primes = []
    for i in range(1, limit + 1):
        if isPrime[i]:
            primes.append(i)
 
    print sum(primes)

FindPrimes(2000000)