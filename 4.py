def check_palindrome(n):
	s = str(n)
	return s[::-1] == s

palindromes = []

for i in xrange(100, 1000):
	for j in xrange(100, 1000):
		if check_palindrome(i * j):
			palindromes.append(i * j)

answer = 0
for i in xrange(0, len(palindromes)):
	if (palindromes[i] > answer):
		answer = palindromes[i]

print(answer)