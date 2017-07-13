def mode(nums):
	tally = {}
	M = nums[0]
	for x in nums:
		tally[x] = tally.get(x, 0) + 1
		if tally[x] > tally[M]:
			M = x

return M


def maximum(nums):
	M = nums[0]
	for x in nums:
		if x > M:
			M = x

return M

def minimum(nums):
	M = nums[0]
	for x in nums:
		if x < M:
			M = x

return M

def mean(nums):
	if len(nums) ==0:
		return None

	M = 0
	for x in nums:
		M += x

	M /= len(nums)
	return M

return M

#print("The mode is"+str(mode([1, 2, 3, 1, 2, 3, 1])))

#print("The mode is "+str(M))


#scores = [1, 8, 7, 12, 2, -5, 0, 1, 1, 2]


