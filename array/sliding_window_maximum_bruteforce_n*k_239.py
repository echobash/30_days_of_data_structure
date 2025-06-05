from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            max_no = float('-inf')
            for j in range(i, i+k):
                if nums[j] > max_no:
                    max_no = nums[j]
            result.append(max_no)
        return result


sol = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(f" {nums = } | {k = } | {sol.maxSlidingWindow(nums, k) = }")

nums = [1]
k = 1
print(f" {nums = } | {k = } | {sol.maxSlidingWindow(nums, k) = }")
