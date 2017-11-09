# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

# DP similar to climb stairs
class Solution(object):
    def numDecodings(self, s):
        """
        O(n)
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0 for _ in range(len(s)+1)]
        if len(s) == 1 and s[0] = '0':
        	return 0
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i>=2 and 10 <= int(s[i-2:i]) and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]