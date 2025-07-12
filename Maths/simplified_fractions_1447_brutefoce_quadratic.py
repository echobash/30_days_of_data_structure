from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                if gcd(i, j) != 1 or i >= j:
                    continue
                result.append(str(i) + "/" + str(j))
        return result


sol = Solution()

n = 2
print(f"{n = } {sol.simplifiedFractions(n) = }")

n = 3
print(f"{n = } {sol.simplifiedFractions(n) = }")

n = 4
print(f"{n = } {sol.simplifiedFractions(n) = }")

n = 10
print(f"{n = } {sol.simplifiedFractions(n) = }")
