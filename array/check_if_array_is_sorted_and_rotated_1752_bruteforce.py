from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_list = sorted(nums)
        for i in range(n):
            nums = [nums[-1]]+nums[:n-1]
            if nums == sorted_list:
                return True
        return False


sol = Solution()

nums = [3,4,5,1,2]
print(f"{nums = } | {sol.check(nums) = }")

nums = [2,1,3,4]
print(f"{nums = } | {sol.check(nums) = }")

nums = [1,2,3]
print(f"{nums = } | {sol.check(nums) = }")

nums = [4,3,2,1]
print(f"{nums = } | {sol.check(nums) = }")

nums = [5,2]
print(f"{nums = } | {sol.check(nums) = }")

nums = [2,5]
print(f"{nums = } | {sol.check(nums) = }")
