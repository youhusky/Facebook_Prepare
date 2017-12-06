class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, num,target, 0, 0, "")
        return res

    def dfs(self, res, num, target, start, curr, temp):
    	# to the last number
    	if start == len(num):
    		if curr == target:
    			res.append(temp)
    		return

    	for i in range(start+1, len(num)+1):
    		# string
    		expr = num[start:i]
    		val = int(expr)

    		if num[start] == '0'and i != start+1:
    			break
    		if start == 0:
    			self.dfs(res, num, target, i, val, expr)
    		else:
    			self.dfs(res, num, target, i, curr+val, temp+'+'+expr)
    			self.dfs(res, num, target, i, curr-val, temp+'-'+expr)
m = Solution()
print m.addOperators("12345", 1239)