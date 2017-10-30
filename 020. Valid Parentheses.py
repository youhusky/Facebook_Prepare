# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
    def isValid(self, s):
        """
        O(N)
        O(1)
        :type s: str
        :rtype: bool
        """
        dic = {')':'(', ']':'[', '}':'{'}
        stack = []
        for each_char in s:
            if each_char not in dic:
                stack.append(each_char)
            else:
                if stack and dic[each_char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if stack else True
