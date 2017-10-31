# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n:
            n -= 1
            res.insert(0, chr((n % 26) + ord('A')) )
            
            n /= 26
        return "".join(res)
        