from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_count = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    total_count += 1
        return total_count


sol = Solution()

nums = [3,1,2,2,2,1,3]
k = 2
print(f"{nums = } {k = } {sol.countPairs(nums, k) = }")

nums = [1,2,3,4]
k = 1
print(f"{nums = } {k = } {sol.countPairs(nums, k) = }")

nums = [3,1,2,12,2,12,3]
k = 2
print(f"{nums = } {k = } {sol.countPairs(nums, k) = }")