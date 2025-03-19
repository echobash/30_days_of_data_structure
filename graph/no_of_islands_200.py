from typing import List


class Solution:
    def traverse_grid(self, grid, i, j, visited_set):

        if (
                i < 0 or
                j < 0 or
                i >= len(grid) or
                j >= len(grid[0]) or
                grid[i][j] == '0' or
                (i, j) in visited_set
        ):
            return 0
        visited_set.add((i, j))
        # down
        self.traverse_grid(grid, i + 1, j, visited_set)
        # right
        self.traverse_grid(grid, i, j + 1, visited_set)
        # left
        self.traverse_grid(grid, i - 1, j, visited_set)
        # up
        self.traverse_grid(grid, i, j - 1, visited_set)

        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        visited_set = set()
        total_count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                total_count = total_count + self.traverse_grid(grid, i, j, visited_set)
        return total_count


solution = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(f"{grid = } {solution.numIslands(grid) = }")

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(f"{grid = } {solution.numIslands(grid) = }")