from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums = sorted(nums)
        n = len(nums)
        min_diff = float('inf')
        for i in range(n - k + 1):
            min_diff = min(min_diff, (nums[i + k - 1] - nums[i]))
        return min_diff


sol = Solution()

nums = [90]
k = 1
print(f"{nums = } | {k = } | {sol.minimumDifference(nums, k) = }")

nums = [9,4,1,7]
k = 2
print(f"{nums = } | {k = } | {sol.minimumDifference(nums, k) = }")

nums = [100,200,300,400,500,600,601,602,603,604,900,1100,1300,1500,4500]
k = 3
print(f"{nums = } | {k = } | {sol.minimumDifference(nums, k) = }")

nums = [100,200,300,400,500,600,601,602,603,604,900,1100,1300,1500,4500]
k = 2
print(f"{nums = } | {k = } | {sol.minimumDifference(nums, k) = }")

nums = [100,200,300,400,500,600,601,602,603,604,900,1100,1300,1500,4500]
k = 5
print(f"{nums = } | {k = } | {sol.minimumDifference(nums, k) = }")

nums = [100,200,300,400,500,600,601,602,603,604,900,1100,1300,1500,4500]
k = 1
print(f"{nums = } | {k = } | {sol.minimumDifference(nums, k) = }")
