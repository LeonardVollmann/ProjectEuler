def collatz(i):
	if i == 0:
		return []
	seq = [i]
	while i > 1:
		if i % 2 == 0:
			i /= 2
		else:
			i = (3 * i) + 1
		seq.append(i)
	return seq

longest = 0
result = 0
for i in xrange(0, 1000000, 1):
	length = len(collatz(i))
	if length > longest:
		result = i
		longest = length

print(result)