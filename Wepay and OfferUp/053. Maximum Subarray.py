# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        index=0
        prevMax = nums[0]
        res = nums[0]
        for each in range(1,len(nums)):
            prevMax = max(prevMax+nums[each], nums[each])
            if res < prevMax:
            	index = each
            	res = prevMax
            #res = max(res, prevMax)

        print res
        t = []
        while res!=0:
        	t.append(nums[index])
        	
        	res -= nums[index]
        	index -= 1
        
        return t[::-1]
m = Solution()
print m.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])