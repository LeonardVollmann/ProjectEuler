from itertools import permutations
p = sorted(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[1000000 - 1]
print sum([p[i] * (10 ** (9 - i)) for i in range(10)])