from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # Move to left
                right = mid - 1
            else:
                # Move to right
                left = mid + 1
        return -1


sol = Solution()

nums = [3, 4, 6, 7, 9, 12, 16, 17]
target = 7
print(sol.search(nums, target))

nums = [-1,0,3,5,9,12]
target = 9
print(sol.search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
print(sol.search(nums, target))
