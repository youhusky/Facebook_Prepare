# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        O(mn)
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) -1:
                    return i
        return -1
                    
                    
