# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set()
        nums = sorted(nums)
        self.backtracking(nums, [], res, visited)
        return res
        
    def backtracking(self, nums, temp, ans, visited):
        if len(temp) == len(nums):
            ans.append(list(temp))
        for i in range(len(nums)):
            if i in visited or i>0 and nums[i]==nums[i-1] and i-1 not in visited:
                continue
            temp.append(nums[i])
            visited.add(i)
            self.backtracking(nums, temp, ans, visited)
            visited.remove(i)
            temp.pop()
        

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set()
        self.backtracking(res, nums,[],visited)
        return res

    def backtracking(self, res, nums, temp,visited):
        if len(temp) == len(nums) and temp not in res:
            res.append(list(temp))
        for i in range(len(nums)):
            if nums[i] in temp and i in visited:
                continue
            visited.add(i)
            temp.append(nums[i])
            self.backtracking(res, nums, temp, visited)
            visited.remove(i)
            temp.pop()
            