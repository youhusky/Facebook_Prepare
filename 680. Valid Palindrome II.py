# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
class Solution(object):
    def validPalindrome(self, s):
        """
        O(N)
        O(1)
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        # check which one need to delete
        c1, c2 = 0, 0
        while l < r:
            if s[l] != s[r]:
                l += 1
                c1 += 1
            else:
                l += 1
                r -= 1
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                r -= 1
                c2 += 1
            else:
                l += 1
                r -= 1
        return c1 <2 or c2 < 2