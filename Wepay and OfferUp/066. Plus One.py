# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cnt = 1
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i] + cnt
            digits[i] = temp % 10
            cnt = temp / 10
        if cnt:
            digits.insert(0,1)
        return digits