from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result_sum = 0
        for col in range(cols):
            for row in range(1,rows):
                if grid[row][col] <= grid[row-1][col]:
                    result_sum += grid[row-1][col] - grid[row][col] + 1
                    grid[row][col] += grid[row-1][col] - grid[row][col] + 1
        return result_sum


sol = Solution()

grid = [[3,2],[1,3],[3,4],[0,1]]
print(grid, sol.minimumOperations(grid))

grid = [[3,2,1],[2,1,0],[1,2,3]]
print(grid, sol.minimumOperations(grid))