from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


sol = Solution()

nums = [4,5,6,7,0,1,2]
target = 0
print(f"{nums = } {sol.search(nums, target) = }")

nums = [4,5,6,7,0,1,2]
target = 3
print(f"{nums = } {sol.search(nums, target) = }")

nums = [1]
target = 0
print(f"{nums = } {sol.search(nums, target) = }")
