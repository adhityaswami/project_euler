import math

def isPrime(number):
	for factor in range(2, math.ceil(math.sqrt(number)) + 1):
		if number % factor == 0:
			return False
	return True

for newFactor in range(2, 600851475143 // 2):
	if 600851475143 % newFactor == 0 and isPrime(newFactor):
		print(newFactor)