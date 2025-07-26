from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-1 * i)

        if n % 2 == 1:
            result.append(0)

        return result


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