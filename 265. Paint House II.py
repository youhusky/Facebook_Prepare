# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Follow up:
# Could you solve it in O(nk) runtime?
# DP problem
class Solution(object):
    def minCostII(self, costs):
        """
        # O(nk)
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))] 
        for i in range(len(costs[0])):
            dp[0][i] = costs[0][i]
        for j in range(1,len(costs)):
            for k in range(len(costs[0])):
                dp[j][k] = self.minCost(dp[j-1], k) + costs[j][k]
        return self.minCost(dp[-1], -1)

    def minCost(self, dp, k):
        res = float('inf')
        for i in range(len(dp)):
            if i == k:
                continue
            else:
                res = min(res, dp[i])
        return res