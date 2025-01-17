from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # Move to left
                right = mid - 1
            else:
                # Move to right
                left = mid + 1
        return left


sol = Solution()

nums = [1,3,5,6]
target = 5
print(nums)
print(target,sol.searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(target,sol.searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(target,sol.searchInsert(nums, target))
