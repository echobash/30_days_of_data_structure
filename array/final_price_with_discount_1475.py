class Solution:
    def finalPrices(self, prices: [int]) -> [int]:
        n = len(prices)

        # prices = [8,4,6,2,3] 5

        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices


sol = Solution()

prices = [8,4,6,2,3]
print(prices, sol.finalPrices(prices))

prices = [1,2,3,4,5]
print(prices, sol.finalPrices(prices))

prices = [10,1,1,6]
print(prices, sol.finalPrices(prices))
