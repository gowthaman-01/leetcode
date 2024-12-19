class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 1, 0
        
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        
        return profit