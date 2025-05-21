from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in zero_row:
                        zero_row.add(i)
                    if j not in zero_col:
                        zero_col.add(j)

        for i in range(m):
            if i in zero_row:
                matrix[i] = [0] * n

        for i in range(n):
            for j in range(m):
                if i in zero_col:
                    matrix[j][i] = 0
        # returning matrix to show output. In Leetcode problem, we didn't had to return though
        return  matrix


sol = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(f" {matrix = } | {sol.setZeroes(matrix) = }")

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(f" {matrix = } | {sol.setZeroes(matrix) = }")