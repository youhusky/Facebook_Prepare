# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# binary search !
# http://community.bittiger.io/topic/241/%E4%B8%80%E8%B5%B7lintcode-%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE%E7%9C%8B%E8%BF%99%E7%AF%87%E5%B0%B1%E5%A4%9F%E4%BA%86/2
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        # contain two possible solutions
        while l + 1 < r:
            mid = l + (r-l)/2
            
            if nums[mid] == target:
                return mid
        
            # case 1 over pivot
            if nums[mid] < nums[l]:
            	# imp corner
                if nums[mid] < target and target <= nums[r]:
                    l = mid
                else:
                    r = mid
            # case 2 before pivot
            else:
            	# imp corner
                if nums[l] <= target and target < nums[mid]:
                    r = mid
                else:
                    l = mid
        # corner case
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        return -1

# follow up duplicate
#             # only add this line
            # else:
            #     l += 1
# 81. Search in Rotated Sorted Array II
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        l, r = 0, len(nums)-1
        # contain two possible solutions
        while l + 1 < r:
            mid = l + (r-l)/2
            
            if nums[mid] == target:
                return True
        
            # case 1 over pivot
            if nums[mid] < nums[l]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid
                else:
                    r = mid
            # case 2 before pivot
            elif nums[mid] > nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid
                else:
                    l = mid
            # only add this line
            else:
                l += 1
        # corner case
        if nums[l] == target:
            return True
        if nums[r] == target:
            return True
        
        return False
                
            
        
