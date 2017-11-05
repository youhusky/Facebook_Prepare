# Remove the minimum number of invalid removeInvalidParenthesesntheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
# Credits:
# Special thanks to @hpplayer for adding this problem and creating all test cases.

# simplify - only return one result
s = "()(()()"
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        checkforword = self.valid(s,'(',')')
        checkbackword = self.valid(checkforword[::-1],')','(')
        return checkbackword[::-1]
    def valid(self, s, left ,right):

        count = 0
        i = 0
        while i < len(s):
        	if s[i] == left:
        		count += 1
        	elif s[i] == right:
        		count -= 1
        	if count < 0:
        		s = s[:i] + s[i+1:]
        		i -= 1
        		count = 0
        	i += 1
        return s
m = Solution()
print m.removeInvalidParentheses(s)


        