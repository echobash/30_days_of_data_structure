from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_cumm_sum = []
        left_cumm_sum = []
        result = []
        curr_sum = 0

        n = len(nums)
        if n == 1:
            return [0]

        for i in range(n):
            curr_sum += nums[i]
            left_cumm_sum.append(curr_sum)

        curr_sum = 0
        for i in range(n - 1, -1, -1):
            curr_sum += nums[i]
            right_cumm_sum.append(curr_sum)

        right_cumm_sum = right_cumm_sum[::-1]

        for i in range(n):
            if i == 0:
                result.append(abs(right_cumm_sum[1]))
            elif i == n - 1:
                result.append(abs(left_cumm_sum[n - 2]))
            else:
                result.append(abs(left_cumm_sum[i - 1] - right_cumm_sum[i + 1]))
        return result


sol = Solution()

nums = [10,4,8,3]
print(f"{nums = } {sol.leftRightDifference(nums) = }")

nums = [1]
print(f"{nums = } {sol.leftRightDifference(nums) = }")