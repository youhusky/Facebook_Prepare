# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        #print path
        stack = []
        for i in path:
            #print i == ''
            if stack and i == '..':
                stack.pop()
            elif i != '' and i!= '.' and i!= '..':
                stack.append(i)
        res = list(stack)
        
        return "/" +"/".join(res)
            
   