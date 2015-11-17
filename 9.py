def findTriplet(nums, target):
	for i in range(0, len(nums)):
		a = nums[i]
		for j in range(i, len(nums)):
			b = nums[j]
			c = target - (a + b)
			if a*a + b*b == c*c:
				return a, b, c

nums = range(1, 1000)
result = findTriplet(nums, 1000)
print(result[0] * result[1] * result[2])