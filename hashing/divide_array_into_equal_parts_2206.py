from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_frequency = Counter(nums)
        # Traverse the array and check if there is at least one such case where...
        # ... the count is odd

        for frequency in num_frequency.values():
            if frequency % 2 == 1:
                return False
        return True


sol = Solution()

nums = [3,2,3,2,2,2]
print(nums, sol.divideArray(nums))

nums = [1,2,3,4]
print(nums, sol.divideArray(nums))
