from typing import List
from math import log10,inf


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        result = []
        m,n = len(grid), len(grid[0])
        for i in range(n):
            max_length = float(-inf)
            for j in range(m):
                if grid[j][i] > 0:
                    max_length= max(max_length,int(log10(grid[j][i])+1))
                elif grid[j][i] < 0:
                    max_length= max(max_length,int(log10(-1 * grid[j][i])+1)+1)
                else:
                    max_length= max(max_length,1)
            result.append(max_length)
        return result


sol = Solution()

grid = [[1],[22],[333]]
print(f"{grid = }  {sol.findColumnWidth(grid) = }")

grid = [[-15,1,3],[15,7,12],[5,6,-2]]
print(f"{grid = }  {sol.findColumnWidth(grid) = }")
