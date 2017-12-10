# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(res,n,k,[],1)
        return res
    def backtracking(self, res,n,k,temp,start):
        
        if k == 0:
            res.append(list(temp))
            #return
        else:
            for i in range(start, n+1):
                temp.append(i)
                self.backtracking(res,n,k-1,temp,i+1)
                temp.pop()
        