class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        # Double reversal won't lead to the same no iff the last digit is 0
        return num % 10 != 0


sol = Solution()

num = 526
print(f"{num = } {sol.isSameAfterReversals(num) = }")

num = 2021
print(f"{num = } {sol.isSameAfterReversals(num) = }")

num = 0
print(f"{num = } {sol.isSameAfterReversals(num) = }")

num = 526000
print(f"{num = } {sol.isSameAfterReversals(num) = }")

num = 20210
print(f"{num = } {sol.isSameAfterReversals(num) = }")
