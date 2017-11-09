# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# Change the items with 0 to first and 2 to the last
class Solution(object):
    def sortColors(self, nums):
        """
        O(n)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, blue = 0 ,len(nums)-1
        i = 0 
        while i <= blue:
            if nums[i] == 0:
                # change i, red index item
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            else:
                i += 1

    def sortCate(self, nums):
        def cate(n):
            if n < 3:
                return 'low'
            elif n < 6:
                return 'medium'
            else:
                return 'high'
        low, high = 0, len(nums)-1
        i = 0
        while i <= high:
            if cate(nums[i]) == 'low':
                nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif cate(nums[i]) == 'high':
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                i += 1

m = Solution()
test = [5,7,1,7,5,3,1,8,9,1]
m.sortCate(test)
print test
