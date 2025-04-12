from typing import List
from math import ceil


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Traverse from Back
        # Inititalise empty set
        # If element not in set, store the element in set
        # If element found in set, get this index of duplicate element as i
        # Now find the no_of_elements_to_remove_from_front = i + 1
        # So min number of operations = ceil(no_of_elements_to_remove_from_front / 3)

        n = len(nums)
        nums_set = set()
        no_of_elements_to_remove_from_front = 0
        for i in range(n-1, -1, -1):
            if nums[i] not in nums_set:
                nums_set.add(nums[i])
            else:
                no_of_elements_to_remove_from_front = i + 1
                return ceil(no_of_elements_to_remove_from_front / 3)

        return 0


sol = Solution()

nums = [1,2,3,4,2,3,3,5,7]
print(f"{nums = } {sol.minimumOperations(nums) = }")

nums = [4,5,6,4,4]
print(f"{nums = } {sol.minimumOperations(nums) = }")

nums = [6,7,8,9]
print(f"{nums = } {sol.minimumOperations(nums) = }")
