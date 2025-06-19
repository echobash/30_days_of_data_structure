from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total_sum = sum(nums)
        min_no = min(nums)
        n = len(nums)

        if target > total_sum:
            return 0

        if target == min_no:
            return 1

        if target == total_sum:
            return n

        # 2,3,5,2,8,3 -> target = 6
        curr_sum = 0
        min_len = n
        left = 0
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum >= target:
                while curr_sum >= target:
                    curr_len = i - left + 1
                    min_len = min(curr_len, min_len)
                    curr_sum -= nums[left]
                    left += 1
        return min_len


sol = Solution()

target = 7
nums = [2,3,1,2,4,3]
print(f"{target = } {nums = } {sol.minSubArrayLen(target, nums) = }")

target = 4
nums = [1,4,4]
print(f"{target = } {nums = } {sol.minSubArrayLen(target, nums) = }")

target = 11
nums = [1,1,1,1,1,1,1,1]
print(f"{target = } {nums = } {sol.minSubArrayLen(target, nums) = }")

target = 6
nums = [2,3,1,2,8,3]
print(f"{target = } {nums = } {sol.minSubArrayLen(target, nums) = }")

target = 7
nums = [8]
print(f"{target = } {nums = } {sol.minSubArrayLen(target, nums) = }")
