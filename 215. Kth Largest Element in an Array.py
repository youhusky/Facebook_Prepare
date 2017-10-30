# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        O(nlgk)
        O(k)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
