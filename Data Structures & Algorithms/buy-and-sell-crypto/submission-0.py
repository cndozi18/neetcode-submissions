class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0

        for sell in range(len(prices)):
            while prices[buy] > prices[sell]:
                buy += 1
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)

        return max_profit

        