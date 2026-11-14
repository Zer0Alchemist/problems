class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for n in range(len(prices) - 1):
            for i in range(n + 1, len(prices)):
                if prices[i] > prices[n]:
                    val = prices[i] - prices[n]
                    if val > max_price:
                        max_price = val

        return max_price