from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        max_water = 0
        left, right = 0, n - 1

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(water, max_water)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                # In case of equality, we can do anyone - left += 1 or right -= 1
                left += 1
        return max_water


sol = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(f"{height = } {sol.maxArea(height) = }")

height = [1,1]
print(f"{height = } {sol.maxArea(height) = }")