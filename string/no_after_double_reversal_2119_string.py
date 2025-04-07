class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return str(num)[-1] != '0'


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
