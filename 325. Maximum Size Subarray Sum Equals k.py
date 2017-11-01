# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

# Example 2:
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

# Follow Up:
# Can you do it in O(n) time?

# Use HashMap to store curSum and we save the longest result which means we lazy update the map
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        O(n)
        O(n)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, cursum = 0, 0
        dic = {}
        # res index == 0
        dic[0] = -1
        # save longest result
        for i in range(len(nums)):
            cursum += nums[i]
            
            if cursum not in dic:
                dic[cursum] = i
            
            # diff sum in prev nums
            if cursum - k in dic:
                ans = max(ans, i - dic[cursum-k])
        return ans
                
# min?
# min()
# dic init empty
        