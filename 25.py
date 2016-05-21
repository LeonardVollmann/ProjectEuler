def fib():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

for index, n in enumerate(fib()):
	if len(str(n)) == 1000:
		print(index)
		break