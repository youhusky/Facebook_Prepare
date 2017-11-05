# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.

# Example:

# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);

# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);

# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
# Solution: Reservoir Sampling
# For the nth target, count is n. Then the probability that rnd.nextInt(count)==1 is 1/n. Thus, the probability that return nth target is 1/n.
# For (n-1)th target, the probability of returning it is (n-1)/n * 1/(n-1)= 1/n......
import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        count = 1
        for i in range(len(self.nums)):
            if self.nums[i] != target:
                continue
            else:
                # start at 1
                if random.randint(1,count) == 1:
                    # save for index
                    res = i
                count += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)