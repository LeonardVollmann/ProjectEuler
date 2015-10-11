sumOfSquares = 0
squareOfSums = 0
for i in range(1, 101):
	squareOfSums += i
	sumOfSquares += i * i

squareOfSums *= squareOfSums

print(squareOfSums - sumOfSquares)