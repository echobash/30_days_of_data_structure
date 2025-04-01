from typing import List


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return n // 2
        return n


sol = Solution()

n = 4
print(f" {n = } | {sol.numberOfCuts(n) = }")

n = 1
print(f" {n = } | {sol.numberOfCuts(n) = }")

n = 3
print(f" {n = } | {sol.numberOfCuts(n) = }")