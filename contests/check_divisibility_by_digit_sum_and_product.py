from typing import List


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original_no = n
        digit_sum = 0
        digit_product = 1

        while n != 0:
            unit_digit = n % 10
            digit_sum += unit_digit
            digit_product *= unit_digit
            n //= 10

        if digit_sum + digit_product == 0:
            return False

        return original_no % (digit_sum + digit_product) == 0


sol = Solution()

n = 99
print(f"{n = }  {sol.checkDivisibility(n) = }")

n = 23
print(f"{n = }  {sol.checkDivisibility(n) = }")