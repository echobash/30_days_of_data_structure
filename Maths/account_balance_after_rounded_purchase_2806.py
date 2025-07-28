class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount

        if purchaseAmount % 10 >= 5:
            return 100 - ((purchaseAmount // 10) + 1) * 10
        else:
            return 100 - (purchaseAmount // 10) * 10


sol = Solution()

purchaseAmount = 9
print(f"{purchaseAmount = } {sol.accountBalanceAfterPurchase(purchaseAmount) = }")

purchaseAmount = 15
print(f"{purchaseAmount = } {sol.accountBalanceAfterPurchase(purchaseAmount) = }")

purchaseAmount = 10
print(f"{purchaseAmount = } {sol.accountBalanceAfterPurchase(purchaseAmount) = }")

purchaseAmount = 11
print(f"{purchaseAmount = } {sol.accountBalanceAfterPurchase(purchaseAmount) = }")

purchaseAmount = 5
print(f"{purchaseAmount = } {sol.accountBalanceAfterPurchase(purchaseAmount) = }")

purchaseAmount = 68
print(f"{purchaseAmount = } {sol.accountBalanceAfterPurchase(purchaseAmount) = }")

purchaseAmount = 62
print(f"{purchaseAmount = } {sol.accountBalanceAfterPurchase(purchaseAmount) = }")