sum = 2

n0 = 1
n1 = 2

for num in range(10000000):
	n0 = n1 + n0
	if n0 > 4000000:
		break
	if n0 % 2 == 0:
		sum += n0
	n1 = n0 + n1
	if n1 > 4000000:
		break
	if n1 % 2 == 0:
		sum += n1

print(sum)