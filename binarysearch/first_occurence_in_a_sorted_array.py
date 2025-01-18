from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if nums[mid - 1] != target:  ###OUB
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # Move to right
                right = mid - 1
        return left


sol = Solution()

nums = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3]
target = 2
print(nums, target,sol.search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 11
print(nums, target,sol.search(nums, target))