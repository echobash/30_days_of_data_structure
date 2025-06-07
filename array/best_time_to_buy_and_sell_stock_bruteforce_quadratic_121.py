from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(n):
            for j in range(i+1, n):
                profit = max(profit, prices[j] - prices[i])
        return profit


sol = Solution()

prices = [7,1,5,3,6,4]
print(f" {prices = } | {sol.maxProfit(prices) = }")

prices = [7,6,4,3,1]
print(f" {prices = } | {sol.maxProfit(prices) = }")

prices = [7,6,5,3,6,9]
print(f" {prices = } | {sol.maxProfit(prices) = }")
