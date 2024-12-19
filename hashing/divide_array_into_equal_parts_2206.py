from collections import defaultdict
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_mapping = defaultdict(int)
        # Store all the nums in the dictionary
        for num in nums:
            count_mapping[num] += 1

        # Traverse the dictionary and check if there is atleast one such case where...
        # ... the count is odd

        for num, count in count_mapping.items():
            if count % 2 == 1:
                return False
        return True


sol = Solution()

nums = [3,2,3,2,2,2]
print(nums, sol.divideArray(nums))

nums = [1,2,3,4]
print(nums, sol.divideArray(nums))
