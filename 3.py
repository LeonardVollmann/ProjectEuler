target = 600851475143
primes = [2]

def is_prime(x):
	for i in range(0, len(primes)):
		if (primes[i] > x):
			return True

		if x % primes[i] == 0:
			return False
	return True

def next_prime(index):
	x = primes[index]
	while True:
		x += 1
		if is_prime(x):
			return x

count = 0
limit = target
while primes[count] < limit:
	p = next_prime(count)
	primes.append(p)

	if (target % primes[count] == 0):
		print(primes[count])
		limit = target / primes[count]

	count += 1

print(primes[len(primes) - 1])