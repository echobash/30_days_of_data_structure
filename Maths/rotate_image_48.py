from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        We will transpose
        Then mirror the transpose matrix vertically
        """

        # Transpose the matrix - i.e swap upper half triangle and lower half triangle
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])

        # Mirror the transposed matrix vertically(by y-axis)

        # Loop on every row. But only half the length of row and swap
        for i in range(n):
            for j in range(n // 2):
                (matrix[i][j], matrix[i][n - j - 1]) = (matrix[i][n - j - 1], matrix[i][j])

        return matrix


sol = Solution()

matrix = [[1,2,-3],[4,-5,6],[7,8,-9]]
print(f"{matrix = } | {sol.rotate(matrix) = }")

matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(f"{matrix = } | {sol.rotate(matrix) = }")

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(f"{matrix = } | {sol.rotate(matrix) = }")

matrix = [[8]]
print(f"{matrix = } | {sol.rotate(matrix) = }")
