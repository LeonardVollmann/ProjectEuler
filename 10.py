def sieve(n):
	primes = [True] * n
	primes[0] = primes[1] = False

	for (i, isPrime) in enumerate(primes):
		if isPrime:
			yield i
			for j in xrange(i*i, n, i):
				primes[j] = False

print(sum(sieve(2000000)))