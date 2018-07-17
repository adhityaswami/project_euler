def checkNum(number):
	for factor in range(1, 21):
		if number % factor != 0:
			return False
	return True

for num in range(2520, 1000000000000000000, 2520):
	if checkNum(num):
		print(num)
		break