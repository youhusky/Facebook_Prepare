# Implement pow(x, n).
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
        	return self.myPow(x,-n)
        if n == 0:
        	return 1.0
        if n % 2 == 0:
        	return self.myPow(x*x, n/2)
        else:
        	return x * self.myPow(x*x, n/2)