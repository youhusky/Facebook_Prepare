# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        # find sum-target in array
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
#       sum(P) - sum(N) = target
#       sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
#       2 * sum(P) = target + sum(nums)
        total = (sum(nums) + S) / 2
        # subset sum
        if S>total or (sum(nums) + S) % 2 == 1:
            return 0
        else:
            
            return self.helper(nums, total)
    def helper(self, nums, k):
        dp = [0 for _ in range(k+1)]
        dp[0] = 1
        #print dp
        for num in nums:
            #print num
            
            for i in range(k, num-1,-1):
                #print i
                dp[i] = dp[i] + dp[i-num]
            #print dp
        return dp[k]
m = Solution()
print m.findTargetSumWays([1,1,1,1,1],3)