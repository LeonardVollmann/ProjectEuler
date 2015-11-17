def is_prime(x, primes):
	for i in xrange(0, len(primes)):
		if (primes[i] > x):
			return True

		if x % primes[i] == 0:
			return False
	return True

def next_prime(index, primes):
	x = primes[index]
	while True:
		x += 1
		if is_prime(x, primes):
			return x

primes = [2]
for i in xrange(0, 10000):
	p = next_prime(i, primes)
	primes.append(p)
	print(p)