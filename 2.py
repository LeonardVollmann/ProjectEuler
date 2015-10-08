nums = []
current = 1
while current < 4000000:
	nums.append(current)
	if current == 1:
		current = 1 + 1
	else:
		l = len(nums)
		current = nums[l - 1] + nums[l - 2]

sum = 0
for i in range(len(nums)):
	if (nums[i] % 2 == 0):
		sum += nums[i]

print(sum)