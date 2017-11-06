# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums)< 3:
            return res
        nums = sorted(nums)
        for i in range(len(nums)-2):
            # dup
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l+= 1
                elif s > 0:
                    r -=1
                else:
                    res.append((nums[i], nums[l],nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

    def threeSum2(self, nums):
        def hashing(string):
            minvalue = min(string)
            maxvalue = max(string)
            return str(minvalue)+str(maxvalue)
        res = []
        helper = set()
        # wit dup
        # res = []
        if len(nums) < 3:
            return res
        for i in range(len(nums)):
            dic = {}
            for j in range(i+1,len(nums)):
                dic[nums[j]] = j
                if -nums[i]-nums[j] in dic:
                    temp = (nums[i], nums[dic[- nums[i]-nums[j]]], nums[j])
                    # IMP
                    if hashing(temp) not in helper:
                        helper.add(hashing(temp))
                        res.append(temp)
                
        return res


test = [-1, 0, 1, 2, -1, -4]
m = Solution()
print m.threeSum2(test)
