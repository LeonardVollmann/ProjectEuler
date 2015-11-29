from math import sqrt

def getNumFactors(n):
	root = sqrt(n)
	iroot = int(root)
	count = -1 if root == iroot else 0
	for candidate in xrange(1, iroot):
		if n % candidate == 0:
			count += 2
	return count

n = 0
iteration = 0
while getNumFactors(n) <= 500:
	iteration += 1
	n += iteration

print n