# Given two strings S and T, determine if they are both one edit distance apart.
# Divide into three part
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # case 1
        if abs(len(s) - len(t)) > 1:
            return False

        # case 2
        if len(s) == len(t):
            count = 0
            for i in range(len(s)):
                if s[i] == t[i]:
                    continue
                else:
                    count += 1
                if count > 1:
                    return False
            return False if count == 0 else True

        # case 3
        if len(s) > len(t):
            s,t = t, s
        if not s:
            return True
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i:] == t[i+1:]
        return True
        
