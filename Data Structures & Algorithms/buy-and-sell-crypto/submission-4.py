class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_val = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - buy_val)
            buy_val = min(buy_val, prices[i])

        return max_profit
        