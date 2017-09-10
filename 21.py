from math import sqrt

def d(n):
	s = 0
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			j = (n / i)
			s += i + j if i != j else i

	return s - n

d = [d(n) for n in range(10000)]

amicables = []
for a in range(2, 10000):
	b = d[a]
	if b >= 10000:
		continue

	if d[b] == a and a != b:
		amicables.append(a)
		amicables.append(b)

print sum(set(amicables))