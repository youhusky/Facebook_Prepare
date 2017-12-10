# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(candidates, target, res,[],0)
        return res
    def backtracking(self, candidates, target, res, temp,start):
        if target < 0:
            return 
        elif target == 0:
            res.append(list(temp))
        else:
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                self.backtracking(candidates, target-candidates[i], res, temp,i)
                temp.pop()
        