from itertools import combinations

num_list = [num for num in range(1, 101)]

sum = 0

combos = combinations(num_list, 2)

for comb in combos:
	sum = sum + (comb[0] * comb[1])

sum *= 2
print(sum)