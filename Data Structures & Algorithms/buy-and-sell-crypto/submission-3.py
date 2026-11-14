class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        max_price = 0

        for n in prices:
            if n < minn:
                minn = n
                continue

            price = n - minn
            if price > max_price:
                max_price = price

        return max_price

        