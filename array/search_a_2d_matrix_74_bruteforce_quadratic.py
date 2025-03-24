from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False

sol = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1],[10]]
target = 10
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")