# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        O(nlgn)
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        res = 0
        pq = []
        for i in intervals:
            while pq and i.start >= pq[0]:
                heappop(pq)
            heappush(pq, i.end)
            res = max(res, len(pq))
        return res
            
        