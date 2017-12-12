# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
from collections import defaultdict
class Solution(object):
    def findErrorNums(self, nums):
        """
        O(n)
        O(n)
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for i in range(1, len(nums)+1):
            if i in dic:
                if dic[i] == 2:
                    dup = i
            else:
                missing = i
        return [dup, missing]
