# A message containing letters from A-Z is being encoded to numbers using the following mapping way:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

# Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

# Also, since the answer may be very large, you should return the output mod 109 + 7.

# Example 1:
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
# Example 2:
# Input: "1*"
# Output: 9 + 9 = 18
# Note:
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.

# So many case need to consider about
# http://www.cnblogs.com/grandyang/p/7279152.html
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10**9+7
        dp = [0 for i in range(len(s)+1)]
        
        dp[0] = 1
        if s[0] =='*':
            dp[1] = 9
        elif s[0] == '0':
            return 0
        else:
            dp[1] = 1
        
        for i in range(2,len(s)+1):
            
            if s[i-1] == '0':
                # only 10,20 two case which cause no other way
                if s[i-2] == '1' or s[i-2] == '2':
                    dp[i] += dp[i-2]
                # '*' reperesent 1 or 2
                elif s[i-2] == '*':
                    dp[i] += 2 * dp[i-2]  
                else:
                    dp[i] = 0
            elif ord('1') <= ord(s[i-1]) and ord(s[i-1]) <= ord('9'):
                
                # can seperate
                dp[i] += dp[i-1]
                # contains other way
                if s[i-2] == '1' or s[i-2] == '2' and ord(s[i-1]) <= ord('6'):
                    dp[i] += dp[i-2]
                elif s[i-2] == '*':
                    # 10 ~26
                    if ord(s[i-1]) <= ord('6'):
                        dp[i] += 2*dp[i-2]
                    else:
                        dp[i] += dp[i-2]
            else:
                dp[i] += 9 * dp[i-1]
                # divide 1 + *
                if s[i-2] == '1':
                    dp[i] += 9*dp[i-2]
                # 2 + *
                elif s[i-2] == '2':
                    dp[i] += 6*dp[i-2]
                # sum case 1 and 2
                elif s[i-2] == '*':
                    dp[i] += 15*dp[i-2]
            dp[i] = dp[i] % mod
        return dp[-1]
                        
                    