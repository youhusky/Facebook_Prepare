# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

# Return the maximum profit you can make.

# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Note:

# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.

## DP

# This problem is just like the other stock problems.
# At given day, we can do 1 out of 4 things:

# buy stock
# hold stock
# do nothing with empty portfolio
# sell stock
# We have 4 arrays with the length of # of the days, recording the max profit at given day if we do given operation.

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        # DP
        buy = [0 for _ in range(len(prices))]
        sell = [0 for _ in range(len(prices))]
        # not sell
        hold = [0 for _ in range(len(prices))]
        # not buy after sell
        skip = [0 for _ in range(len(prices))]
        
        # IMP
        # init
        buy[0] = - prices[0]
        hold[0] = - prices[0]
        
        for i in range(1, len(prices)):
            buy[i] = max(skip[i-1], sell[i-1]) - prices[i]
            
            hold[i] = max(hold[i-1], buy[i-1])
            
            skip[i] = max(skip[i-1], sell[i-1])
            
            sell[i] = max(buy[i-1], hold[i-1]) + prices[i] - fee
            
        return max(buy[-1], hold[-1], skip[-1], sell[-1],0)

# But we really do not need so much dp
class Solution(object):
    def maxProfit(self, prices, fee):
    	# only consider the buy and sell
        N = len(prices)
        if not N:
            return 0
        buy = [0] * N
        sell = [0] * N
        buy[0] = -prices[0]
        for i in range(1, N):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)
        return max(sell[N - 1], 0)

# So based on that only previous status can relate to current status

class Solution(object):
    def maxProfit(self, prices, fee):
    	# only consider the buy and sell
        N = len(prices)
        if not N:
            return 0
        
        sell = 0
        buy = -prices[0]
        for i in range(1, N):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return max(sell, 0)

# 122. Best Time to Buy and Sell Stock II
# which is really the same as the 714
class Solution(object):
    def maxProfit(self, prices):
    	# only consider the buy and sell
        N = len(prices)
        if not N:
            return 0
        
        sell = 0
        buy = -prices[0]
        for i in range(1, N):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i])

        return max(sell, 0)

# 309. Best Time to Buy and Sell Stock with Cooldown
        # buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        # sell[i] = max(sell[i-1], buy[i-1] + prices[i])
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        # buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        # sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        
        b0 = -prices[0]
        b1 = b0
        s0 = 0
        s1 = 0
        s2 = 0
        
        for i in range(1,len(prices)):
            b1 = max(b0, s0 - prices[i])
            s2 = max(s1, b0 + prices[i])
            
            b0 = b1
            s0 = s1
            s1 = s2
        return s2
            
        
class Solution(object):
	def maxProfit(self, prices):
	    if len(prices) < 2:
	        return 0
	    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
	    for price in prices:
	        prev_buy = buy
	        buy = max(prev_sell - price, prev_buy)
	        prev_sell = sell
	        sell = max(prev_buy + price, prev_sell)
	    return sell
            

