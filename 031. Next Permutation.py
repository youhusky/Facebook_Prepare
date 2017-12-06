class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        # j - position
        if not nums:
            return nums
        j = 0 
        # find
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] < nums[i]:
                j = i - 1
                break

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j+1:] = sorted(nums[j+1:])
                return












        if not nums:
            return nums
        i = len(nums)
        j = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1] < nums[i]:
                j = i-1
                break
        for i in range(len(nums)-1, -1,-1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j+1:] = sorted(nums[j+1:])
                return 