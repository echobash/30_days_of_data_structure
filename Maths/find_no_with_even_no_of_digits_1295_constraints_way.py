from math import log10, floor
from typing import List


class Solution:
    ## Using constraints
    # 1<=num>100000
    # or 10<=num>9999 or num = 100000
    # or 10<=num>99
    # or 1000<=num>9999
    # Conclustion ->  10<=num>99 or 1000<=num>9999 or num = 100000
    def findNumbers(self, nums: List[int]) -> int:
        numbers_with_even_no_of_digits = 0
        for num in nums:
            if 10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000:
                print(num, 10 <= num >= 99)
                numbers_with_even_no_of_digits += 1
        return numbers_with_even_no_of_digits


sol = Solution()

nums = [12,345,2,6,7896]
print(f"{nums = } {sol.findNumbers(nums) = }")

nums = [555,901,482,1771]
print(f"{nums = } {sol.findNumbers(nums) = }")


nums = [5535,9031,482,0]
print(f"{nums = } {sol.findNumbers(nums) = }")

