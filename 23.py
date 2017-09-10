from math import sqrt

limit = 28123 + 1

def d(n):
	s = 0
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			j = (n / i)
			s += i + j if i != j else i

	return s - n

abundants = [n for n in range(limit) if d(n) > n]

sums = []
for i, a in enumerate(abundants):
	for b in abundants[i:]:
		if a + b < limit:
			sums.append(a + b)

print sum(range(limit)) - sum(set(sums)) # total sum - sum of sums of abundants = sum of non-sums of abundants