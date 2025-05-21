from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        water = 0
        max_water = 0
        for i in range(n):
            for j in range(i + 1, n):
                water = min(height[i], height[j]) * (j - i)
                if water > max_water:
                    max_water = water
        return max_water


sol = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(f"{height = } {sol.maxArea(height) = }")

height = [1,1]
print(f"{height = } {sol.maxArea(height) = }")