from math import gcd
from typing import List


class Solution:
    def isCoprime(self, num1, num2):
        return gcd(num1, num2) == 1

    def getFirstDigit(self, num):
        while num >= 10:
            num //= 10
        return num

    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isCoprime(self.getFirstDigit(nums[i]), nums[j] % 10):
                    print(f"{nums[i]}, {nums[j]}")
                    count += 1
        return count


sol = Solution()

nums = [2,5,1,4]
print(f"{nums = } | {sol.countBeautifulPairs(nums) = }")

nums = [11,21,12]
print(f"{nums = } | {sol.countBeautifulPairs(nums) = }")

nums = [31,25,72,79,74]
print(f"{nums = } | {sol.countBeautifulPairs(nums) = }")
