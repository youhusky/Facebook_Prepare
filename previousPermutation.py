# 2764135 
# 2764135 
# 2763145 
# 2763541 
def previousPermutation(nums):
	if not nums:
		return nums
	j = 0
	# find
	for i in range(len(nums)-1, -1, -1):
		if nums[i-1] > nums[i]:
			j = i-1
			break

	# change
	for i in range(len(nums)-1, -1, -1):
		if nums[i] < nums[j]:
			nums[i], nums[j] = nums[j], nums[i]
			nums[j+1:] = reversed(nums[j+1:])
			return

nums = [2,7,6,4,1,3,5]
previousPermutation(nums)
print nums