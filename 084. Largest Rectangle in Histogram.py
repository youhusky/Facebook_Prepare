# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        O(n)
        :type heights: List[int]
        :rtype: int
        """
        length = len(heights)
        stack =  []
        maxArea = 0
        for i in range(length+1):
            height = heights[i] if i!= length else 0
            while stack and height <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                maxArea = max(maxArea, h*w)
            stack.append(i)
        return maxArea
        
