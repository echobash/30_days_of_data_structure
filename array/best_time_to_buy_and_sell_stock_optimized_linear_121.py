from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min_till_now = float('inf')

        for price in prices:
            if price < min_till_now:
                # Can buy at this
                min_till_now = price
            # Sell at every price and update max
            profit = max(profit, price - min_till_now)
        return profit


sol = Solution()

prices = [7,1,5,3,6,4]
print(f" {prices = } | {sol.maxProfit(prices) = }")

prices = [7,6,4,3,1]
print(f" {prices = } | {sol.maxProfit(prices) = }")

prices = [7,6,5,3,6,9]
print(f" {prices = } | {sol.maxProfit(prices) = }")
