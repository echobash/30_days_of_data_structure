from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target <= nums[mid]:
                    # Look in left
                    right = mid - 1
                else:
                    # Look in right
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                # Right part is sorted
                if nums[mid] <= target <= nums[right]:
                    # Look in right
                    left = mid + 1
                else:
                    # Look in left
                    right = mid - 1
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

nums = [15,18,20,25,30,35,40,45,5,10,12,14]
target = 25
print(f"{nums = } {sol.search(nums, target) = }")

nums = [15,18,20,25,30,35,40,45,5,10,12,14]
target = 12
print(f"{nums = } {sol.search(nums, target) = }")

nums = [15,18,20,25,30,35,40,45,5,10,12,14]
target = 10
print(f"{nums = } {sol.search(nums, target) = }")
