
def isPalindromicNumber(number):
	if str(number) == str(number)[::-1]:
		return True
	else:
		return False

for num1 in range(900, 1000):
	for num2 in range(900, 1000):
		if(isPalindromicNumber(num1 * num2)):
			print(num1, num2, num1 * num2)