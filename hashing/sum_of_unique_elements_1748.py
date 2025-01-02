from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_count = Counter(nums)

        sum = 0
        for num,count in num_count.items():
            if count == 1:
                sum += num
        return sum


solution = Solution()

nums = [1,2,3,2]
print(nums, solution.sumOfUnique(nums))

nums = [1,1,1,1,1]
print(nums, solution.sumOfUnique(nums))

nums = [1,2,3,4,5]
print(nums, solution.sumOfUnique(nums))
