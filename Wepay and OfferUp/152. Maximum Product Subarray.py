# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = nums[0]
        maxEndingHere = nums[0]
        minEndingHere = nums[0]
        for i in range(1, len(nums)):
            maxTemp = maxEndingHere
            maxEndingHere = max(maxEndingHere * nums[i], nums[i], minEndingHere * nums[i])
            minEndingHere = min(minEndingHere * nums[i], nums[i], maxTemp * nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar