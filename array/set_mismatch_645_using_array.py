from collections import defaultdict
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0, 0]
        count_mapping = defaultdict(int)

        for num in nums:
            count_mapping[num] += 1

        for num in range(1, n + 1):
            if count_mapping[num] == 2:
                result[0] = num

            if count_mapping[num] == 0:
                result[1] = num

        return result


sol = Solution()

nums = [1,2,2,4]
print(nums, sol.findErrorNums(nums))

nums = [1,1]
print(nums, sol.findErrorNums(nums))

nums = [2,2]
print(nums, sol.findErrorNums(nums))
