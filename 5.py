def check(n):
	for i in range(1, 20):
		if n % i != 0:
			return False
	return True

num = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

while True:
	if check(num):
		break

	num += 19

print(num)