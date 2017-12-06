# You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
# For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.
import heapq
class Solution(object):
    def smallestRange(self, nums):
        # O(nlgm)
        # O(m) -space
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = []
        end = nums[0][0]
        for i in range(len(nums)):
            # heapq -- value, index of list, index
            heapq.heappush(pq,[nums[i][0], i, 0])
            end = max(end, nums[i][0])
            
        minrange = float('inf')
        start = -1
        while len(pq) == len(nums):
            t = heapq.heappop(pq)
            if end - t[0] < minrange:
                minrange = end - t[0]
                start = t[0]
                
            if t[2] + 1 < len(nums[t[1]]):
                t[0] = nums[t[1]][t[2] + 1]
                t[2] += 1
                heapq.heappush(pq, (t))
                end = max(end, t[0])
                
        return [start, start+minrange]