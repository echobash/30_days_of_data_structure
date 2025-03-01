from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        different_height_order = 0
        n = len(heights)
        sorted_heights = sorted(heights)
        for i in range(n):
            if sorted_heights[i] != heights[i]:
                different_height_order += 1
        return different_height_order

sol = Solution()

heights = [1,1,4,2,1,3]
print(f" {heights = } | {sol.heightChecker(heights) = }")

heights = [5,1,2,3,4]
print(f" {heights = } | {sol.heightChecker(heights) = }")

heights = [1,2,3,4,5]
print(f" {heights = } | {sol.heightChecker(heights) = }")
