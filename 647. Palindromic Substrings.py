# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        count = [0]
        for i in range(len(s)):
            self.check(s,i,i,count) # abcddcba  -- # abcdcba
            self.check(s,i,i+1, count)
        return count[0]
    def check(self, s, l, r, count):
        while l>=0 and r < len(s) and s[l] == s[r]:
            count[0] += 1
            l -= 1
            r += 1