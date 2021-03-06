# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        O(n)
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
# Follow up at most k times
    def removeDuplicates(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        i = 0
        for n in nums:
            if i < k or n > nums[i-k]:
                nums[i] = n
                i += 1
        return i
