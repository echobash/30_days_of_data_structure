from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Look for strictly increasing - str_inc_max
        # Look for strictly decreasing - str_dec_max
        # local_max
        # global_max
        str_inc_max = 1
        str_dec_max = 1

        for i in range(n - 1):
            local_max = 1
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    local_max += 1
                else:
                    break
            str_inc_max = max(str_inc_max, local_max)

        for i in range(n - 1):
            local_max = 1
            for j in range(i + 1, n):
                if nums[j] < nums[j - 1]:
                    local_max += 1
                else:
                    break
            str_dec_max = max(str_dec_max, local_max)

        return max(str_dec_max, str_inc_max)


sol = Solution()

nums = [1,4,3,3,2]
print(f"{nums = } | {sol.longestMonotonicSubarray(nums) = }")

nums = [3,3,3,3]
print(f"{nums = } | {sol.longestMonotonicSubarray(nums) = }")

nums = [3,2,1]
print(f"{nums = } | {sol.longestMonotonicSubarray(nums) = }")

nums = [4,3,2,1]
print(f"{nums = } | {sol.longestMonotonicSubarray(nums) = }")

nums = [5,2]
print(f"{nums = } | {sol.longestMonotonicSubarray(nums) = }")

nums = [2,5]
print(f"{nums = } | {sol.longestMonotonicSubarray(nums) = }")
