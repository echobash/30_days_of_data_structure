from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        total_count = 0
        for row, col in indices:
            # Increment the complete row
            for i in range(n):
                matrix[row][i] += 1

            # Increment the complete column
            for i in range(m):
                matrix[i][col] += 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 == 1:
                    total_count += 1

        return total_count


sol = Solution()

m = 2
n = 3
indices = [[0,1],[1,1]]
print(f"{m = } {n = } {indices = } {sol.oddCells(m, n, indices) = }")

m = 2
n = 2
indices = [[1,1],[0,0]]
print(f"{m = } {n = } {indices = } {sol.oddCells(m, n, indices) = }")
