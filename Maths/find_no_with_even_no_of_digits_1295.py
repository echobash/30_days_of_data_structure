from math import log10, floor
from typing import List


class Solution:
    def hasEvenNoOfDigits(self,number):
        return (floor(log10(number)) + 1) % 2 == 0

    def findNumbers(self, nums: List[int]) -> int:
        numbers_with_even_no_of_digits = 0
        for num in nums:
            if num <= 0:
                continue

            if not self.hasEvenNoOfDigits(num):
                continue
            numbers_with_even_no_of_digits += 1
        return numbers_with_even_no_of_digits


sol = Solution()

nums = [12,345,2,6,7896]
print(f"{nums = } {sol.findNumbers(nums) = }")

nums = [555,901,482,1771]
print(f"{nums = } {sol.findNumbers(nums) = }")


nums = [5535,9031,482,0]
print(f"{nums = } {sol.findNumbers(nums) = }")

