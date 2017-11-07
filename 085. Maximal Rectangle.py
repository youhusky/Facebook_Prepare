# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.
class Solution(object):
    def maximalRectangle(self, matrix):
    	# O(m^2)
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                # count next level '1'
                height[i] = height[i] + 1 if row[i] == '1' else 0
                
            stack = []
            
            for i in range(n + 1):
                while stack and height[i] <= height[stack[-1]]:
                    h = height[stack.pop()]
                    # if not stack means left boundary is zero then width is i else is the stack[-1] index
                     w = i - 1 - stack[-1] if stack else i
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
