# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.backtracking(nums, [], ans)
        return ans
    def backtracking(self, nums, temp, ans):
        if len(nums) == len(temp):
            ans.append(list(temp))
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.backtracking(nums, temp, ans)
            temp.pop()

class Solution(object):
	# [1] [2,1],[1,2], [3,2,1],[2,3,1]
    def permute(self, nums):
        perms = [[]]   
        for n in nums:
            temp = []
            for perm in perms:
                for i in range(len(perm)+1):   
                    temp.append(perm[:i] + [n] + perm[i:])   ###insert n
                    
            perms = temp
        return perms
