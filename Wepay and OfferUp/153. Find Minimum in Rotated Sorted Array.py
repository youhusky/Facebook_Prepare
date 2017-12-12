# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.
class Solution(object):
    def findMin(self, nums):
        """
        O(logn)
        O(1)
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right and nums[left]> nums[right]:
            middle = left + (right-left)/2
            if nums[middle] > nums[right]:
                # left-middle is increasing
                left = middle + 1
            else:
                right = middle
        return nums[left]
                
