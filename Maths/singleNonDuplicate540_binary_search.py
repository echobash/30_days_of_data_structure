from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]

        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            elif nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    # Look in right
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if (mid - 1) % 2 == 1:
                    # Look in left
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return nums[mid]


solution = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(f"{nums= }{ solution.singleNonDuplicate(nums)= }")

nums = [3,3,7,7,10,11,11]
print(f"{nums= }{ solution.singleNonDuplicate(nums)= }")

nums = [1,1,2,2, 3, 3,4,8,8]
print(f"{nums= }{ solution.singleNonDuplicate(nums)= }")

nums = [1,1,2,2, 3, 4,4,8,8]
print(f"{nums= }{ solution.singleNonDuplicate(nums)= }")