from typing import List

from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        all_nums = []
        result = [0] * 2
        n = len(grid)
        for i in range(n):
            for j in range(n):
                all_nums.append(grid[i][j])

        all_nums_count = Counter(all_nums)
        for i in range(1, n ** 2 + 1):
            if all_nums_count[i] == 0:
                result[1] = i
            elif all_nums_count[i] == 2:
                result[0] = i

        return result


sol = Solution()

grid = [[1,3],[2,2]]
print(f"{grid = } {sol.findMissingAndRepeatedValues(grid) = }")

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(f"{grid = } {sol.findMissingAndRepeatedValues(grid) = }")
