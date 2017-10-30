# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        O(2^N)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(nums, [], res, 0)
        return res
    def backtracking(self, nums, temp, res, start):
        res.append(list(temp))
        for i in range(start,len(nums)):
            temp.append(nums[i])
            self.backtracking(nums, temp, res, i+1)
            temp.pop()
        
        