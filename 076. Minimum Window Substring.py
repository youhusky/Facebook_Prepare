from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        O(n)
        O(1)
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        if not s or not t:
            return res
        # init
        dic = defaultdict(int)
        # sliding windows
        l,r = 0,0
        min_length = len(s)
        size = len(t)
        for char in t:
            dic[char] += 1
            
        while r < len(s):
            if s[r] in dic:
                if dic[s[r]] > 0:
                    size -= 1
                # value < 0 means duplicate char in s
                dic[s[r]] -= 1
            
            r += 1
            
            while size == 0:
                if min_length >= r-l:
                    min_length = r-l
                    res = s[l:r]
                
                # left bound
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        size += 1
                
                l += 1
        return res
                
        
