# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".

# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        O(N)
        O(1)
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return ""
        if not t:
            return ""
        useddict = defaultdict(int)
        for char in t:
            useddict[char] += 1
            
        minlength = len(s) + 1
        length = len(t)
        l, r = 0, 0
        res = ""
        
        while r < len(s):
            if s[r] in useddict:
                useddict[s[r]] -= 1
                # only valid char in t will minus length
                if useddict[s[r]] >= 0:
                    length -= 1
            r += 1
            while length == 0:
                if minlength >= r-l:
                    minlength = r-l
                    res = s[l:r]
                
                if s[l] in useddict:
                    useddict[s[l]] += 1
                    # avoid duplicate
                    if useddict[s[l]] > 0:
                        length += 1
                l += 1
        return res
                
                
