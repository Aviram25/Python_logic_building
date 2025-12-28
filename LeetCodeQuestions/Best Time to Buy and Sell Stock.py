class Solution(object):
    def maxProfit(self, prices):
        buy = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            max_profit = max(max_profit,prices[i] - buy)    
        return max_profit
