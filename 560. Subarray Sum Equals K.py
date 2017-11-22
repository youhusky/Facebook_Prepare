# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# Simple
class Solution(object):
	def easysubarraySum(self, nums, k):
		if not nums:
			return False
		res = set()
		res.add(0)
		
		prevtotal = 0
		for num in nums:
			prevtotal += num
			res.add(prevtotal)
			if prevtotal - k in res:
				return True
		return False

m = Solution()
print m.easysubarraySum([2,5,7,-1],15)
