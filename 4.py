def check_palindrome(n):
	s = str(n)
	return s[::-1] == s

palindromes = []

for i in range(100, 1000):
	for j in range(100, 1000):
		if check_palindrome(i * j):
			palindromes.append(i * j)

answer = 0
for i in range(0, len(palindromes)):
	if (palindromes[i] > answer):
		answer = palindromes[i]

print(answer)