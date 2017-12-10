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
        res = []
        self.backtracking(nums, res, [])
        return res
    def backtracking(self, nums, res, temp):
        if len(temp) == len(nums):
            res.append(list(temp))
        for num in nums:
            if num in temp:
                continue
            #temp.append(num)
            print temp
            self.backtracking(nums,res,temp+[num])
            #temp.pop()
        
m = Solution()
print m.permute([1,2,3])

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
