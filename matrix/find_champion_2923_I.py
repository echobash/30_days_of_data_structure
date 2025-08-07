from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        max_sum = 0
        ans = -1
        m,n = len(grid), len(grid[0])
        for i in range(m):
            if  sum(grid[i]) > max_sum:
                max_sum = sum(grid[i])
                ans = i
        return ans


sol = Solution()

grid = [[0,1],[0,0]]
print(f"{grid = } {sol.findChampion(grid) = }")
