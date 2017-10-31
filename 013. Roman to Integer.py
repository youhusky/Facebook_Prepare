# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# focus on the rule compare the previous number
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic ={'X':10,"V":5, 'I':1,'L':50,'C':100,'D':500,'M':1000}
        value = dic[s[-1]]
        for i in range(len(s)-2,-1,-1):
            # XX - 20
            if dic[s[i]] >= dic[s[i+1]]:
                value += dic[s[i]]
            # IV - 4
            else:
                value -= dic[s[i]]
        return value
