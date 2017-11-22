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

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            # start from 0 otherwise start last diff num
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res