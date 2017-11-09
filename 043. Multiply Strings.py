# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# must see the Leetcode First Discussion 

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        
        pos = [0 for _ in range(m+n)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                
                second_position = i+j
                first_position = i+j+1
                
                original = int(num1[i]) * int(num2[j])
                temp = original + pos[first_position]
                
                pos[second_position] += temp / 10 ## 15/10 = 1
                pos[first_position] = temp % 10 ## 15%10 = 5
        res = ""
        for i in pos:
            if not res and i == 0:
                continue
            res += str(i)
        return res if res else '0'
                
        