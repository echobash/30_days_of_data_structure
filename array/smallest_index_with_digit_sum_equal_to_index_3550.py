from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = float('inf')
        for i in range(n):
            digit_sum = 0
            number = nums[i]
            while number != 0:
                digit_sum += number % 10
                number //= 10
            if digit_sum == i:
                min_index = min(min_index, i)
        return min_index if min_index != float('inf') else -1


sol = Solution()

nums = [1,3,2]
print(f"{ nums = } {sol.smallestIndex(nums) =}")

nums = [1,10,11]
print(f"{ nums = } {sol.smallestIndex(nums) =}")

nums = [1,2,3]
print(f"{ nums = } {sol.smallestIndex(nums) =}")
