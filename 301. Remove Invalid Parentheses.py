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

    def check(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
    def removeInvalidParentheses2(self, s):
        res = []
        if not s:
            return res
        visited = set()
        queue = []

        # init
        # deal with diplicate
        visited.add(s)
        queue.append(s)

        flag = False

        while queue:
            t = queue.pop(0)
            if self.check(t):
                res.append(t)
                
                flag = True
                continue

            # check equal length with minimal delete times
            # if length(t) == 5 first is true
            # then we only need to generate length == 5 others to append res
            if flag:
                continue

            for i in range(len(t)):
                if t[i] != '(' and t[i] != ')':
                    continue
                temp = t[:i] + t[i+1:]
                if temp in visited:
                    continue
                visited.add(temp)
                queue.append(temp)
        return res


m = Solution()
print m.removeInvalidParentheses2(s)


        