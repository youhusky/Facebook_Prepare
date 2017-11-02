# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
class Solution(object):
    def hIndex(self, citations):
        """
        O(lgn)
        binary search templete
        :type citations: List[int]
        :rtype: int
        """
        l, r = 0, len(citations) -1
        n = len(citations)
        while l <= r:
            mid = l + (r-l)/2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] > n - mid:
                r = mid -1
            else:
                l = mid + 1
        return n- l
            
