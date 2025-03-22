from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total_count = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0:
                    total_count += 1
        return total_count


sol = Solution()

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(f"{grid= } {sol.countNegatives(grid) = }")


grid = [[3,2],[1,0]]
print(f"{grid= } {sol.countNegatives(grid) = }")

grid = [[-4,-3,-2,-1],[-3,-2,-1,-1],[-1,-1,-1,-2],[-1,-1,-2,-3]]
print(f"{grid= } {sol.countNegatives(grid) = }")

grid = [[4,3,2,1],[3,2,1,1],[4,3,2,1],[3,2,1,1]]
print(f"{grid= } {sol.countNegatives(grid) = }")