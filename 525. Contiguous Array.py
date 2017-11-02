# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

class Solution(object):
    def findMaxLength(self, nums):
        """
        O(n)
        O(n)
        :type nums: List[int]
        :rtype: int
        """
        zero, one = 0, 0
        dic = {}
        res = 0
        # init
        dic[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
            if (zero - one) in dic:
                res = max(res, i - dic[zero-one])
            else:
                dic[zero-one] = i
        return res
