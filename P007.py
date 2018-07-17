import math

def isPrime(number):
	for factor in range(2, math.ceil(math.sqrt(number)) + 1):
		if number % factor == 0:
			return False
	return True

counter = 1

for num in range(2, 410401):
	if isPrime(num):
		counter += 1
		if counter == 10001:
			print(num)
			break