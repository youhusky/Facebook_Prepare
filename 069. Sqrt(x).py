# Implement int sqrt(int x).

# Compute and return the square root of x.
class Solution(object):
    def mySqrt(x):
    	if x <= 1:
    		return 1
    	left, right = 1, x
    	ans = right
    	while left <= right:
    		mid = left + (right - left) /2
    		if mid <= x / mid:
    			left = mid + 1
    			ans = mid
    		else:
    			right = mid - 1
    	return ans
