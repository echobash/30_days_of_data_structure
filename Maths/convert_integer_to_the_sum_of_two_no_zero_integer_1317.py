from typing import List


class Solution:
    def has_zero_in_number(self, m):
        while m > 0:
            if m % 10 == 0:
                return True
            m //= 10
        return False

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n+1):
            search_value = n - i
            if not self.has_zero_in_number(i) and not self.has_zero_in_number(search_value):
                return [i, search_value]


sol = Solution()

n = 2
print(f"{n = } {sol.getNoZeroIntegers(n) = }")

n = 11
print(f"{n = } {sol.getNoZeroIntegers(n) = }")

n = 4102
print(f"{n = } {sol.getNoZeroIntegers(n) = }")
