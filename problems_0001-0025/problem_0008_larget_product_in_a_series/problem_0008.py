from operator import mul

with open("Problem 8.txt", "r") as f:
	numbers = f.readline().strip()
	numbers = str(numbers)

listnumbers = []

for i in numbers:
	listnumbers.append(int(i))

besttotal = 0

for i in range(0, len(listnumbers) - 13):
	runningtotal = 1
	for n in range(0, 13):
		runningtotal *= listnumbers[i + n]
	print runningtotal
	if runningtotal > besttotal:
		besttotal = runningtotal

print besttotal




