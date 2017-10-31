# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# carry!
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        i,j = len(a) -1, len(b)-1
        carry = 0
        while i>=0 or j>=0:
            if i >= 0:
                carry += int(a[i]) - 0
                i -= 1
            if j >= 0:
                carry += int(b[j]) - 0
                j-=1
            res = str(carry % 2) + res
            carry /= 2
        return res if carry != 1 else '1' + res