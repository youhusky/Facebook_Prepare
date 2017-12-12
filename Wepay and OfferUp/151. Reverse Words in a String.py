# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution(object):
    def reverseWords(self, s):
        """
        O(n)
        O(n)
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        li = s.strip().split()
        res = []
        for each in range(len(li)-1,-1,-1):
            res.append(li[each])
        return ' '.join(res)
