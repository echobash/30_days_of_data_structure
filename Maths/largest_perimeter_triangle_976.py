from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        # 2,5,4,10
        # 2,4,5,10
        for i in range(n-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


sol = Solution()

n = [3,2,3,4]
print(f"{n = } | {sol.largestPerimeter(n) = }")

n = [1,2,1,10]
print(f"{n = } | {sol.largestPerimeter(n) = }")

n = [2, 1, 2]
print(f"{n = } | {sol.largestPerimeter(n) = }")

n = [7, 6, 2, 1, 5]
print(f"{n = } | {sol.largestPerimeter(n) = }")

n = [1, 1, 1, 2, 2, 2]
print(f"{n = } | {sol.largestPerimeter(n) = }")

n = [10, 15, 7, 6, 5]
print(f"{n = } | {sol.largestPerimeter(n) = }")

n = [3, 2, 3, 4]
print(f"{n = } | {sol.largestPerimeter(n) = }")
