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