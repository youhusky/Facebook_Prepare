# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        O(2^N)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # imp
        nums = sorted(nums)
        self.backtracking(nums, [], res, 0)
        return res
    def backtracking(self, nums, temp, res, start):
        res.append(list(temp))
        for i in range(start,len(nums)):
        	# Detect dup
            if i > start and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.backtracking(nums, temp, res, i+1)
            temp.pop()