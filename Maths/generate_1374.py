from typing import List


class Solution:
    def generateTheString(self, n: int) -> str:
        """
        n = even -> odd+odd
        n = odd -> odd + odd + odd
        """
        if n == 1:
            return "a"

        if n % 2 == 0:
            return "a" + (n - 1) * "b"
        else:
            if n == 3:
                return "abc"
            return "a" + 3 * "b" + (n - 4) * "c"


sol = Solution()

n = 1
print(f"{n = } {sol.sumZero(n) = }")

n = 2
print(f"{n = } {sol.sumZero(n) = }")

n = 3
print(f"{n = } {sol.sumZero(n) = }")

n = 4
print(f"{n = } {sol.sumZero(n) = }")

n = 5
print(f"{n = } {sol.sumZero(n) = }")

n = 468
print(f"{n = } {sol.sumZero(n) = }")