from __future__ import print_function

words = [
	"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
	"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
	"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand", "and"
]
offset_ones = 0
offset_teens = 11
offset_tens = 20
offset_hundred = 28
offset_thousand = 29
offset_and = 30

chars = 0

def count_prefix(hundred):
	count = 0
	if hundred > 0:
		count += len(words[offset_ones + hundred])
		count += len(words[offset_hundred])
		count += len(words[offset_and])
		print(words[offset_ones + hundred], end=" ")
		print(words[offset_hundred], end=" ")
		print(words[offset_and], end=" ")
	return count

for hundred in xrange(10):
	if hundred > 0:
		chars += len(words[offset_ones + hundred])
		chars += len(words[offset_hundred])
		print(words[offset_ones + hundred], end=" ")
		print(words[offset_hundred], end=" ")

	for one in xrange(1, 11):
		chars += count_prefix(hundred)
		chars += len(words[offset_ones + one])
		print(words[offset_ones + one])

	for teen in xrange(9):
		chars += count_prefix(hundred)
		chars += len(words[offset_teens + teen])
		print(words[offset_teens + teen])

	for ten in xrange(8):
		for one in xrange(0, 10):
			chars += count_prefix(hundred)
			chars += len(words[offset_tens + ten])
			chars += len(words[offset_ones + one])
			print(words[offset_tens + ten], end="")
			if one > 0:
				print("-", end="")
			print(words[offset_ones + one])

chars += len(words[offset_ones + 1])
chars += len(words[offset_thousand])
print(words[offset_ones + 1], end=" ")
print(words[offset_thousand])

print(chars)