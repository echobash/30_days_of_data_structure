from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if nums[1] < nums[0]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                # Go to right
                left = mid + 1
            else:
                # Go to left
                right = mid - 1


sol = Solution()

nums = [1, 2, 4, 5, 7, 8, 3]
print(f"{nums= } {sol.findPeakElement(nums)= }")

nums = [10, 20, 15, 2, 23, 90, 80]
print(f"{nums= } {sol.findPeakElement(nums)= }")

nums = [1, 2, 3]
print(f"{nums= } {sol.findPeakElement(nums)= }")

nums = [1,2,1,3,5,6,4]
print(f"{nums= } {sol.findPeakElement(nums)= }")

nums = [1,2,3,1]
print(f"{nums= } {sol.findPeakElement(nums)= }")
