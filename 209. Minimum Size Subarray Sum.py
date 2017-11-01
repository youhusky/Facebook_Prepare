# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

# click to show more practice.
# Binary Search
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        minlength = len(nums)+1
        l, r = 0, 0
        while r < len(nums):
            res += nums[r]
            r += 1
            while res >= s:
                minlength = min(minlength, r-l)
                # move right step
                res -= nums[l]
                l += 1
            
        return 0 if minlength == len(nums) +1 else minlength
