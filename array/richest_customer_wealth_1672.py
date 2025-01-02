from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        m = len(accounts[0])

        max_wealth = 1
        for i in range(n):
            sum_of_wealth_of_customer_i = 0
            for j in range(m):
                sum_of_wealth_of_customer_i += accounts[i][j]
            if sum_of_wealth_of_customer_i > max_wealth:
                max_wealth = sum_of_wealth_of_customer_i
        return max_wealth


sol = Solution()

accounts = [[1,2,3],[3,2,1]]
print(accounts, sol.maximumWealth(accounts))

accounts = [[1,5],[7,3],[3,5]]
print(accounts, sol.maximumWealth(accounts))

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(accounts, sol.maximumWealth(accounts))