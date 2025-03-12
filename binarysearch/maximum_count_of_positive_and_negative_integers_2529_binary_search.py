from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        last_negative_index = -1
        first_positive_index = -1

        positive_count = 0
        negative_count = 0

        left, right = 0, n - 1

        # Get first_positive_index
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                first_positive_index = mid
                right = mid - 1

        # Get last_negative_index
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= 0:
                right = mid - 1
            else:
                last_negative_index = mid
                left = mid + 1

        if first_positive_index != -1:
            positive_count = n - first_positive_index

        if last_negative_index != -1:
            negative_count = last_negative_index + 1

        return max(negative_count, positive_count)


sol = Solution()


nums = [0]
print(f"{nums = } {sol.maximumCount(nums) = }")

nums = [-2,-1,-1,1,2,3]
print(f"{nums = } {sol.maximumCount(nums) = }")

nums = [-3,-2,-1,0,0,1,2]
print(f"{nums = } {sol.maximumCount(nums) = }")

nums = [5,20,66,1314]
print(f"{nums = } {sol.maximumCount(nums) = }")

nums = [-12,-11,-10,-9]
print(f"{nums = } {sol.maximumCount(nums) = }")
