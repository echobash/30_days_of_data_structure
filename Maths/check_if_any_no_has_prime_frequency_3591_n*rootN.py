from collections import Counter
from typing import List


class Solution:
    def isPrime(self, num):
        if num == 2:
            return True

        if num <= 1 or num % 2 == 0:
            return False

        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        num_freq = Counter(nums)
        for freq in num_freq.values():
            if self.isPrime(freq):
                return True
        return False


sol = Solution()

nums = [1,2,3,4,5,4]
print(f"{nums = } {sol.checkPrimeFrequency(nums) = }")

nums = [1,2,3,4,5]
print(f"{nums = } {sol.checkPrimeFrequency(nums) = }")

nums = [2,2,2,4,4]
print(f"{nums = } {sol.checkPrimeFrequency(nums) = }")
