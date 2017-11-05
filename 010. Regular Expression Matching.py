# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

# reference to Tushar youtube video which is amazing
# dp[i][j] = { dp[i-1][j-1] --s[i] == p[j] or p[j] == '.'
#				dp[i][j-2] -- if p[j] == '*'
#				dp[i-1][j] -- if s[i] == p[j-1] or p[j-1] == '.'
	
#   }
class Solution(object):
    def isMatch(self, s, p):
        """
        O(mn)
        O(mn)
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp =[[False for _ in range(len(p)+1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        
        for i in range(1,len(p)+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p) + 1):
                # case 1
                if p[j-1] =='.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] =='*':
                    # case 2
                    # init
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        # * means nothing for this index
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
                    
