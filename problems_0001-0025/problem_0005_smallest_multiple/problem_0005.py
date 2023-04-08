n = 2520

found = False

while found == False:
	counter = 0
	for i in range(20, 0, -1):
		#print n % i
	
		if n % i == 0:
			counter += 1
		else:
			break

	if counter == 20:
		found = True
		print n
		print found
	n += 2520
