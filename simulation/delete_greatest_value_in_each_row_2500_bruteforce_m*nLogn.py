from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 124
        # 331

        # 124
        # 113

        sorted_grid = []
        for row in grid:
            sorted_grid.append(sorted(row))

        ans = 0
        m, n = len(sorted_grid), len(sorted_grid[0])
        for i in range(n):
            max_val = 0
            for j in range(m):
                max_val = max(max_val, sorted_grid[j][i])
            ans += max_val
        return ans


sol = Solution()

grid = [[1,2,4],[3,3,1]]
print(f"{grid = } {sol.deleteGreatestValue(grid)}")

grid = [[10]]
print(f"{grid = } {sol.deleteGreatestValue(grid)}")